"""
Python automation script to disable my main monitor, so it can be used to play xbox

Steps:
1. Open Display Settings
2. Select the first monitor
3. Open dropdown menu with options
4. Extend desktop to the display
5. Click accept changes
"""

import pyautogui, time, logging


def main():
    """
    This programm assumes that the second screen is set as the main display, and only monitors 2 and 3 are enabled.
    These coordiantes are relative to the second monitor being the main monitor, where (0,0)
    is the top left corner of the second monitor. In the other program, the first monitor starts
    as the main monitor, so (0,0) is the top left corner of the first monitor, and the coordinates will
    be different.
    """
    button_coordinates = {
        'first_screen':{
            'first_screen_symbol':(1345, 269),
            'extend_desktop_symbol':(-776, 292),
            'make_main_display_symbol':(999, 583),
            'disconnect_this_display_symbol':(-788, 330)
        },
        'second_screen':{
            'first_screen_symbol':(1404,285),
            'extend_desktop_symbol':(1486, 423),
            'make_main_display_symbol':(681,585),
            'disconnect_this_display_symbol':(1492, 460),
            'keep_changes':(877, 591)
        },
        'third_screen':{
            'first_screen_symbol':(-851, 287),
            'extend_desktop_symbol':(-788, 419),
            'make_main_display_symbol':(-1877,1864),
            'disconnect_this_display_symbol':(-788, 455),
            'keep_changes':(-1723, 1689)
        }
    }

    # Set up logging
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

    # minimize all windows to ensure nothing overlaps with the display settings
    logging.debug('Minimizing all windows')
    pyautogui.hotkey('win', 'm')

    # open display settings
    logging.debug('Opening display settings')
    pyautogui.press('win')
    time.sleep(0.3)
    pyautogui.write('Display Settings')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)

    # maximize display settings to ensure the coordinates are the same every time
    display_settings_window = pyautogui.getActiveWindow()
    display_settings_window.maximize()
    time.sleep(1)

    # determine in which monitor display settings was opened
    logging.debug('Determining in which monitor display settings was opened')
    if display_settings_window.size == (1936, 1096):
        screen = 'second_screen'
    elif display_settings_window.size == (1295, 735):
        screen = 'third_screen'
    else:
        logging.debug(f'Could not determine screen of size: {str(display_settings_window.size)}')
        raise Exception('Could not determine screen')
    logging.debug(f'Display settings opened on {screen}')

    # select the first screen
    logging.debug('Selecting first screen')
    pyautogui.click(button_coordinates[screen]['first_screen_symbol'])
    time.sleep(0.3)

    # click on the options menu and select 'extend desktop to this display'
    logging.debug('Extending desktop to first display')
    pyautogui.click(button_coordinates[screen]['disconnect_this_display_symbol'])
    time.sleep(0.3)
    pyautogui.click(button_coordinates[screen]['extend_desktop_symbol'])
    time.sleep(3)

    # determine in which monitor display settings are after extending to first display
    display_settings_window = pyautogui.getActiveWindow()
    logging.debug('Determining in which monitor display settings was opened')
    if display_settings_window.size == (2576, 1456):
        screen = 'first_screen'
    elif display_settings_window.size == (1936, 1096):
        screen = 'second_screen'
    elif display_settings_window.size == (1295, 735):
        screen = 'third_screen'
    else:
        logging.debug(f'Could not determine screen of size: {str(display_settings_window.size)}')
        raise Exception('Could not determine screen')
    logging.debug(f'Display settings opened on {screen}')

    # click on keep changes
    logging.debug('Clicking on keep changes')
    pyautogui.click(button_coordinates[screen]['keep_changes'])
    time.sleep(0.3)

    # make first monitor the main display
    logging.debug('Making first monitor the main display')
    pyautogui.click(button_coordinates[screen]['make_main_display_symbol'])
    time.sleep(0.3)


if __name__ == '__main__':
    main()