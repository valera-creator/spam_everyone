import pyautogui
import time

time.sleep(3)  # время, чтобы перейти в чат
while True:
    pyautogui.typewrite('@everyone')
    pyautogui.press("enter")
