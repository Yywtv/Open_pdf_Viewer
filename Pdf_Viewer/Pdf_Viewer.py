# App work perfectly, needs more features, search, zoom, and adjust the layout of the app more 
# dark dnd theme
# update 22/10/23 :
# everything still sucks, especailly since i added the animation. 
# update 30/11/23 :
# been a while, but it looks like i've fixed the fluid button problem, separated the place so that it doesn't get placed upon initialization, meaning i can place
# the button separately and i don't have to create the buttons every time the animtion starts, but just placing it in slightly different places for a very quick amount of time. (i'll be confused reading this in the future :D)
# now just need to make the text actually highlightable

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
from tkinterdnd2 import DND_FILES, TkinterDnD
from Menus import Menu
from CustomTitleBar_m import CustomTitleBar


window = TkinterDnD.Tk()
window.geometry('400x400+800+200')
title_bar = CustomTitleBar(window, "pdf_viewer", '#22577A', '#222F44', '#222F44')
window.configure(bg = '#222F44')

def Close(event):
    v2.destroy()
    v1.img_object_li.clear()
    menu.pack_forget()
    menu.self_destruct()
    menu.remove_menus()
    canvas.pack(pady = 10)
    Browse_button.pack(pady = 5)


opened = False
def on_drop(event):
    global v2, v1, menu,opened
    if opened == False:
        filename = event.data[1:-1]
        menu = Menu(window, Close, Browse)
        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(window, pdf_location = filename, width = 100, height = 90)
        v2.place(relx = 0.5, y = 36, anchor = 'n', relwidth = 0.5425, relheight = 0.99)
        
        canvas.pack_forget()
        canvas_return('Change Your Files Here')
        canvas.pack(pady = 10)
        opened = True
    else:
        Close(None)
        filename = event.data[1:-1]
        menu = Menu(window, Close, Browse)
        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(window, pdf_location = filename, width = 100, height = 90)
        v2.place(relx = 0.5, y = 36, anchor = 'n', relwidth = 0.5425, relheight = 0.99)
        
        canvas.pack_forget()
        canvas.children.clear()
        canvas_return('Change Your Files Here')
        canvas.pack(pady = 10)

canvas = ctk.CTkCanvas(window, width = 200, height = 200, bg = '#222F44', highlightthickness = 0)
canvas.pack(pady = 10)

image_path = 'd:/Python/learnTKinter/dnd_box.png'
image_tk = tk.PhotoImage(file = image_path)

def canvas_return(text):
    canvas.create_image(100, 100, image = image_tk)
    canvas.create_text(100,100, text = text, fill = '#00FFEF', font =ctk.CTkFont(family = 'helvetica', size = 15, weight = 'bold'))
    canvas.create_text(100,150, text = 'or', fill = '#00FFEF', font =ctk.CTkFont(family = 'helvetica', size = 15, weight = 'bold'))

canvas_return('Drop your Files Here')
canvas.drop_target_register(DND_FILES)
canvas.dnd_bind('<<Drop>>', on_drop)

# initialdir = os.getcwd()
def Browse(event):
    global v2,v1, filename, opened
    filename = filedialog.askopenfilename(
    title = 'Select pdf file',
    filetypes = (('PDF file', '.pdf'),
    ('PDF file', '.PDF'),
    ('ALL file', '.txt')))


    if filename != '':
        if opened == False:
            global menu
            menu = Menu(window, Close, Browse)
            v1 = pdf.ShowPdf()
            v2 = v1.pdf_view(window, pdf_location = filename, width = 100, height = 90)
            v2.place(relx = 0.5, y = 36, anchor = 'n', relwidth = 0.5425, relheight = 0.99)
            v1.img_object_li.clear()
            filename = ''
            canvas.pack_forget()
            opened = True
            Browse_button.pack_forget()
        else:
            Close(None)
            menu = Menu(window, Close, Browse)
            v1 = pdf.ShowPdf()
            v2 = v1.pdf_view(window, pdf_location = filename, width = 100, height = 90)
            v2.place(relx = 0.5, y = 36, anchor = 'n', relwidth = 0.5425, relheight = 0.99)
            v1.img_object_li.clear()
            filename = ''
            canvas.pack_forget()
            Browse_button.pack_forget()
    


    

Browse_button = ctk.CTkButton(window, text = 'Browse File', command = lambda: Browse("<Button-1>"), fg_color = '#00FFEF', text_color = '#222F44',
                              hover_color = '#22577A', font = ctk.CTkFont(family = 'Great Vibes', size = 15, weight = 'bold'),
                              width = 200)
Browse_button.pack(pady = 5)

window.bind("<Escape>", Close)


window.mainloop()