# eight_ball.py
# a GUI version of the Magic 8 Ball Toy

from tkinter import *
from random import *

answers = ["It is certain.", "It is decidedly so.", 
"Without a doubt.", "Yes - definitely!",
"You may rely on it.", "As I see it, yes.",
"Most likely.", "Outlook good.",
"Yes.", "Signs point to yes.",
"Reply hazy, please try again.", "Ask again later.",
"Better not tell you now.", "Cannot predict now.",
"Concentrate and ask again.", "Don't count on it.",
"My reply is no.", "My sources say no.",
"Outlook not so good.", "Very doubtful."]

def submit():
    """Gets the user's question and gives an answer."""
    question = ask_box.get()
    message = "You didn't ask anything."
    if question:
        message = choice(answers)
    display(message)

def display(message):
    """Takes a string and puts it in the answer box."""
    ask_box.delete(0, END)
    txt["state"] = "normal"
    txt.delete(0.0, END)
    txt.insert(0.0, message)
    txt["state"] = "disabled"

# set up the GUI
root = Tk()
app = Frame(root)
app.grid()
root.title("Magic 8 Ball")
root.geometry("280x340")

ask_lbl = Label(app, text = "Please ask a yes or no question.")
ask_lbl.grid(columnspan = 3, pady = 5, padx = 10)

ask_box = Entry(app, width = 30)
ask_box.grid(columnspan = 3, pady = 5, padx = 10)
ask_box.focus_force()

shake = Button(app, text = "Shake the 8 Ball.")
shake["command"] = submit
shake.grid(column = 1, pady = 5)

# create a label with an image.
picture = Label(app)
picture.grid(column = 1)
eight_ball = PhotoImage(file = "8ball.ppm")
picture["image"] = eight_ball

txt = Text(app, width = 30, height = 3, wrap = WORD, state = DISABLED)
txt.grid(columnspan = 3, pady = 5, padx = 5)

# start the loop
root.mainloop()
