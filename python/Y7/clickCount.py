# clickCount.py
from tkinter import *

def main():
    myGui = Tk()
    clickCount = Frame(myGui)
    clickCount.grid()
    button = MyBtn(text="0")
    button["command"] = button.click
    button.grid()
    myGui.mainloop()


class MyBtn(Button):
    def click(self):
        """Increment count and update label."""
        try:
            self.count += 1
        except AttributeError:
            self.count = 1
        self.configure(text=str(self.count))

if __name__ == "__main__":
    main()
