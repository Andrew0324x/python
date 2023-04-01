from PIL import Image       # to store image as file
import pyautogui as pag     # Screenshot
import time                 # Time for delay and filename etc...

time.sleep(3)               # Delay 3 seconds

filepath = 'C:/Users/pqnyy/pythn/Screenshot/images'

for oi in range(1, 11): 
    curr_time=time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(f"{filepath}/image{curr_time}.png")
    time.sleep(2)





