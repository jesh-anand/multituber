from tkinter import *

"""This script is the GUI prototype for multituber

"""
# TODO: Change the UI element cordination

def main():
    testUI()


def testUI():
    root = Tk()
    root.title('Youtube Downloader - Prototype')

    # Declare the text widget
    text_widget1 = Text(root, height=20, width=50)

    # Declare the button widget
    button_1 = Button(root, text='Download', command=lambda: gettext(text_widget1), height=1, width=10)

    # Coordinates for widgets
    text_widget1.grid(row=0)
    button_1.grid(row=1, column=1)

    root.mainloop()


def gettext(widget):
    text = widget.get("1.0", END)

    if len(text) == 0:
        print('No links inserted! Exiting..')
        return

    print(text)


if __name__ == '__main__':
    main()
