---
permalink: /setup
layout: page
title: Setup
---
## General Requirements

The **single player** game mode can be played with or without an internet connection on any computer. To play multiplayer, an internet connection is required. Both players must be connected to the same network, and some networks with locked down settings will not allow the connection to form. **At Olin, use OLIN-DEVICES, not OLIN** In order to host a multiplayer game, the host must run the game from MacOS, Windows, and most Linux systems. 

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
