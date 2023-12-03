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
base_image_check_folder_path = f'{os.path.dirname(__file__)}/../image_checks/'

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
    clear_screenshots()
    pyautogui.screenshot(f'screenshots/{screenshot_name}', config.SCREENSHOT_CROP_COORDINDATES)

# TODO: Set a base pixel size and have a config for screen size. Then multiply base size by value?
def check_for_image(image_name: str) -> bool:
    try:
        # take_screenshot()
        image_path = os.path.join(base_image_check_folder_path, image_name)
        image = Image.open(image_path)
    except IOError:
        raise IOError(f'Could not find an image at this location: [{image_path}]')
    
    if pyautogui.locateOnScreen(image) == None:
        return False
    else:
        return True
    

def check_for_shiny(pokemon_name: str) -> bool:
    return not check_for_image(f'pokemon/{pokemon_name}/image.png')


def check_in_battle() -> bool:
    return check_for_image('in_battle_check.png')


def check_for_recap_screen() -> bool:
    return check_for_image('recap_screen_check.png')