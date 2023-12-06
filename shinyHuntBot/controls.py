# COMMON IMPORTS
from time import sleep

# PACKAGE IMPORTS
import pyautogui

# LOCAL IMPORTS
import config

###################################################################################################
###################################################################################################

# CONTROL FUNCTIONS
###################################################################################################
def press_button(button: str, pause=0):
    """Actual key presses appeared to not be working, so keyDown and keyUp are used to simulate a button press"""
    pyautogui.keyDown(button)
    sleep(pause)
    pyautogui.keyUp(button)



# INTERACTION CONTROLS
def press_a():
    """Simulates pressing the 'A' button on the emulator. Uses the A_BUTTON_KEYBIND value from config file"""
    press_button(config.A_BUTTON_KEYBIND)


def press_b():
    """Simulates pressing the 'B' button on the emulator. Uses the B_BUTTON_KEYBIND value from config file"""
    press_button(config.B_BUTTON_KEYBIND)



# MOVEMENT CONTROLS
def move_up(spaces: int):
    """
    Moves a given number of spaces up on normal speed. Note that fast foward increases the number of steps by ~ 1.5
    """
    i = 1
    while i <= spaces:
        press_button(config.UP_BUTTON_KEYBIND)
        sleep(0.2)
        i += 1

def run_up(spaces: int):
    """
    Runs a given number of spaces up on normal speed. Note that fast foward increases the number of steps by ~ 1.5
    """
    with pyautogui.hold(config.B_BUTTON_KEYBIND):
        move_up(spaces)

def run_up_for(time: int):
    """Runs right for a given amount of time"""
    with pyautogui.hold(config.B_BUTTON_KEYBIND):
        press_button(config.UP_BUTTON_KEYBIND, time)


def move_right(spaces: int):
    """
    Moves a given number of spaces right on normal speed. Note that fast foward increases the number of steps by ~ 1.5
    """
    i = 1
    while i <= spaces:
        press_button(config.RIGHT_BUTTON_KEYBIND)
        sleep(0.2)
        i += 1

def run_right(spaces: int):
    """
    Runs a given number of spaces right on normal speed. Note that fast foward increases the number of steps by ~ 1.5
    """
    with pyautogui.hold(config.B_BUTTON_KEYBIND):
        move_right(spaces)

def run_right_for(time: int):
    """Runs right for a given amount of time"""
    with pyautogui.hold(config.B_BUTTON_KEYBIND):
        press_button(config.RIGHT_BUTTON_KEYBIND, time)


def move_down(spaces: int):
    """
    Moves a given number of spaces down on normal speed. Note that fast foward increases the number of steps by ~ 1.5
    """
    i = 1
    while i <= spaces:
        press_button(config.DOWN_BUTTON_KEYBIND)
        sleep(0.2)
        i += 1

def run_down(spaces: int):
    """
    Runs a given number of spaces down on normal speed. Note that fast foward increases the number of steps by ~ 1.5
    """    
    with pyautogui.hold(config.B_BUTTON_KEYBIND):
        move_down(spaces)

def run_down_for(time: int):
    """Runs down for a given amount of time"""
    with pyautogui.hold(config.B_BUTTON_KEYBIND):
        press_button(config.DOWN_BUTTON_KEYBIND, time)
    

def move_left(spaces: int):
    """
    Moves a given number of spaces left on normal speed. Note that fast foward increases the number of steps by ~ 1.5
    """
    i = 1
    while i <= spaces:
        press_button(config.LEFT_BUTTON_KEYBIND)
        sleep(0.2)
        i += 1

def run_left(spaces: int):
    """
    Runs a given number of spaces right on normal speed. Note that fast foward increases the number of steps by ~ 1.5
    """
    with pyautogui.hold(config.B_BUTTON_KEYBIND):
        move_left(spaces)

def run_left_for(time: int):
    """Runs left for a given amount of time"""
    with pyautogui.hold(config.B_BUTTON_KEYBIND):
        press_button(config.LEFT_BUTTON_KEYBIND, time)



# MENU CONTROLS
def open_menu():
    """Opens the menu in game"""
    press_button(config.MENU_BUTTON_KEYBIND)



# SYSTEM CONTROLS
def reset():
    """Soft resets the emulator using the bound reset hotkey"""
    press_button(config.RESET_BUTTON_KEYBIND)


def toggle_fast_forward():
    """Toggles the fast forward mode on by pressing down and releasing 'TAB'"""
    press_button(config.FAST_FORWARD_TOGGLE_BUTTON_KEYBINDING)