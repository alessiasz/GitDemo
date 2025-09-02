import pyautogui
import time

while True:
    position = pyautogui.moveTo(795,744, duration=2)
    pyautogui.click(795,744, button = 'left')
    time.sleep(30)
    pyautogui.click(795,744, button = 'left')
    pyautogui.moveTo(780, 740, duration=4)
    time.sleep(10)