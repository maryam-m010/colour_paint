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
        self.pen_sizeframe = LabelFrame(self.r, text = "size", bd = 5, bg = "white", font = ("times new roman", "15"))
        self.pen_sizeframe.place(x = 0, y = 310, height = 200, width = 80)
        self.penscale = Scale(self.pen_sizeframe, orient = VERTICAL, from_ = 50, to = 0, len = 170)
        self.penscale.set(1)
        self.penscale.grid(row = 0, column = 1, padx = 10)
        row = column = 0
        for i in colours:
            Button(self.colorframe, bg = i, bd = 2, width = 3, command = lambda col = i: self.select_colour(col)).grid(row = row, column = column)
            row += 1
            if row == 6:
                column = 1
                row = 0
        self.canvas = Canvas(self.r,bg = "white", bd = 5, height = 500, width = 500)
        self.canvas.place(x = 90, y = 0)
        self.canvas.bind("<B1-Motion>", self.draw)

    def select_colour(self, clr):
        self.r.pencolour = clr

    def draw(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill = self.r.pencolour, outline = self.r.pencolour, width = self.penscale.get())


if __name__=="__main__":
    root = Tk()
    a = Paint(root)
    root.mainloop()
