import tkinter as tk

class View(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.image = tk.PhotoImage(file="resources/images/download-icon.png")
        b = tk.Button(self, text="Download", image=self.image, compound="left")
        b.pack(side="top")

if __name__ == "__main__":
    root = tk.Tk()
    view = View(root)
    view.pack(side="top", fill="both", expand=False)
    root.mainloop()