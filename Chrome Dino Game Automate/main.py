import pyautogui
from PIL import Image,ImageGrab
from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)

def takeScreenshot():
    image = ImageGrab.grab()
    image.show()
    return image

if __name__ == "__main__":
    time.sleep(3)
    image = takeScreenshot()
    data = image.load()
    print(asarray(image))
    for i in range(34,45):
        for j in range(45,67):
            data

