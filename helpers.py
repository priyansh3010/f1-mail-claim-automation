import cv2
import glob
import numpy as np
import os
import sys
import pyautogui

from PIL import Image

def capture_fullscreen():
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame


def best_screen_match(current_screen):

    lowest = sys.maxsize
    lowest_name = ""

    for file_name in glob.glob("screenshots/*.png"):
        sample_screen = Image.open(file_name)
        sample_screen = np.array(sample_screen)
        sample_screen = cv2.cvtColor(sample_screen, cv2.COLOR_BGR2GRAY)

        diff = cv2.absdiff(sample_screen, current_screen)
        mean_diff = np.mean(diff)

        if lowest > mean_diff:
            lowest = mean_diff
            lowest_name = file_name.rsplit(".png")[0].split("screenshots\\")[1]
    
    return lowest_name
    
