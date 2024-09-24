import pyautogui
import keyboard
import tkinter as tk
import os
import shutil

window = tk.Tk()
appdata = f"{os.getenv('LOCALAPPDATA')}\\autobracket_data\\"

try:
    op = open(fr"{appdata}operation.txt", 'r').read()
except:
    shutil.move('autobracket_data', os.getenv('LOCALAPPDATA')+"\\")

def read_operation():
    op = open(fr"{appdata}operation.txt", 'r')
    op.read()
    if op == '1':
        op.close()
        return True
    else:
        op.close()
        return False

operation = read_operation()

def autobracket():
    print('yay')

keyboard.add_hotkey('"', autobracket)

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
        # autobracket()
    window.update()


# window.geometry("420x276")
window.geometry("417x273")
window.title("Auto Bracket")
window.resizable(False, False)
window.iconbitmap(fr'{appdata}icon.ico')

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


