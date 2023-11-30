import tkinter as tk
from FluidButton import button
import customtkinter as ctk
from PIL import Image,ImageTk

class Menu(ctk.CTkFrame):
    def __init__(self, parent, close_command, browse_command):
        super().__init__(master = parent, fg_color = '#222F44', corner_radius = 0)
        self.parent = parent
        self.close_command = close_command
        self.browse_command = browse_command

        self.img_More = ImageTk.PhotoImage(Image.open('Pdf_Viewer/More_button.png'))
        self.img_More_hover = ImageTk.PhotoImage(Image.open('Pdf_Viewer/More_button_hovered.png'))

        self.img_Open = ImageTk.PhotoImage(Image.open('Pdf_Viewer/Open_button.png'))
        self.img_Open_hover = ImageTk.PhotoImage(Image.open('Pdf_Viewer/open_button_hovered.png'))

        self.img_Close = ImageTk.PhotoImage(Image.open('Pdf_Viewer/Close_button.png'))
        self.img_Close_hover = ImageTk.PhotoImage(Image.open('Pdf_Viewer/Close_button_hovered.png'))


        # font = ctk.CTkFont(family = 'Great Vibes', size = 15, weight = 'bold')

        # self.button_close = ctk.CTkButton(master = parent, text = '',fg_color = '#00FFEF',
        #                                 text_color = '#222F44', hover_color = '#22577A', command = close_command, font = font,
        #                                 corner_radius = 100, width = 30, height = 30)
        # self.button_open = ctk.CTkButton(master = parent, text = '',fg_color = '#00FFEF',
        #                                 text_color = '#222F44', hover_color = '#22577A', command = browse_command, font = font,
        #                                 corner_radius = 100, width = 15, height = 15)

        self.more_button = button(parent, '#222F44', self.img_More, self.img_More_hover, self.toggle)
        self.more_button.Place(0,35,'nw')

        self.close_button = button(self.parent, '#222F44', self.img_Close, self.img_Close_hover, self.close_command)
        self.open_button = button(self.parent, '#222F44',  self.img_Open, self.img_Open_hover, self.browse_command)
        
        self.switch = ctk.IntVar()
        self.switch.set(value = 0)

        self.x = 0

        # button = ctk.CTkButton(self, 
        #                         image= self.img_More, 
        #                         text = '', 
        #                         width = 10, 
        #                         height = 60, 
        #                         corner_radius = 100,
        #                         fg_color = '#00FFEF',
        #                         hover_color = ('#22577A','#22577A'),
        #                         command = self.toggle,
        #                         font = font)
        # button.pack(side = 'left')



        self.pack(fill = 'x')
        
    def toggle(self,event):
        if self.switch.get() == 0:
            self.more_menus()
        else:
            self.switch.set(value= 0)
            self.less_menus()

    def more_menus(self):
        if self.x < 30:
            self.x += 0.7
            self.close_button.Place(self.x, 68, 'ne')
            self.open_button.Place(self.x, 100, 'ne')
            self.after(1,self.more_menus)
        else:
            self.switch.set(value= 1)
        # self.button_close.place(x = 0, y = 68)
        # self.button_open.place(x = 0, y = 100)

    def less_menus(self):
        if self.x > 0:
            self.x -= 0.7
            self.close_button.Place(self.x, 68, 'ne')
            self.open_button.Place(self.x, 100, 'ne')
            self.after(1,self.less_menus)
        else:
            self.switch.set(value= 0)
        #     self.close_button.children.clear()
        #     self.open_button.children.clear()
        #     self.close_button.place_forget()
        #     self.open_button.place_forget()



    def remove_menus(self):
        self.x = 0
        self.switch.set(value= 0)
        self.close_button.place_forget()
        self.open_button.place_forget()

        
    
    def self_destruct(self):
        self.pack_forget()
        self.more_button.place_forget()