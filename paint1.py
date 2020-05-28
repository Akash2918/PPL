import os
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor


class Paint(object):
    
    DEFAULT_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        
        self.win = tk.Tk()
        self.win.title('Paint Application')
        
        self.WIDTH = self.win.winfo_screenwidth()
        self.HEIGHT = self.win.winfo_screenheight()
        self.line_width = tk.IntVar()

        self.win.geometry("1200x900+300+300")
        self.win.configure(bg = 'black')
        
        #Getting path
        path = os.getcwd()

        #Adding menubar to the widget
        menubar = tk.Menu(self.win, bg = 'white')

        newphoto = tk.PhotoImage(file = path + '/Images/new.png')
        openphoto = tk.PhotoImage(file = path + '/Images/open.png')
        savephoto = tk.PhotoImage(file = path + '/Images/save.png')
        exitphoto = tk.PhotoImage(file = path + '/Images/exit.png')
        helpphoto = tk.PhotoImage(file = path + '/Images/help.png')
        aboutphoto = tk.PhotoImage(file = path + '/Images/about.png')
        
        #Creating file menu

        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label = 'New', command = self.donothing, image = newphoto, compound = tk.RIGHT)
        filemenu.add_command(label = 'Open', command = self.donothing, image = openphoto, compound = tk.RIGHT)
        filemenu.add_command(label = 'Save', command = self.donothing, image = savephoto, compound = tk.RIGHT)
        filemenu.add_separator()
        filemenu.add_command(label = 'Exit', command = self.win.quit, image = exitphoto, compound = tk.RIGHT)
        menubar.add_cascade(label = 'File', menu = filemenu)

        #Creating help menu
        
        helpmenu = tk.Menu(menubar, tearoff = 0)
        helpmenu.add_command(label = 'Help', command = self.donothing, image = helpphoto, compound = tk.RIGHT)
        helpmenu.add_command(label = 'About', command = self.donothing, image = aboutphoto, compound = tk.RIGHT)
        menubar.add_cascade(label = 'Help', menu = helpmenu)

        self.win.config(menu = menubar)
        
        #Adding frames to the main window
        frame1 = ttk.Frame(self.win, width = 90, height = 390, border = 1)
        frame1.grid(column = 0, row = 0, padx = 5, pady = 5)

        frame2 = ttk.Frame(self.win, width = self.WIDTH - 110, height = self.HEIGHT-10, relief = tk.RAISED)
        frame2.grid(column = 1, row = 0, padx = 5, pady = 5)

        self.canvas = tk.Canvas(frame2, width = self.WIDTH - 110, height = self.HEIGHT - 10, bg = '#ffffff', cursor = 'dot')
        self.canvas.grid(row = 0, column = 0)
        
        #Adding buttons in the frame 1
        penphoto = tk.PhotoImage(file = path + '/Images/pen.png')
        pencilphoto = tk.PhotoImage(file = path + '/Images/pencil.png')
        eraserphoto = tk.PhotoImage(file = path + '/Images/eraser.png')
        brushphoto = tk.PhotoImage(file = path + '/Images/brush.png')
        colorphoto = tk.PhotoImage(file = path + '/Images/color.png')

        self.pen_button = ttk.Button(frame1, text = '', command = self.use_pen, image = penphoto)
        self.pen_button.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.brush_button = ttk.Button(frame1, text = '', command = self.use_brush, image = brushphoto)
        self.brush_button.grid(column = 1, row = 0, padx = 5, pady = 5)

        self.pencil_button = ttk.Button(frame1, text = '', command = self.use_pencil, image = pencilphoto)
        self.pencil_button.grid(column = 0, row = 1, padx = 5, pady = 5)

        self.eraser_button = ttk.Button(frame1 , text = '', command = self.use_eraser, image = eraserphoto)
        self.eraser_button.grid(column = 1, row = 1, padx = 5, pady = 5)

        self.color_button = ttk.Button(frame1, text = '', command = self.choose_color, image = colorphoto)
        self.color_button.grid(column = 0, row = 2, padx = 5, pady = 5)
        
        self.label = ttk.Label(frame1, text = 'Select the size :')
        self.label.grid(column = 0, row = 3, padx = 5, pady = 5)

        self.choose_size_button = tk.Scale(frame1, from_ = 1, to = 10, orient = tk.HORIZONTAL)
        self.choose_size_button.grid(column = 0, row = 4, padx = 5, pady = 5)

        self.setup()
        self.win.mainloop()

    def donothing(self):
        print("Menubar created successfully")
    
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)
        #self.line_widht = self.choose_size_button.get()
        #self.line_width = self.line_width * 1.5

    def use_brush(self):
        self.activate_button(self.brush_button)
        #self.line_width = self.choose_size_button.get()
        #self.line_width = self.line_widht * 2

    def use_pencil(self):
        self.activate_button(self.pencil_button)
        #self.line_width = self.choose_size_button.get()

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color = self.color)[1]
    
    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode = True)
        self.eraser_on = True
        
    def activate_button(self, some_button, eraser_mode = False):
        #self.active_button.config(relief = tk.RAISED)
        #some_button.config(relief = tk.SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y,
                    event.x, event.y, width = self.line_width, fill = paint_color,
                    capstyle = tk.ROUND, smooth = tk.TRUE, splinesteps = 36)
            
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()


