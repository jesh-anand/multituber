from tkinter import *
from logger import DEBUG
from logger import ERROR

"""ui.py: This script is the GUI interface for Multituber """


class Gui:
    link = []

    def __init__(self):
        self.root = Tk()
        self.root.title('Multituber')
        self.text_widget1 = Text(self.root, height=20, width=50)
        icon = PhotoImage(file="resources/images/download-icon.png")
        button_1 = Button(self.root, text='Download', command=lambda: self.insertlink(self.text_widget1), width=100,
                          image=icon, compound="left")
        self.text_widget1.grid(row=0)
        button_1.grid(row=1, column=1)
        self.root.mainloop()

    def insertlink(self, widget):
        text = widget.get("1.0", END)

        if len(text) < 1:
            ERROR('No link entries found! Exiting..')
            return

        self.link = str(text).strip().split('\n')
        self.closewindow()

    def getlinks(self):
        return self.link

    def closewindow(self):
        self.root.destroy()

# -- Unit Testing
if __name__ == "__main__":
    ui = Gui()
    ui.getlinks()
