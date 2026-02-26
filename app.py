import keyboard
import cv2
import pyautogui
import pydirectinput
import numpy as np
import os
import time
import threading

from helpers import capture_fullscreen, best_screen_match
from PIL import Image

# 
def listen_for_exit():
    keyboard.wait('q')  # blocks until 'q' is pressed
    print("Exiting...")
    os._exit(0)

threading.Thread(target=listen_for_exit, daemon=True).start()

start_key = "f3"
user_input = ""

"""
Terminal navigation for the user to change start key if needed
"""
print("-------------------------------------")
print("F1 25 MAIL CLAIM AUTOMATION")
while True:
    print("-------------------------------------")
    print("1 - Open Start Program Page")
    print(f"2 - Change Start Program Key (current key is {start_key})")
    try:
        user_input = int(input("Type Your input and press enter: ").strip())
        time.sleep(0.5)
    except ValueError:
        print("Please enter an integer.")
    except OSError:
        print("\nPlease enter an integer.")
    else:
        if user_input == 1:
            break
        elif user_input == 2:
            print("Please click your preferred key to start program.")
            new_key = keyboard.read_key()
            start_key = new_key
            print(f"New start key has been set to {start_key}.")
        else:
            print("Please enter a valid integer (1 or 2).")

print(f"Press {start_key} to start the program (press 'q' to exit anytime).")
keyboard.wait(start_key)
while True:

    current_screen = capture_fullscreen()
    current_state_assessed = best_screen_match(current_screen)

    if current_state_assessed == "online-services-error":
        pydirectinput.press("enter")
        time.sleep(20)
    elif current_state_assessed in ["communicating-online-services", "mail-loading-screen1", "mail-loading-screen2"]:
        time.sleep(20)
    elif current_state_assessed in ["mail-screen1", "mail-screen2"]:
        pydirectinput.press("enter")
        time.sleep(5)
    elif current_state_assessed == "mail-rewards-screen":
        pydirectinput.press("enter")
        time.sleep(25)
    """
    time.sleep(2)
    pydirectinput.press("enter")
    time.sleep(1)
    pydirectinput.press("enter")
    print(pyautogui.locateOnScreen("screenshots/sample_rewards.png", confidence=0.9))
    print("Made it here2")
    """
