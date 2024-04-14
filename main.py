import pyautogui
import time

# при запуске должна быть выбрана английская раскладка
time.sleep(3)  # время, чтобы перейти в чат
while True:
    pyautogui.typewrite('@everyone')
    pyautogui.press("enter")

    # чтобы настроить частоту отправки:
    # pyautogui.press("enter", interval=0.2) interval - частота отправки - здесь каждые 0.2 секунды
