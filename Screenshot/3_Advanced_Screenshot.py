from PIL import Image       # to store image as file
import pyautogui as pag     # Screenshot
import time                 # Time for delay and filename etc...
import keyboard             # To check pressed keyboard
from io import BytesIO
import win32clipboard
from datetime import datetime


filepath = 'C:/Users/pqnyy/pythn/Screenshot/images'


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

while True:
    go_on = True

    if keyboard.is_pressed("ctrl"):
        while True:
            start_time = datetime.now()
            start = pag.position()      
            time.sleep(0.2)
            break

        while True:
            now_time = datetime.now()
            if (now_time - start_time).total_seconds() > 5:
                go_on = False
                break
            if keyboard.is_pressed("ctrl"):
                end = pag.position()
                time.sleep(0.2)
                break

        if go_on:

            # X point
            if start[0] == end[0]:
                go_on = False
                continue
            elif start[0] < end[0]:
                x_point = start[0]
            else:
                x_point = end[0]

            # Y point
            if start[1] == end[1]:
                go_on = False
                continue
            elif start[1] < end[1]:
                y_point = start[1]
            else:
                y_point = end[1]

            # Width / Height
            width = abs(end[0]-start[0])
            height = abs(end[1]-start[1])

            tempimage = f"{filepath}/temp.png"
            pag.screenshot(tempimage, region = (x_point, y_point, width, height))
            image = Image.open(tempimage)

            output = BytesIO()
            image.convert('RGB').save(output, 'BMP')
            data = output.getvalue()[14:]
            output.close()

            send_to_clipboard(win32clipboard.CF_DIB, data)
    elif keyboard.is_pressed("esc"):
        break

    