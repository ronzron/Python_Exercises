import pyperclip
import pyshorteners
from tkinter import *

window = Tk()
window.geometry("450x450")
window.title("URL Shortener")
window.config(bg="#549")
url = StringVar()
url_addreress = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_addreress.set(url_short)

def copyurl():
    url_short = url_addreress.get()
    pyperclip.copy(url_short)

Label(window, text="my url shortener", font="roboto").pack(pady=10)
Entry(window, textvariable=url).pack(pady=5)
Button(window, text="genertate shrot url", command=urlshortener).pack(pady=7)
Entry(window, textvariable=url_addreress).pack(pady=5)
Button(window, text="Copy URL", command=copyurl).pack(pady=5)

window.mainloop()
