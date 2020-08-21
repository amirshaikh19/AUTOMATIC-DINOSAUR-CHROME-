#  CODED BY @AMIRSHAIKH --> @amirshaikh19 (github)

import pyautogui
from PIL import ImageGrab
import time


def hit(key):
    pyautogui.press(key)
    return


def is_collide(data):
    
    for i in range(225, 265):
        for j in range(275, 378):
            if data[i, j] < 100:
                hit('down')
                return

    
    for i in range(225, 270):
        for j in range(380, 455):
            if data[i, j] < 100:
                hit('up')
                return
    return


if __name__ == "__main__":
    print("Automated DINO BY AMIR SHAIKH")
    time.sleep(3)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        is_collide(data)
