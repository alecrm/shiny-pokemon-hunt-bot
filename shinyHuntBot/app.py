# IMPORTS
###################################################################################################
# DEFAULT IMPORTS
from time import localtime
from time import sleep
from time import strftime
from time import time

#PACKAGE IMPORTS
import pyautogui

# LOCAL IMPORTS
import config
import controls
import screenshot

###################################################################################################
###################################################################################################



# VARIABLES
###################################################################################################
# boolean checks
is_in_battle = True

# Message displayed when ending app
exit_message = 'Woah, something went oopsies'

# Counters
try_count = config.TRY_COUNT
failure_count = 0

# Capitalize pokemon name to ensure it matches the format we expect to see
pokemon_name = config.POKEMON_NAME.upper() if config.POKEMON_NAME.upper() == 'SETUP' else config.POKEMON_NAME.lower().capitalize()

###################################################################################################
###################################################################################################



# FUNCTIONS
###################################################################################################

def skip_dialogue(num_times: int, pause: int = 0.3):
    """
    Skips through dialogue when initiating the static encounter.
    'num_times' should be the number of times you have to press 'A'
    """
    i = 1
    while i <= num_times:
        controls.press_a()
        sleep(pause)
        i += 1


def load_game():
    """
    Hacky method to maneuver from resetting the game to initiating the static encounter.
    We do a combination of pressing 'A' and waiting some time to get through each screen.
    """
    # Soft reset emulator
    controls.reset()
    sleep(12)

    # Press A to skip intro screen
    controls.press_a()
    sleep(2)

    # Press A to move past title screen
    controls.press_a()
    sleep(4)

    # Press A to load the game
    controls.press_a()
    sleep(3)


def check_for_recap_screen():
    """
    Looks to see if the game is showing the recap screen after loading a save file.
    If it is, we cancel out of it and save the game quickly so that it stops showing up.
    This adds time to the run where we save to stop it from appearing, but ultimately saves
    time across all following runs
    """
    screenshot.take_screenshot()
    if screenshot.check_for_recap_screen():
        controls.press_b()
        sleep(3)
        controls.open_menu()
        controls.move_down(4)
        controls.press_a()
        sleep(2)
        controls.press_a()
        sleep(2)
        controls.press_a()
        sleep(10)


def is_in_battle() -> bool:
    """
    Checks if we are in a battle by searching the game screenshot for the enemy's health bar
    """
    global is_in_battle
    global failure_count
    if not screenshot.check_in_battle():
        failure_count += 1
        return False
    else:
        failure_count = 0
        return True


def is_shiny_check() -> bool:
    """
    Checks if the pokemon is shiny be looking to see if the pokemon's default picture is found
    in the game screenshot. If it IS found, the pokemon is not shiny. If it IS NOT found,
    the pokemon is likely shiny (or potentially something went wrong)
    """
    global exit_message
    global try_count
    if screenshot.check_for_shiny(pokemon_name):
        exit_message = f'CONGRATS ON YOUR SHINY {pokemon_name.upper()}!!! :) It only took {try_count} {"try" if try_count == 1 else "tries"}!'
        return True
    else:
        try_count +=1
        return False

###################################################################################################
###################################################################################################



# MAIN CALL FUNCTIONS
###################################################################################################
def static_shiny_hunt():
    """
    Main function for hunting static encounter pokemon. This effectively handles Rotom, Spiritomb,
    Drifloon, and all legendaries except for Mesprit and Cresselia. Basically, we just soft reset the
    emulator, trigger the static encounter battle, and check if the pokemon is shiny. If not, we repeat
    """
    global try_count
    global exit_message

    while True:
        start_time = time()
        # Displays the current attempt start time and number
        print(f'{strftime("%Y-%m-%d %I:%M:%S %p", localtime(time()))} --- Attempt number: {try_count}')

        # Soft resets emulator and initiates the battle
        load_game()
        check_for_recap_screen()

        # Press A to battle Pokemon
        controls.press_a()
        sleep(.6)

        if pokemon_name == 'Rotom':
            skip_dialogue(3)
        else:
            skip_dialogue(1)
        sleep(9)

        # Confirms the emulator successfully got into the battle. Kills the app after 10 consecutive failures
        if not is_in_battle():
            print(f'Failed to get into the battle. Trying again! Failure count: {failure_count}')
            if failure_count >= 10:
                exit_message = f'Cycle continuously failed to get into a battle. Killing app.'
                break
            else:
                continue

        # Checks if the pokemon is shiny
        if is_shiny_check():
            break

        # Calculates and prints failed attempt length
        elapsed_time = time() - start_time
        print(f'This attempt took: {strftime("%M minutes and %S seconds", localtime(elapsed_time))}\n')
    
    # Calculates and prints successful attempt length
    elapsed_time = time() - start_time
    print(f'This attempt took: {strftime("%M minutes and %S seconds", localtime(elapsed_time))}\n')


def mesprit_shiny_hunt():
    """
    Main function for hunting Mesprit. Because the roaming pokemon (Mesprit and Cresselia)
    are so unique (aka annoying), they get their entire own function. Yay!
    """
    global try_count
    global exit_message
    
    
    while True:
        should_restart = False
        start_time = time()
        # Displays the current attempt start time and number
        print(f'{strftime("%Y-%m-%d %I:%M:%S %p", localtime(time()))} --- Attempt number: {try_count}')

        ######################################### STARTING GAME #########################################
        # Soft resets game
        load_game()
        check_for_recap_screen()

        ################################### TRIGGERING MESPRIT HUNT ####################################
        # Skip through Mesprit disappearing
        skip_dialogue(3, 1.5)
        sleep(2)

        # Skip through Rowan appearing
        skip_dialogue(1, 1.5)
        sleep(2)

        # Skip through Rowan's dialogue part 1
        skip_dialogue(8, 1.5)
        sleep(2)

        # Skip through Rowan's dialogue part 2
        skip_dialogue(8, 1.5)
        sleep(2.75)

        ######################################## Exiting Cave ###########################################
        # Runs right to align with cave entrance
        controls.run_right_for(0.26)
        # sleep(0.3)

        # Runs down to exit cave
        controls.run_down_for(2.2)
        sleep(2.75)

        ####################################### Fly to Jubilife ########################################
        # Opens menu and opens 'Pokemon' screen
        controls.open_menu()
        controls.move_down(1)
        controls.press_a()
        sleep(1.75)

        # Selects flying pokemon and selects 'Fly'
        # controls.toggle_fast_forward() # We slow it down so that we're able to easily select a pokemon
        controls.move_down(1)
        controls.press_a()
        controls.move_down(1)
        controls.press_a()
        sleep(1.5)

        # Selects Jubilife city as the destination to fly to
        controls.move_right(2)
        controls.move_up(2)
        # controls.toggle_fast_forward() # We speed up now to zoom through the fly cutscene
        sleep(0.2)
        controls.press_a()
        sleep(10.3)

        #################################### Navigate to Route 202 #####################################
        # Moves to the left and then down to get out of Jubilife City
        controls.run_left_for(0.8)
        controls.run_down_for(3.05)
        controls.run_right_for(0.65)
        controls.run_down_for(1.6)

        ####################################### Hunt for Mesprit ########################################
        # Continues to move between Jubilife City & Route 202 until Mesprit arrives
        start_hunt_time = time() # Used to track how long we're hunting for Mesprit
        while True:

            # Breaks out of the loop once Mesprit has arrived
            if screenshot.check_mesprit_is_here():
                break

            # Restarts the app if we've been trying for more than 20 minutes
            if (time() - start_hunt_time) > config.MESPRIT_HUNT_TIMEOUT:
                should_restart = True
                break

            # If Mesprit is still not here, moves up into Jubilife City and back down into Route 202
            controls.run_up_for(1.4)
            controls.run_down_for(1.4)
        
        # Checks to see if we broke out of the mesprit hunt to restart
        if should_restart:
            print('TOOK TOO LONG TO HUNT MESPRIT. RESTARTING ATTEMPT!!!')
            continue

        ####################################### Apply Max Repel ########################################
        # Opens bag
        controls.open_menu()
        controls.move_down(1)
        controls.press_a()
        sleep(1.75)

        # Applies Max Repel
        controls.press_a()
        sleep(0.4)
        controls.press_a()
        sleep(0.4)
        controls.press_a()
        sleep(0.4)

        # Closes bag
        controls.press_b()
        sleep(2)
        controls.press_b()
        sleep(0.4)

        ####################################### Trigger battle #########################################
        # Moves into grass
        controls.move_right(2)

        # Continues to move in the grass until we find Mesprit
        start_battle_time = time() # Used to track how long we've been trying to initiate a battle
        while True: 
            # screenshot.take_screenshot()

            # If we don't see the route path, we recognize we're in a battle and break out of the loop
            if not screenshot.check_for_path():
                sleep(9)
                break

            # Restarts the app if we've been trying for more than 5 minutes
            if (time() - start_battle_time) > config.BATTLE_START_TIMEOUT:
                should_restart = True
                break

            # If we're still not in the battle, we'll run to the right and run back to the left
            controls.run_right_for(0.5)
            controls.run_left_for(0.5)
            sleep(1.5)

        # Checks to see if we broke out of the mesprit hunt to restart
        if should_restart:
            print('TOOK TOO LONG TO HUNT MESPRIT. RESTARTING ATTEMPT!!!')
            continue
        
        ################################## Check for Shiny Mesprit #####################################
        # Checks if the pokemon is shiny
        if is_shiny_check():
            break
        
        # Calculates and prints failed attempt length
        elapsed_time = time() - start_time
        print(f'This attempt took: {strftime("%M minutes and %S seconds", localtime(elapsed_time))}\n')
    
    # Calculates and prints successful attempt length
    elapsed_time = time() - start_time
    print(f'This attempt took: {strftime("%M minutes and %S seconds", localtime(elapsed_time))}\n')


# TODO: Implement cresselia_shiny_hunt
def cresselia_shiny_hunt():
    """
    Main function for hunting Cresselia. Because the roaming pokemon (Cresselia and Mesprit)
    are so unique (aka annoying), they get their entire own function. Yay!
    """
    raise NotImplementedError('Cresselia shiny hunt method has not been implemented yet')


def setup_crop_coordinates():
    """
    Setup method for guiding users through getting the values to set the [SCREEN_CROP_COORDINATES] config value
    """
    # Grabs the LEFT coordinate value
    print(f'\nPlease position your mouse at the very left side of the emulator window within 5 seconds')
    sleep(5)
    left, _ = pyautogui.position()
    print(f'Left value: {left}\n{config.MESSAGE_SPACING_SYMBOLS}')

    # Grabs the TOP coordinate value
    print(f'\nPlease position your mouse at the top of the actual emulator window (Just below the menu bar) within 5 seconds')
    sleep(5)
    _, top = pyautogui.position()
    print(f'Top value: {top}\n{config.MESSAGE_SPACING_SYMBOLS}')

    # Grabs the WIDTH coordinate value
    print(f'\nPlease position your mouse at the very right side of the emulator window within 5 seconds')
    sleep(5)
    right, _ = pyautogui.position()
    width = right - left
    print(f'Width value: {width}\n{config.MESSAGE_SPACING_SYMBOLS}')

    # Grabs the HEIGHT coordinate value
    print(f'\nPlease position your mouse at the very bottom side of the emulator window within 5 seconds')
    sleep(5)
    _, bottom = pyautogui.position()
    height = bottom - top
    print(f'Bottom value: {bottom}\n{config.MESSAGE_SPACING_SYMBOLS}')

    config_value = (left, top, width, height)
    print(f'\nPlease replace the [SCREEN_CROP_COORDINATES] with this value (including parentheses): {config_value}')


# TODO: Update is_shiny() method so that it compares an partial image of the hunted pokemon against the screenshot
#        - Have a folder structure of pokemon_compare_images/$POKEMON_NAME/image.png
if __name__ == "__main__":
    """
    Main app function call. Chooses which shiny hunt function to
    use on the the pokemon set in the [POKEMON_NAME] config value
    """
    # Confirms the pokemon name set in the config file is a valid option
    if pokemon_name not in config.VALID_POKEMON_LIST and pokemon_name != 'SETUP':
        raise ValueError(f'[{pokemon_name}] is not a valid pokemon to shiny hunt! Please select from the list of available pokemon')
        
    # Quick pause at the start of the app in case the user needs to switch to the emulator window
    sleep(3)
    
    # Decides what startup message to print
    if pokemon_name == 'SETUP':
        print(f'{config.MESSAGE_SPACING_SYMBOLS}\nRunning Screen Position Setup. Please ensure your emulator window is full screen and active\n{config.MESSAGE_SPACING_SYMBOLS}')
    else:
        print(f'{config.MESSAGE_SPACING_SYMBOLS}\nStarting hunt for shiny {pokemon_name}!\n{config.MESSAGE_SPACING_SYMBOLS}')
        pyautogui.click(*config.EMULATOR_EMPTY_CLICK_COORDINATES)
        sleep(0.3)

    # SHINY HUNT FUNCTION CALL
    match pokemon_name:
        case 'SETUP':
            setup_crop_coordinates()
        case 'Mesprit':
            mesprit_shiny_hunt()
        case 'Cresellia':
            cresselia_shiny_hunt()
        case _:
            static_shiny_hunt()
    
    # Once the shiny hunt exits, prints the reason for exiting
    if pokemon_name == 'SETUP':
        print(f'{config.MESSAGE_SPACING_SYMBOLS}\nExiting setup! Remember to set a pokemon to hunt in the config value [POKEMON_NAME] :) Happy shiny hunting!\n{config.MESSAGE_SPACING_SYMBOLS}')
    else:
        print(f'{config.MESSAGE_SPACING_SYMBOLS}\n{exit_message}\nShutting down app\n{config.MESSAGE_SPACING_SYMBOLS}')