from tkinter import Tk, StringVar, Label, Entry, Button, GROOVE
import pyshorteners
import tkinter.messagebox as messagebox
import tkinter as tk


def convert():
    s = pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)


def copy_shortened_url():
    # Copy the shortened URL to the clipboard
    root.clipboard_clear()
    root.clipboard_append(shorturl.get())
    messagebox.showinfo("Copy Success", "Shortened URL copied to clipboard!")


root = Tk()
root.title("URL Shortener")
root.geometry("420x350")
root.resizable(False, False)
root.config(background="#F5F5F5")  # Apple-like background color

# Declare variables
url = StringVar()
shorturl = StringVar()

# Design labels
Label(
    root,
    text="URL Shortener",
    bg="#F5F5F5",
    fg="#1E90FF",
    font="Helvetica 22 bold",
    anchor="center",  # Center the text horizontally
).place(x=80, y=10)

Label(
    root,
    text="-----------------------------------------------------------------------------",
    bg="#F5F5F5",
    fg="#1E90FF",
    font="Helvetica 12",
).place(x=15, y=50)

# Accepting URL as a Input
Label(
    root,
    text="Enter URL Here",
    bg="#F5F5F5",
    fg="#1E90FF",
    font="Helvetica 10 bold",
    padx=2,
    pady=2,
).place(x=7, y=100)
Entry(root, textvariable=url, font="Helvetica 12", width=30).place(x=7, y=120)

# Creating button to give a call for convert function
Button(
    root,
    text="Convert",
    bg="#FFD700",
    fg="#000",
    font="Helvetica 12 bold",
    command=convert,
    relief=GROOVE,
).place(x=7, y=180)

# Displaying shortened URL
Label(
    root,
    text="Shortened URL - Copy & Paste in browser",
    bg="#F5F5F5",
    fg="#1E90FF",
    font="Helvetica 10 bold",
    padx=2,
    pady=2,
).place(x=7, y=250)
Entry(root, textvariable=shorturl, width=35, font="Helvetica 12").place(x=7, y=270)

# Copy button
Button(
    root,
    text="Copy",
    bg="#FFD700",
    fg="#000",
    font="Helvetica 12 bold",
    command=copy_shortened_url,
    relief=GROOVE,
).place(x=335, y=268)

# StatusBar - Only for design purposes
statusvar = StringVar()
statusvar.set("")
Label(
    root, textvariable=statusvar, relief=GROOVE, bg="#F5F5F5", fg="#1E90FF", width=60
).place(x=-1, y=328)

root.mainloop()
