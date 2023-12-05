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


def take_screenshot(name: str = None, region=None):
    """Takes a screenshot of the desktop and crops it down to the pokemon battle. Update the config"""
    clear_screenshots()
    if region == None:
        region = config.SCREENSHOT_CROP_COORDINDATES
    if name != None:
        pyautogui.screenshot(f'screenshots/{name}', region)
    else:
        pyautogui.screenshot(f'screenshots/{screenshot_name}', region)


# TODO: Set a base pixel size and have a config for screen size. Then multiply base size by value?
def check_for_image(image_name: str, search_image_path: str = None, confidence: int = 0.999) -> bool:
    search_image = None
    try:
        image_path = os.path.join(base_image_check_folder_path, image_name)
        image = Image.open(image_path)
    except IOError:
        raise IOError(f'Could not find an image at this location: [{image_path}]')
    
    if search_image_path != None:
        try:
            search_image = Image.open(search_image_path)
        except IOError:
            raise IOError(f'Could not find an image at this location: [{search_image_path}]')
    else:
        take_screenshot()
        try:
            search_image = Image.open(screenshot_path)
        except IOError:
            raise IOError(f'Could not find an image at this location: [{screenshot_path}]')

    search_image = search_image.resize((2484, 1351))
    if pyautogui.locate(image, search_image, confidence=confidence) == None:
        return False
    else:
        return True
    

def check_for_shiny(pokemon_name: str) -> bool:
    return not check_for_image(f'pokemon/{pokemon_name}.png')


def check_in_battle() -> bool:
    return check_for_image('in_battle_check.png')


def check_for_recap_screen() -> bool:
    return check_for_image('recap_screen_check.png')


def check_mesprit_is_here() -> bool:
    max_tries = 10
    attempt = 1
    is_icon_visible = False

    while attempt <= max_tries:
        image_name = f'mesprit_icon_hunt.png'
        take_screenshot(image_name)
        image_path = os.path.join(screenshots_folder_path, image_name)

        if check_for_image('mesprit_location_images/mesprit_icon_visible_check.png', image_path, confidence=0.9):
            is_icon_visible = True
            break
        else:
            attempt += 1

    if is_icon_visible:
        return check_for_image('mesprit_location_images/mesprit_location_check-1.png', image_path, confidence=0.9) or check_for_image('mesprit_location_images/mesprit_location_check-2.png', image_path, confidence=0.9)
    else:
        return False


def check_for_path() -> bool:
    """Checks if we're in battle or not by looking for the route path"""
    return check_for_image('pathway_check.png', confidence=0.5)