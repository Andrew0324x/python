from PIL import Image       # to store image as file
import pyautogui as pag     # Screenshot
import time                 # Time for delay and filename etc...
import keyboard             # To check pressed keyboard

filepath = 'C:/Users/pqnyy/pythn/Screenshot/images'

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(f"{filepath}/image{curr_time}.png")

while True:
    if keyboard.is_pressed("ctrl + shift"):      # Recognize what button is pressed
        screenshot()
    elif keyboard.is_pressed("esc"):
        break