"""
Contains a classes to support networking for multiplayer game mode.
"""

import socket
import threading
import time
from abc import ABC, abstractmethod
import platform
import subprocess
import sys
import os

PORT = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Network(ABC):
    """
    Base class to support networking between a host and client.

    Attributes:
        _player: HostPlayer object representing the model of the host
            player
        _host_ip: string representing the IPv4 address of the host computer
    """

    def __init__(self, player):
        self._player = player
        self._host_ip = self.get_host_ip()

    def transmit_receive_wpm(self, conn):
        """
        Threaded function that exchanges wpm with the other player. Continuously
        transmit this player's wpm and receive the opponent's wpm.

        Args:
            conn: socket object representing the connection to the other player
        """
        while True:
            my_wpm = self._player.wpm
            conn.send(str(my_wpm).encode())

            opponent_wpm = conn.recv(1024).decode()
            if opponent_wpm:
                self._player.opponent_wpm = int(opponent_wpm)
            else:
                print("SERVER: No data received, close connection")
                break

            if self._player.game_over:
                print("SERVER: Game ended, close connection (player.game_over)")
                break
            time.sleep(0.5)

    @abstractmethod
    def get_host_ip(self):
        """
        Find the IPv4 address of the host device.

        Return a string containing the IPv4 address. The address consists of a
        set of 4 numbers, separated by periods.
        """


class Host(Network):
    """
    Class controlling networking for the host player. Extends the Network base
    class to creates a server for the client to connect to.
    """

    def get_host_ip(self):
        """
        Find the IPv4 address of the current device.

        Return a string containing the IPv4 address. The address consists of a
        set of 4 numbers, separated by periods.
        """
        if (
            "microsoft" in platform.uname().release.lower()
            or "wsl" in platform.release().lower()
        ):
            print(
                "🚫 WSL detected — use host mode from macOS, Windows, or Linux"
                " instead."
            )
            return "127.0.0.1"

        system = platform.system()

        # --- macOS ---
        if system == "Darwin":
            try:
                result = subprocess.run(
                    ["ipconfig", "getifaddr", "en0"],
                    capture_output=True,
                    text=True,
                )
                ip = result.stdout.strip()
                if ip:
                    print(f"🟢 macOS detected. Wi-Fi IP: {ip}")
                    return ip
            except Exception as e:
                print("❌ Failed to get macOS IP:", e)

        # --- Windows ---
        elif system == "Windows":
            try:
                hostname = socket.gethostname()
                ip = socket.gethostbyname(hostname)
                if ip and not ip.startswith("127."):
                    print(f"🟢 Windows detected. Host IP: {ip}")
                    return ip
            except Exception as e:
                print("❌ Failed to get Windows IP:", e)

        # --- Linux (non-WSL) ---
        elif system == "Linux":
            try:
                result = subprocess.run(
                    ["hostname", "-I"], capture_output=True, text=True
                )
                ip_list = result.stdout.strip().split()
                for ip in ip_list:
                    if not ip.startswith("127."):
                        print(f"🟢 Linux detected. Host IP: {ip}")
                        return ip
            except Exception as e:
                print("❌ Failed to get Linux IP:", e)

        print("⚠️ Could not detect a LAN IP. Using localhost.")
        return "127.0.0.1"

    def start_server(self):
        """
        Attempt to start a new server by binding the socket to the ip address
        and port. Then start a new thread to transmit and receive wpm.
        """
        try:
            s.bind((self._host_ip, PORT))
        except socket.error as e:
            print("SERVER: Failed to bind server", e)

        client_conn = self.find_client()
        thread = threading.Thread(
            target=self.transmit_receive_wpm, args=(client_conn,)
        )
        thread.start()

    def find_client(self):
        """
        Wait for the client to connect. Blocks all other code execution until a
        connection is established.
        """
        s.listen()
        print("SERVER: Waiting for a connection, Server Started")

        conn, addr = s.accept()
        print("SERVER: Connected to:", addr)
        return conn


class Client(Network):
    """
    Class controlling networking for the client player. Extends the Network
    base class to connect to the server created by the host.
    """

    def get_host_ip(self):
        """
        Prompt the user to enter the IP address of the host.

        Returns a string with the user's input.
        """
        return input(
            "\nPlease enter the hosts' IP address (displayed on their screen): "
        )

    def connect_server(self):
        """
        Connect to the server created by the host. Then start a new thread to
        transmit and receive wpm.
        """
        try:
            s.connect((self._host_ip, PORT))
        except socket.error as e:
            print("SERVER: Connection Failed", e)

        thread = threading.Thread(target=self.transmit_receive_wpm, args=(s,))
        thread.start()
