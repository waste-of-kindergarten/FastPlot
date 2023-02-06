from tkinter import messagebox
from tkinter import *
from PIL import Image,ImageTk
import os
class help_:
    def __init__(self):
        pass
    def introduction(self):
        messagebox.showinfo("使用说明","有关软件的使用说明请阅读readme.html")
    def software(self):
        messagebox.showinfo("软件信息","FastPlot 为一款简单易用且功能强大的绘图软件工具, 该软件使用python语言,致力于将matplotlib图形化以便快速高效绘图图形")
    def version(self):
        messagebox.showinfo("版本信息","FastPlot v.1.0.0 beta")
    def author(self):
        messagebox.showinfo("作者信息","幼儿园废料")
    def donate(self,root):
        top = Toplevel(root)
        top.geometry('300x360')
        top.resizable(False,False)
        top.title("捐助")
        
        
        img = Image.open("payment.jpg")
        img = img.resize((300,300))
        img = ImageTk.PhotoImage(img)
        label = Label(top,image=img)
        label.grid()
        label = Label(top,text="Thanks♪(･ω･)ﾉ")
        label.grid()
        top.mainloop()
        