from tkinter import *
from tkinter.ttk import Labelframe, Scale
from turtle import pensize

class Paint():
    def __init__(self, root):
        self.r = root
        self.r.geometry("600x600")
        self.r.title("colour paint")
        self.r.config(background = "white")
        self.r.pencolour = "black"
        colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black"]
        self.colorframe = LabelFrame(self.r, text="colour", font=("times new roman", "15"), bd=5, bg="white")
        self.colorframe.place(x = 0, y = 0, width = 80, height = 190)

if __name__=="__main__":
    root = Tk()
    a = Paint(root)
    root.mainloop()
