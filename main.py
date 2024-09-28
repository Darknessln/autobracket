import pyautogui
import keyboard
import tkinter as tk
import os
import shutil
from time import sleep


terminate = False
window = tk.Tk()
appdata = f"{os.getenv('LOCALAPPDATA')}\\autobracket_data\\"

try:
    op = open(fr"{appdata}operation.txt", 'r').read()
    print(op)
except:
    shutil.move('autobracket_data', os.getenv('LOCALAPPDATA')+"\\")

def read_operation(op):
    if op == '1':
        return True
    else:
        return False

delay = 0.5
operation = read_operation(op)
print(operation)
def autobracket():
    global operation
    global terminate

    while operation:
        pyautogui.PAUSE = 0.001
        if keyboard.is_pressed('('):
            pyautogui.typewrite(')')
            if keyboard.is_pressed('shift'):
                pyautogui.keyUp('shift')
                pyautogui.press('left')
            else:
                pyautogui.press('left')
            sleep(delay)

        elif keyboard.is_pressed('['):
            pyautogui.typewrite(']')
            if keyboard.is_pressed('shift'):
                pyautogui.keyUp('shift')
                pyautogui.press('left')
            else:
                pyautogui.press('left')
            sleep(delay)

        elif keyboard.is_pressed('{'):
            pyautogui.typewrite('}')
            if keyboard.is_pressed('shift'):
                pyautogui.keyUp('shift')
                pyautogui.press('left')
            else:
                pyautogui.press('left')
            sleep(delay)

        elif keyboard.is_pressed('"'):
            if keyboard.is_pressed('shift'):
                pyautogui.typewrite('"')
                pyautogui.keyUp('shift')
                pyautogui.press('left')
            else:
                pyautogui.typewrite("'")
                pyautogui.press('left')
            sleep(delay)

        if terminate == True:
            break
        window.update()

def switch():
    global operation
    if operation:
        button.config(image=off)
        operation = False
        op = open(fr"{appdata}operation.txt", 'w')
        op.write('0')
        op.close()
        autobracket()
    else:
        button.config(image=on)
        operation = True
        op = open(fr"{appdata}operation.txt", 'w')
        op.write('1')
        op.close()
        autobracket()
    window.update()


def on_closing():
    global terminate
    terminate = True
    window.destroy()


window.geometry("417x273")
window.title("Auto Bracket")
window.resizable(False, False)
window.iconbitmap(fr'{appdata}icon.ico')
window.protocol("WM_DELETE_WINDOW", on_closing)

on = tk.PhotoImage(file=fr"{appdata}On.png")
off = tk.PhotoImage(file=fr"{appdata}Off.png")

if operation:
    button = tk.Button(window, image=on, bd=0, command=switch)
    button.pack()
    autobracket()
else:
    button = tk.Button(window, image=off, bd=0, command=switch)
    button.pack()

window.mainloop()