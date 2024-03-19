import tkinter
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
def ty():
    extra_win = tk.Toplevel()
    extra_win.title('order page')
    extra_win.geometry("300x300")
    extra_win.resizable(False,False)

    Label(extra_win, text = "Thankyou for ordering", font = ('Georgia', 15)).place(x = 55, y = 150)

def bf():
    window = tk.Toplevel()
    window.title('Our menu')
    window.geometry("400x400")
    window.resizable(False,False)
     
    Label(window, text = 'items', font = ('Georgia',20,"bold")).place(x = 150, y = 50)
    
    Button(window, text = 'bread-Egg-Fruit juice', font = ('Georgia',10),command=ty).place(x = 50, y = 100)
    
    Button(window, text = 'Dosa/Idli', font = ('Georgia',10),command=ty).place(x = 50, y = 150)

    Button(window, text = 'Poha/Upma', font = ('Georgia',10),command=ty).place(x = 50, y = 200)
def lun():
    window = tk.Toplevel()
    window.title('Our menu')
    window.geometry("400x400")
    window.resizable(False,False)
     
    Label(window, text = 'items', font = ('Georgia',20,"bold")).place(x = 150, y = 50)
    
    Button(window, text = 'NorthIndian-Thali', font = ('Georgia',10),command=ty).place(x = 50, y = 100)
    
    Button(window, text = 'SouthIndian-Thali', font = ('Georgia',10),command=ty).place(x = 50, y = 150)

    Button(window, text = 'EastIndian-Thali', font = ('Georgia',10),command=ty).place(x = 50, y = 200)
def din():
    window = tk.Toplevel()
    window.title('Our menu')
    window.geometry("400x400")
    window.resizable(False,False)
     
    Label(window, text = 'items', font = ('Georgia',20,"bold")).place(x = 150, y = 50)
    
    Button(window, text = 'Italian/Chinese', font = ('Georgia',10),command=ty).place(x = 50, y = 100)
    
    Button(window, text = 'Indian Cuisine', font = ('Georgia',10),command=ty).place(x = 50, y = 150)

    Button(window, text = 'Korean/Japanese', font = ('Georgia',10),command=ty).place(x = 50, y = 200)
    
def create_window():
    window = tk.Toplevel()
    window.title('Our menu')
    window.geometry("400x400")
    window.resizable(False,False)
     
    Label(window, text = 'Dishes', font = ('Georgia',20,"bold")).place(x = 150, y = 50)
    
    Button(window, text = 'Breakfast', font = ('Georgia',10),command=bf).place(x = 160, y = 100)
    
    Button(window, text = 'Lunch', font = ('Georgia',10),command=lun).place(x = 160, y = 150)

    Button(window, text = 'Dinner', font = ('Georgia',10),command=din).place(x = 160, y = 200)

    Button11 = Button(window, text = "Confirm your order", command = ty)
    Button11.place(x = 150, y = 300)
    
    
    

          
                   
win = tkinter.Tk()
win.title("Hotel Management")
win.config(bg="white")
win.geometry("500x600")
win.resizable(False,False)

image_path = PhotoImage(file=r"C:\Users\dassu\OneDrive\Desktop\workspace\python-tkinter-learning\images\welcome-image.png")
bg_image = Label(win,image = image_path)
bg_image.place(relheight = 1, relwidth = 1)
text_label = tkinter.Label(win, text = 'Welcome to CoastBay Resort', font = ('Georgia',24,"italic"))
text_label.pack()

service_lbl = Label(win, text = "Services available", bg = "white", fg = "black", justify = "left", font = ("Georgia",10))
service_lbl.place(x = 30, y = 100)
cb1 = IntVar()
cb2 = IntVar()
Button1 = Checkbutton(win, text = "Roomservice",variable = cb1, onvalue = 1, offvalue = 0,height = 1)
Button2 = Checkbutton(win, text = "Dine-In",variable = cb2, onvalue = 1, offvalue = 0,height = 1)
Button1.place(x = 200, y = 100)
Button2.place(x = 300, y = 100)
menu_lbl = Label(win, text = "Choose exotic dishes from our curated menu!!!", bg = "white", fg = "black", justify = "left", font = ("Georgia",16))
menu_lbl.place(x = 30, y = 200)
Button3 = Button(win, text = "Click here", command = create_window)
Button3.place(x = 200, y = 250)

win.mainloop()
