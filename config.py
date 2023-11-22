############################
##### EMULATOR CONFIGS #####
############################

# SYSTEM CONFIG VARIABLES
EMULATOR_EMPTY_CLICK_COORDINATES = (3022, 1246)         # x, y pixel coordinates of where to click into the emulator without clicking on the touch screen for DS emulators      THIS SHOULD BE UPDATED
MESPRIT_HUNT_TIMEOUT = 1200                             # Amount of time in seconds before assuming the run has failed and restarting the next run                              THIS SHOULD BE UPDATED
BATTLE_START_TIMEOUT = 300                              # Amount of time in seconds before assuming the run has failed and restarting the next run                              THIS SHOULD BE UPDATED


# CONTROL VARIABLES
A_BUTTON_KEYBIND = 'x'                                  # Update to what your emulator's keyboard binds to 'A' are                                                              THIS SHOULD BE UPDATED
B_BUTTON_KEYBIND = 'z'                                  # Update to what your emulator's keyboard binds to 'B' are                                                              THIS SHOULD BE UPDATED
X_BUTTON_KEYBIND = 's'                                  # Update to what your emulator's keyboard binds to 'X' are                                                              THIS SHOULD BE UPDATED
Y_BUTTON_KEYBIND = 'a'                                  # Update to what your emulator's keyboard binds to 'Y' are                                                              THIS SHOULD BE UPDATED
MENU_BUTTON_KEYBIND = 's'                               # Update to what your emulator's keyboard binds to open the menu are. Usually either 'Start' or 'X'                     THIS SHOULD BE UPDATED
FAST_FORWARD_TOGGLE_BUTTON_KEYBINDING = 'tab'           # Update to what your emulator's keyboard binds to removing FPS limit/toggle fast-forward                               THIS SHOULD BE UPDATED
RESET_BUTTON_KEYBIND = 'r'                              # Update to what your emulator's keyboard binds to soft resetting the game                                              THIS SHOULD BE UPDATED
UP_BUTTON_KEYBIND = 'up'                                # Update to what your emulator's keyboard binds to 'Move Up' are                                                        THIS SHOULD BE UPDATED
RIGHT_BUTTON_KEYBIND = 'right'                          # Update to what your emulator's keyboard binds to 'Move Right' are                                                     THIS SHOULD BE UPDATED
DOWN_BUTTON_KEYBIND = 'down'                            # Update to what your emulator's keyboard binds to 'Move Down' are                                                      THIS SHOULD BE UPDATED
LEFT_BUTTON_KEYBIND = 'left'                            # Update to what your emulator's keyboard binds to 'Move Left' are                                                      THIS SHOULD BE UPDATED


###########################
####### APP CONFIGS #######
###########################

# POKEMON NAME
POKEMON_NAME = 'Azelf'

# SCREENSHOT VARIABLES
SCREENSHOT_CROP_COORDINDATES = (2635, 88, 5119, 1439)   # LEFT, TOP, RIGHT, BOTTOM                                                                                              THIS SHOULD BE UPDATED


# PIXEL CHECK VARIABLES
HEALTH_BAR_PIXEL_CHECK_COORDINATES = (1170, 310)         # x, y pixel coordinates of where to check the health bar RGB                                                          THIS SHOULD BE UPDATED
HEALTH_BAR_RGB = (24, 195, 32)                          # RGB values of health bar. This should not need to be updated

SHINY_COLOR_PIXEL_CHECK_COORDINATES = (2004, 342)       # x, y pixel coordinates of where to check the pokemon color RGB                                                        THIS SHOULD BE UPDATED
NORMAL_COLOR_RGB = (182, 207, 247)                      # RGB values of the pokemon's NORMAL color. We check to make sure to stop the app if anything BUT this value is found   THIS SHOULD BE UPDATED

HAT_COLOR_CHECK_COORDINATES = (1550, 570)               # x, y pixel coordinates of where to check RGB for Dia's hat                                                            THIS SHOULD BE UPDATED
HAT_COLOR_RGB_LIST = [(219, 101, 105), (174, 81, 73), (190, 69, 65), (174, 69, 65), (134, 69, 93), (125, 60, 109), (219, 109, 125), (223, 109, 125), (223, 109, 121), (182, 89, 125)]
                                                        # ^^^ List of RGB colors that Dia's hat could be depending on the time of day and light shading. This should not need to be updated

MESPRIT_MAP_ICON_CHECK_COORDINATES = (150, 806)         # x, y pixel coordinates of where to check the map icon RGB                                                             THIS SHOULD BE UPDATED
MESPRIT_MAP_ICON_COLOR_RGB = (16, 40, 24)               # RGB values of the map icon for where Mesprit is                                                                       THIS SHOULD BE UPDATED