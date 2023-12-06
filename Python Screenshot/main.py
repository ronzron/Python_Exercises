import pyautogui
import tkinter as tk
from tkinter.filedialog import *

window = tk.Tk()

canvas1 = tk.Canvas(window, width=400, height=400)
canvas1.pack()

def takeScreenshot():
    myscreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path+"_screenshot.png")


myButton = tk.Button(text="Take Screenshot", command=takeScreenshot, font=10)
canvas1.create_window(160, 160, window=myButton)

window.mainloop()