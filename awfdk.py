import pyautogui
for i in range(10):
    print(pyautogui.PAUSE)
    pyautogui.PAUSE = 0.01
    pyautogui.press('p')

