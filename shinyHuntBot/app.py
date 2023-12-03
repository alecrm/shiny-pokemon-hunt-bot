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
pokemon_name = config.POKEMON_NAME.capitalize()

###################################################################################################
###################################################################################################

# FUNCTIONS
###################################################################################################

def skip_dialogue(num_times: int):
    """
    Skips through dialogue when initiating the static encounter.
    'num_times' should be the number of times you have to press 'A'
    """
    i = 1
    while i <= num_times:
        controls.press_a()
        sleep(0.3)
        i += 1


def load_game():
    """
    Hacky method to maneuver from resetting the game to initiating the static encounter.
    We do a combination of pressing 'A' and waiting some time to get through each screen.
    """
    # Soft reset emulator
    controls.reset()
    sleep(2)

    # Press A to skip intro screen
    controls.press_a()
    sleep(0.5)

    # Press A to move past title screen
    controls.press_a()
    sleep(0.5)

    # Press A to load the game
    controls.press_a()
    sleep(0.25)

def check_for_recap_screen():
    screenshot.take_screenshot()
    if screenshot.check_for_recap_screen():
        controls.press_b()
        sleep(0.5)
        controls.open_menu()
        controls.move_down(4)
        controls.press_a()
        sleep(0.3)
        controls.press_a()
        sleep(0.3)
        controls.press_a()
        sleep(4.2)


def is_in_battle() -> bool:
    """
    Checks a particular pixel location in the battle screenshot to make sure the enemy's health bar is visible
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
    global try_count
    global exit_message

    while True:
        start_time = time()
        # Displays the current attempt number
        print(f'{strftime("%Y-%m-%d %I:%M:%S %p", localtime(time()))} --- Attempt number: {try_count}')

        # Soft resets emulator and initiates the battle
        load_game()
        check_for_recap_screen()

        # Press A to battle Pokemon
        controls.press_a()
        sleep(0.2)

        skip_dialogue(1)
        sleep(2.5)

        # Clears contents of the screenshot folder and takes a screenshot of the battle
        screenshot.clear_screenshots()
        screenshot.take_screenshot()

        # Confirms the emulator successfully got into the battle. Kills the app after 3 consecutive failures
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
        
        elapsed_time = time() - start_time
        print(f'This attempt took: {strftime("%M minutes and %S seconds", localtime(elapsed_time))}\n')


def mesprit_shiny_hunt():
    global try_count
    global exit_message
    

    while True:
        should_restart = False
        start_time = time()
        # Displays the current attempt number
        print(f'{strftime("%Y-%m-%d %I:%M:%S %p", localtime(time()))} --- Attempt number: {try_count}')

        ######################################### STARTING GAME #########################################
        # Soft resets game
        load_game()
        check_for_recap_screen()

        ################################### TRIGGERING MESPRIT HUNT ####################################
        # Skip through Mesprit disappearing
        skip_dialogue(3)
        sleep(0.7)

        # Skip through Rowan appearing
        skip_dialogue(1)
        sleep(0.7)

        # Skip through Rowan's dialogue part 1
        skip_dialogue(8)
        sleep(0.7)

        # Skip through Rowan's dialogue part 2
        skip_dialogue(8)
        sleep(0.85)

        ######################################## Exiting Cave ###########################################
        # Runs right to align with cave entrance
        controls.run_right(1)

        # Runs down to exit cave
        controls.run_down_for(0.75)
        sleep(0.85)

        ####################################### Fly to Jubilife ########################################
        # Opens menu and opens 'Pokemon' screen
        controls.open_menu()
        controls.move_down(1)
        controls.press_a()
        sleep(0.8)

        # Selects flying pokemon and selects 'Fly'
        controls.toggle_fast_forward() # We slow it down so that we're able to easily select a pokemon
        controls.move_down(1)
        controls.press_a()
        controls.move_down(1)
        controls.press_a()
        sleep(1.3)

        # Selects Jubilife city as the destination to fly to
        controls.move_right(2)
        controls.move_up(2)
        controls.toggle_fast_forward() # We speed up now to zoom through the fly cutscene
        sleep(0.5)
        controls.press_a()
        sleep(3.3)

        #################################### Navigate to Route 202 #####################################
        # Moves to the left and then down to get out of Jubilife City
        controls.run_left_for(0.2455)
        controls.run_down_for(1.180825)
        controls.run_right_for(0.2455)
        controls.run_down_for(0.5)

        ####################################### Hunt for Mesprit ########################################
        # Continues to move between Jubilife City & Route 202 until Mesprit arrives
        is_mesprit_here = False # Boolean to track if Mesprit has arrived
        start_hunt_time = time() # Used to track how long we're hunting for Mesprit
        while True:
            attempts = 1
                # Takes a screenshot 3 times when checking if Mesprit is there to try to avoid capturing
                #  the screenshot while the mesprit icon is blinking off
            while attempts <= 3:
                screenshot.clear_screenshots()
                screenshot.take_screenshot()
                # If the mesprit icon is on Route 202 on our map, set is_mesprit_here to true
                if screenshot.get_pixel_color(*config.MESPRIT_MAP_ICON_CHECK_COORDINATES) == config.MESPRIT_MAP_ICON_COLOR_RGB:
                    print(f'Noticed Mesprit on screenshot attempt: {attempts}')
                    is_mesprit_here = True
                    break

                attempts += 1 # Otherwise, increase our attempt count

            # Breaks out of the loop once Mesprit has arrived
            if is_mesprit_here:
                break

            # Restarts the app if we've been trying for more than 20 minutes
            if (time() - start_hunt_time) > config.MESPRIT_HUNT_TIMEOUT:
                should_restart = True
                break

            # If Mesprit is still not here, moves up into Jubilife City and back down into Route 202
            controls.run_up_for(0.5)
            controls.run_down_for(0.5)
        
        # Checks to see if we broke out of the mesprit hunt to restart
        if should_restart:
            print('TOOK TOO LONG TO HUNT MESPRIT. RESTARTING ATTEMPT!!!')
            continue

        ####################################### Apply Max Repel ########################################
        # Opens bag
        controls.open_menu()
        controls.move_down(1)
        controls.press_a()
        sleep(0.7)

        # Applies Max Repel
        controls.press_a()
        controls.press_a()
        controls.press_a()

        # Closes bag
        controls.press_b()
        sleep(0.7)
        controls.press_b()

        ####################################### Trigger battle #########################################
        # Moves into grass
        controls.move_right(1)

        # Continues to move in the grass until we find Mesprit
        start_battle_time = time() # Used to track how long we've been trying to initiate a battle
        while True: 
            screenshot.clear_screenshots()
            screenshot.take_screenshot()

            # If Dia's hat is no longer visible, we recognize we're in battle and wait for the battle to start
            if screenshot.get_pixel_color(*config.HAT_COLOR_CHECK_COORDINATES) not in config.HAT_COLOR_RGB_LIST:
                sleep(2.2)
                break

            # Restarts the app if we've been trying for more than 5 minutes
            if (time() - start_battle_time) > config.BATTLE_START_TIMEOUT:
                should_restart = True
                break

            # If we're still not in the battle, we'll run to the right and run back to the left
            controls.run_right_for(0.1)
            controls.run_left_for(0.1)
            sleep(0.5)

        # Checks to see if we broke out of the mesprit hunt to restart
        if should_restart:
            print('TOOK TOO LONG TO HUNT MESPRIT. RESTARTING ATTEMPT!!!')
            continue
        
        ################################## Check for Shiny Mesprit #####################################
        screenshot.clear_screenshots()
        screenshot.take_screenshot()

        # Checks if the pokemon is shiny
        if is_shiny_check():
            break
        
        elapsed_time = time() - start_time
        print(f'This attempt took: {strftime("%M minutes and %S seconds", localtime(elapsed_time))}\n')


def cresselia_shiny_hunt():
    raise NotImplementedError('Cresselia shiny hunt method has not been implemented yet')



# TODO: Update is_shiny() method so that it compares an partial image of the hunted pokemon against the screenshot
#        - Have a folder structure of pokemon_compare_images/$POKEMON_NAME/image.png

if __name__ == "__main__":
    if pokemon_name not in config.VALID_POKEMON_LIST:
        raise ValueError(f'[{pokemon_name}] is not a valid pokemon to shiny hunt! Please select from the list of available pokemon')
    
    sleep(3) # Gives 3 seconds to make sure the emulator window is active after starting
    # screenshot.clear_screenshots()
    # screenshot.take_screenshot()

    print(f'------------------------------------------------------------------\nStarting hunt for shiny {pokemon_name}!\n------------------------------------------------------------------')
    pyautogui.click(*config.EMULATOR_EMPTY_CLICK_COORDINATES)
    sleep(0.1)

    # SHINY HUNT FUNCTION CALL
    match pokemon_name:
        case 'Mesprit':
            mesprit_shiny_hunt()
        case 'Cresellia':
            cresselia_shiny_hunt()
        case _:
            static_shiny_hunt()

    
    # Once the app exits the while loop, prints the reason for exiting
    print(f'------------------------------------------------------------------\n{exit_message}\nShutting down app\n------------------------------------------------------------------')