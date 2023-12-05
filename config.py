############################
##### EMULATOR CONFIGS #####
############################

# SYSTEM CONFIG VARIABLES
EMULATOR_EMPTY_CLICK_COORDINATES = (3022, 1246)         # x, y pixel coordinates of where to click into the emulator without clicking on the touch screen for DS emulators      THIS SHOULD BE UPDATED
MESPRIT_HUNT_TIMEOUT = 1200                             # Amount of time in seconds before assuming the run has failed and restarting the next run                              THIS SHOULD BE UPDATED
BATTLE_START_TIMEOUT = 300                              # Amount of time in seconds before assuming the run has failed and restarting the next run                              THIS SHOULD BE UPDATED
TRY_COUNT = 1
# ^^^ Current attempt number. Should start at 1 at the beginning of a hunt and be updated if you kill the app during the hunt and start it up again


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

VALID_POKEMON_LIST = ['Drifloon', 'Spiritomb', 'Rotom', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Darkrai', 'Shaymin', 'Arceus']


# POKEMON NAME
POKEMON_NAME = 'Giratina'


# SCREENSHOT VARIABLES
SCREENSHOT_CROP_COORDINDATES = (2635, 88, 2484, 1351)   # LEFT, TOP, WIDTH, HEIGHT                                                                                              THIS SHOULD BE UPDATED


# TODO: After a day of cycling through Mesprit, determine if these can be deleted
# PIXEL CHECK VARIABLES
# HAT_COLOR_CHECK_COORDINATES = (1550, 570)               # x, y pixel coordinates of where to check RGB for Dia's hat                                                            THIS SHOULD BE UPDATED
# HAT_COLOR_RGB_LIST = [(219, 101, 105), (174, 81, 73), (190, 69, 65), (174, 69, 65), (134, 69, 93), (125, 60, 109), (219, 109, 125), (223, 109, 125), (223, 109, 121), (182, 89, 125), (138, 69, 121), (154, 77, 125)]
                                                        # ^^^ List of RGB colors that Dia's hat could be depending on the time of day and light shading. This should not need to be update
