import tkinter
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
def ty(last):
    extra_win = tk.Toplevel()
    extra_win.title('order page')
    extra_win.geometry("600x300")
    extra_win.resizable(False,False)

    Label(extra_win, text = f"Thankyou for ordering \n {last} \n visit again", font = ('Georgia', 15)).place(x = 200, y = 100)

def aaa(a,b,c,d):
    window = tk.Toplevel()
    window.title('Our menu')
    window.geometry("400x400")
    window.resizable(False,False)
     
    Label(window, text = a, font = ('Georgia',20,"bold")).place(x = 150, y = 50)
    
    Button(window, text = b, font = ('Georgia',10),command=lambda:ty(b)).place(x = 50, y = 100)
    
    Button(window, text = c, font = ('Georgia',10),command=lambda:ty(c)).place(x = 50, y = 150)

    Button(window, text = d, font = ('Georgia',10),command=lambda:ty(d)).place(x = 50, y = 200)

def create_window():
    window = tk.Toplevel()
    window.title('Our menu')
    window.geometry("400x400")
    window.resizable(False,False)
     
    Label(window, text = 'Dishes', font = ('Georgia',20,"bold")).place(x = 150, y = 50)
    
    Button(window, text = 'Breakfast', font = ('Georgia',10),command=lambda:aaa('breakfast-items','bread-egg-Fruitjuice','Dosa/idli','Poha/Upma')).place(x = 160, y = 100)
    
    Button(window, text = 'Lunch', font = ('Georgia',10),command = lambda:aaa('Lunch-items','NorthIndian-Thali','SouthIndian-Thali','EastIndian-Thali')).place(x = 160, y = 150)

    Button(window, text = 'Dinner', font = ('Georgia',10),command = lambda:aaa('Dinner-Items','Italian/Chinese','Indian Cuisine','Korean/Japanese')).place(x = 160, y = 200)

##    Button4 = Button(window, text = "Confirm your order", command = ty)
##    Button4.place(x = 150, y = 300)
    
    
    

          
                   
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
Button3 = Button(win, text = "Click here", command = lambda:create_window())
Button3.place(x = 200, y = 250)

win.mainloop()
