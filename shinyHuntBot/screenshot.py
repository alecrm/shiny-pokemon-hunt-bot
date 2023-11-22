# PACKAGE IMPORTS
import os
import shutil

# PACKAGE IMPORTS
import pyautogui
from PIL import Image

# LOCAL IMPORTS
import config

###################################################################################################
###################################################################################################

# VARIABLES
###################################################################################################
screenshot_name = f'shiny_hunt.png'
screenshots_folder_path = f'{os.path.dirname(__file__)}/../screenshots/'
screenshot_path = os.path.join(screenshots_folder_path, screenshot_name)

###################################################################################################
###################################################################################################

# FUNCTIONS
###################################################################################################

def clear_screenshots():
    """Clears screenshots of previous run"""
    for file in os.listdir(screenshots_folder_path):
        file_path = os.path.join(screenshots_folder_path, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete [{file}] file.\nReason: {e}')


def take_screenshot():
    """Takes a screenshot of the desktop and crops it down to the pokemon battle. Update the config"""
    pyautogui.screenshot(f'screenshots/{screenshot_name}')
    screenshot = Image.open(screenshot_path)
    screenshot.crop(config.SCREENSHOT_CROP_COORDINDATES).save(screenshot_path)


def get_pixel_color(x, y):
    screenshot = Image.open(screenshot_path)
    pixels = screenshot.load()
    return pixels[x, y]