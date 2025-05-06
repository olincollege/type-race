# type-race
[Website](https://olincollege.github.io/type-race/)

# Project Summary

**type-race** is an exciting game that puts your typing skills to the test! Choose to race the clock in the single player game mode, or challenge a friend through our local online multiplayer.

When the game starts, you have 60 seconds to copy as much of the prompt on your screen as you can. As you type, the prompt will scroll. If you make a mistake, no worries! Mistakes are underlined in red and can be fixed with the backspace key. In the top left, view the time remaining, your current words per minute, and your opponent's words per minute (if playing multiplayer).

# Setup

## General Requirements

The **single player** game mode can be played with or without an internet connection on any computer. **Git** and **pip** are pre-requisites to use.

To play multiplayer, an internet connection is required. Both players must be connected to the same network, and some networks with locked down settings will not allow the connection to form. **At Olin, use OLIN-DEVICES, not OLIN** In order to host a multiplayer game, the host must run the game from MacOS, Windows, and most Linux systems. 

> [!NOTE]  
> The host can **not** run the game from WSL. Network ports in WSL are not accessible to outside devices.

## Python Dependencies

Our program is built to run with **Python 3.12**. Download python
[here](https://www.python.org/downloads/).

Our program relies on the following dependencies:

1. **pygame** is used to handle user input and to create the GUI. Install with:
```bash
pip install pygame
```
2. **pytest** is used for unit tests. Install with:
```bash
pip install pytest
```

# Playing type-race

## Single player

To play single player:

1. Clone the online repository onto your local computer with `git clone PASTE_HTTPS_KEY_HERE`
2. Navigate to the *type-race* directory (`cd type-racer`)
3. In the terminal, run `python main.py` to launch the game
4. When prompted on-screen type 's' to play single player

## Multiplayer

Two laptops are required to play type-race multiplayer. One player will serve as the host and the other player will serve as the client.

### Host Instructions

1. Clone the online repository onto your local computer with `git clone PASTE_HTTPS_KEY_HERE`
2. Navigate to the *type-race* directory (`cd type-racer`)
3. In the terminal, run `python main.py` to launch the game
4. When prompted on-screen type 'h' to play as the host

**If hosting on Windows**, there a couple of things to keep in mind:
- The first time you play as host, you will get a popup asking if you want the program to communicate over public and private networks. **Click Allow**. If you fail to do this, you will have to manually add a Windows Defender firewall inbound rule to allow TCP on port 5555.
- If the game fails unexpectedly, you might into the following error next time you attempt to host: `SERVER: Failed to bind server [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions`. This means that the port was not properly closed from the last game session. To rectify this, do the following from an **administrator** powershell terminal:
    - Run: `netstat -ano | findstr :5555`. Look for the last 4 numbers in the output that follows. These numbers represent the PID.
    - Run: `taskkill /PID 0000 /F`. Replace *0000* with the PID from the last step.

### Client Instructions

1. Navigate to the *type-race* directory (`cd type-racer`)
2. In the terminal, run `python main.py` to launch the game
3. When prompted on-screen type 'c' to play as the client
4. Enter the IP address displayed on the **host's** screen when prompted
