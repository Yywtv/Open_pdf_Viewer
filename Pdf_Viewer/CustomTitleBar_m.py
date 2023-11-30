from tkinter import *
from ctypes import windll


class CustomTitleBar(Frame):
    def __init__(self, parent, title, bg, hover_btn_bg, parent_bg):
        super().__init__(master = parent, bg = bg, relief='raised', bd=0, highlightthickness=0)
        self.parent = parent
        self.title = title
        self.bg = bg        
        self.hover_btn_bg = hover_btn_bg
        self.parent_bg = parent_bg
        parent.overrideredirect(True)
        parent.minimized = False 
        parent.maximized = False
        
        self.close_button = Button(self, text='  ×  ', command=self.parent.destroy,bg=self.bg,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
        self.expand_button = Button(self, text=' 🗖 ', command=self.maximize_me,bg=self.bg,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
        self.minimize_button = Button(self, text=' 🗕 ',command=self.minimize_me,bg=self.bg,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
        self.title_bar_title = Label(self, text=self.title, bg=self.bg,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

        self.pack(fill=X)
        self.close_button.pack(side=RIGHT,ipadx=7,ipady=1)
        self.expand_button.pack(side=RIGHT,ipadx=7,ipady=1)
        self.minimize_button.pack(side=RIGHT,ipadx=7,ipady=1)
        self.title_bar_title.pack(side=LEFT, padx=10)

        self.bind('<Button-1>', self.get_pos)
        self.title_bar_title.bind('<Button-1>', self.get_pos)

        self.close_button.bind('<Enter>',self.changex_on_hovering)
        self.close_button.bind('<Leave>',self.returnx_to_normalstate)
        self.expand_button.bind('<Enter>', self.change_size_on_hovering)
        self.expand_button.bind('<Leave>', self.return_size_on_hovering)
        self.minimize_button.bind('<Enter>', self.changem_size_on_hovering)
        self.minimize_button.bind('<Leave>', self.returnm_size_on_hovering)

        self.resizex_widget = Frame(self.parent,bg = self.parent_bg, cursor='sb_h_double_arrow')
        self.resizex_widget.pack(side=RIGHT,ipadx=2,fill=Y)

        self.resizex_widget.bind("<B1-Motion>",self.resizex)
        
        self.resizey_widget = Frame(self.parent,bg = self.parent_bg, cursor='sb_v_double_arrow')
        self.resizey_widget.pack(side=BOTTOM,ipadx=2,fill=X)

        self.resizey_widget.bind("<B1-Motion>",self.resizey)

        self.parent.bind("<FocusIn>",self.deminimize)
        self.parent.after(10, lambda: self.set_appwindow(self.parent))

    def set_appwindow(self,mainWindow):

        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080
        
        hwnd = windll.user32.GetParent(mainWindow.winfo_id())
        stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        stylew = stylew & ~WS_EX_TOOLWINDOW
        stylew = stylew | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    
        mainWindow.wm_withdraw()
        mainWindow.after(10, lambda: mainWindow.wm_deiconify())
    
    def minimize_me(self):
        self.parent.attributes("-alpha",0)
        self.parent.minimized = True       


    def deminimize(self,event):

        self.parent.focus() 
        self.parent.attributes("-alpha",1)
        if self.parent.minimized == True:
            self.parent.minimized = False                              
            

    def maximize_me(self):

        if self.parent.maximized == False:
            self.parent.normal_size = self.parent.geometry()
            self.expand_button.config(text=" 🗗 ")
            self.parent.geometry(f"{self.parent.winfo_screenwidth()}x{self.parent.winfo_screenheight()}+0+0")
            self.parent.maximized = not self.parent.maximized 
            
            
        else: 
            self.expand_button.config(text=" 🗖 ")
            self.parent.geometry(self.parent.normal_size)
            self.parent.maximized = not self.parent.maximized
           
    
    def changex_on_hovering(self,event):
        global close_button
        self.close_button['bg']='red'
        
        
    def returnx_to_normalstate(self,event):
        global close_button
        self.close_button['bg']=self.bg
        

    def change_size_on_hovering(self,event):
        global expand_button
        self.expand_button['bg']=self.hover_btn_bg
        
    def return_size_on_hovering(self,event):
        global expand_button
        self.expand_button['bg']=self.bg
        

    def changem_size_on_hovering(self,event):
        global minimize_button
        self.minimize_button['bg']=self.hover_btn_bg
        
        
    def returnm_size_on_hovering(self,event):
        global minimize_button
        self.minimize_button['bg']=self.bg
    
    def get_pos(self,event):
        if self.parent.maximized == False:
    
            xwin = self.parent.winfo_x()
            ywin = self.parent.winfo_y()
            startx = event.x_root
            starty = event.y_root

            ywin = ywin - starty
            xwin = xwin - startx

            
            def move_window(event):
                self.parent.config(cursor="fleur")
                self.parent.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')


            def release_window(event):
                self.parent.config(cursor="arrow")
                
                
            self.bind('<B1-Motion>', move_window)
            self.bind('<ButtonRelease-1>', release_window)
            self.title_bar_title.bind('<B1-Motion>', move_window)
            self.title_bar_title.bind('<ButtonRelease-1>', release_window)
        else:
            self.expand_button.config(text=" 🗖 ")
            self.parent.maximized = not self.parent.maximized

    def resizex(self,event):
        xwin = self.parent.winfo_x()
        difference = (event.x_root - xwin) - self.parent.winfo_width()
        
        if self.parent.winfo_width() > 150 :
            try:
                self.parent.geometry(f"{ self.parent.winfo_width() + difference }x{ self.parent.winfo_height() }")
            except:
                pass
        else:
            if difference > 0:
                try:
                    self.parent.geometry(f"{ self.parent.winfo_width() + difference }x{ self.parent.winfo_height() }")
                except:
                    pass
                
        self.resizex_widget.config(bg=self.parent_bg)
    
    def resizey(self,event):
        ywin = self.parent.winfo_y()
        difference = (event.y_root - ywin) - self.parent.winfo_height()

        if self.parent.winfo_height() > 150:
            try:
                self.parent.geometry(f"{ self.parent.winfo_width()  }x{ self.parent.winfo_height() + difference}")
            except:
                pass
        else:
            if difference > 0:
                try:
                    self.parent.geometry(f"{ self.parent.winfo_width()  }x{ self.parent.winfo_height() + difference}")
                except:
                    pass

        self.resizex_widget.config(bg=self.parent_bg)
