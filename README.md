# type-race
[Website]() | [Video]()

# Project Summary

**type-race** is an exciting game that puts your typing skills to the test! Choose to race the clock in the single player game mode, or challenge a friend through our local online multiplayer.

When the game starts, you have 60 seconds to copy as much of the prompt on your screen as you can. As you type, the prompt will scroll. If you make a mistake, no worries! Mistakes are underlined in red and can be fixed with the backspace key. In the top left, view the time remaining, your current words per minute, and your opponent's words per minute (if playing multiplayer).

# Setup

## General Requirements

The **single player** game mode can be played with or without an internet connection on any computer. To play multiplayer, an internet connection is required. In order to host a multiplayer game, the host must run the game from MacOS, Windows, and most Linux systems. 

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

1. Navigate to the *type-race* directory (`cd type-racer`)
2. In the terminal, run `python main.py` to launch the game
3. When prompted on-screen type 's' to play single player

## Multiplayer

Two laptops are required to play type-race multiplayer. One player will serve as the host and the other player will serve as the client.

### Host Instructions

1. Navigate to the *type-race* directory (`cd type-racer`)
2. In the terminal, run `python main.py` to launch the game
3. When prompted on-screen type 'h' to play as the host

### Client Instructions

1. Navigate to the *type-race* directory (`cd type-racer`)
2. In the terminal, run `python main.py` to launch the game
3. When prompted on-screen type 'c' to play as the client
4. Enter the IP address displayed on the **host's** screen when prompted
