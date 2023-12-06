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


def check_for_image(search_image_name: str, parent_image_path: str = None, confidence: int = 0.9) -> bool:
    """Looks for a given image inside a given screenshot. If no screenshot is given, it takes a screenshot"""
    # Tries to get the image from the name
    parent_image = None
    try:
        search_image_path = os.path.join(base_image_check_folder_path, search_image_name)
        search_image = Image.open(search_image_path)
    except IOError:
        raise IOError(f'Could not find an image at this location: [{search_image_path}]')
    
    # If a search image path is provided, tries to get the image from the path.
    #  If no search image path is provided, takes a screenshot and uses this image
    if parent_image_path != None:
        try:
            parent_image = Image.open(parent_image_path)
        except IOError:
            raise IOError(f'Could not find an image at this location: [{parent_image_path}]')
    else:
        take_screenshot()
        try:
            parent_image = Image.open(screenshot_path)
        except IOError:
            raise IOError(f'Could not find an image at this location: [{screenshot_path}]')

    # Resizes the taken screenshot to roughly match the size that the image check images were taken at
    parent_image = parent_image.resize((2484, 1351))

    # Attempts to locate the search image inside the parent image
    if pyautogui.locate(search_image, parent_image, confidence=confidence) == None:
        return False
    else:
        return True
    

def check_for_shiny(pokemon_name: str) -> bool:
    """Checks to see if the base pokemon screenshot is NOT currently on the screen"""
    return not check_for_image(f'pokemon/{pokemon_name}.png', confidence=0.97)


def check_in_battle() -> bool:
    """Checks to see if the enemy's health bar is currently on the screen"""
    return check_for_image('in_battle_check.png')


def check_for_recap_screen() -> bool:
    """Checks to see if the recap screen is currently displaying"""
    return check_for_image('recap_screen_check.png')


def check_mesprit_is_here() -> bool:
    """
    Checks to see if Mesprit is currently in our route. We first try to get a screenshot
    that has the roaming pokemon icon visible. We then check to see if the roaming
    pokemon icon is in the same route as us
    """
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
        return check_for_image('mesprit_location_images/mesprit_location_check-1.png', image_path, confidence=0.788) or check_for_image('mesprit_location_images/mesprit_location_check-2.png', image_path, confidence=0.788)
    else:
        return False


def check_for_path() -> bool:
    """Checks if we're in battle or not by looking for the route path"""
    return check_for_image('pathway_check.png', confidence=0.5)