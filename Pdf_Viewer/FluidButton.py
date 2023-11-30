import tkinter as tk
from PIL import ImageTk, Image

class button(tk.Canvas):
    def __init__ (self, parent, bg, image_1, image_2, command):
        super().__init__(master = parent, width = 30, height = 30, highlightthickness = 0, bg = bg)
        tagname = 'event'
        self.button = self.create_image(15, 15, image = image_1, tag = tagname)
        self.image_1 = image_1
        self.image_2 = image_2

        self.tag_bind(tagname, "<Enter>", lambda event : self.enter())
        self.tag_bind(tagname, "<Leave>", lambda event : self.leave())
        self.tag_bind(self.button, "<Button-1>", command)



    def enter(self):
        self.config(cursor = "hand2")
        self.itemconfig(self.button, image = self.image_2)
        

    def leave(self):
        self.config(cursor="")
        self.itemconfig(self.button, image = self.image_1)

    def Place(self, pos_x, pos_y, anchor):
        self.place(x = pos_x, y = pos_y, anchor = anchor)
        