"""
Python automation script to disable my main monitor, so it can be used to play xbox

Steps:
1. Open Display Settings
2. Select the second monitor
3. Make it the main monitor
4. Select the first monitor
5. Disconnect the first monitor
6. Click accept changes
"""

import pyautogui, time, logging


def main():
    """
    This programm assumes that the first screen is set as the main display, and all 3 monitors are enabled.
    These coordiantes are relative to the first monitor being the main monitor, where (0,0)
    is the top left corner of the first monitor. In the other program, the second monitor starts
    as the main monitor, so (0,0) is the top left corner of the second monitor, and the coordinates will
    be different.
    """
    button_coordinates = {
        'first_screen':{
            'second_screen_symbol':(1525, 269),
            'extend_desktop_symbol':(-776, 292),
            'make_main_display_symbol':(999, 583),
            'first_screen_after_change_symbol':(-1203, 104),
            'disconnect_this_display_symbol':(-788, 330)
        },
        'second_screen':{
            'second_screen_symbol':(3766, 434),
            'extend_desktop_symbol':(1460, 460),
            'make_main_display_symbol':(3240, 755),
            'first_screen_after_change_symbol':(1036, 270),
            'disconnect_this_display_symbol':(1450, 497),
            'keep_changes':(885, 594),
            'close_display_settings':(1897, 17)
        },
        'third_screen':{
            'second_screen_symbol':(1175, 1707),
            'extend_desktop_symbol':(-1176, 1732),
            'make_main_display_symbol':(681, 2025),
            'first_screen_after_change_symbol':(-1558, 1543),
            'disconnect_this_display_symbol':(-1175, 1769),
            'keep_changes':(-1371, 411),
            'close_display_settings':(-665, 17)
        }
    }
    
    # setting up logging
    logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s', level=logging.DEBUG)

    # minimize all windows to ensure nothing overlaps with the display settings
    # sometimes if a video player is in full screen, the display settings can open behind it
    # so this is a precaution
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
    logging.debug('Maximizing display settings window')
    display_settings_window = pyautogui.getActiveWindow()
    display_settings_window.maximize()
    time.sleep(1)

    # depending on where it was opened last, display settings can open in any of the 3 monitors
    # so we get the size of the display settings window to determine which monitor it was opened in
    # this only works for me because all 3 of my monitors are different sizes
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
    
    # click on the second screen symbol inside of display settings
    logging.debug('Finding second screen')
    pyautogui.click(button_coordinates[screen]['second_screen_symbol'], interval=0.5)
    time.sleep(0.5)

    # set it as the main display
    logging.debug('Setting second screen as main display')
    pyautogui.click(button_coordinates[screen]['make_main_display_symbol'], interval=0.5)
    time.sleep(2.5)

    # click back on the first screen symbol
    logging.debug('Finding first screen')
    pyautogui.click(button_coordinates[screen]['first_screen_after_change_symbol'], interval=0.5)

    # open the 'extend desktop to this display' menu and disconnect the display
    logging.debug('Disconnecting first screen')
    pyautogui.click(button_coordinates[screen]['extend_desktop_symbol'], interval=0.5)
    pyautogui.click(button_coordinates[screen]['disconnect_this_display_symbol'], interval=0.5)
    
    # wait to make sure the monitor has been disconnected
    time.sleep(2.5)

    # after disconnecting the display, the display settings window can once again be in either of the remaining 2 monitors
    # so we get the size of the display settings window to determine which monitor it was opened in
    # because that will change the coordinates of the 'keep changes' button, then click on the button
    display_settings_window = pyautogui.getActiveWindow()
    if display_settings_window.size == (1936, 1096):
        screen = 'second_screen'
    elif display_settings_window.size == (1295, 735):
        screen = 'third_screen'
    pyautogui.click(button_coordinates[screen]['keep_changes'])


if __name__ == '__main__':
    main()