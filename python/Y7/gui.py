# click_counter.py

from tkinter import *

def click():
    """Function to change the number on the button."""
    btn["text"] = btn["text"] + 1

root = Tk()
root.title("Click Counter")
root.geometry("125x75")

# create a frame
app = Frame(root)
app.grid()

# create a label
lbl = Label(app, text = "Click the button!")
lbl.grid(padx = 5, pady = 5)

# create a button
btn = Button(app, text = 0)
btn.grid(padx = 5, pady = 5)
btn["command"] = click

# start main loop
root.mainloop()
