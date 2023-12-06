from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("500x500")
window.title("Python Project GUI program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="#88f7a6")


window.mainloop() #place window on computer screen, listen for events