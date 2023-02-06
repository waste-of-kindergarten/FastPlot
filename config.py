from tkinter import *
import json
import os
from params import *
class configuration_:
    def __init__(self,root):
        self.root = root
        self.font = 'SimHei'
        self.fontsize = 12
        self.boardground = 'gray'
        self.plotground = 'silver'
        self.loadconfig()
        
    def loadconfig(self):
        # 加载配置文件
        if not os.path.exists("setting"):
            self.fixconfig()
        else:
            with open("setting.json",'r') as f:
                conf = json.load(f)
            self.font = conf.get('font',self.font)
            self.fontsize = conf.get('fontsize',self.fontsize)
            self.boardground = conf.get('boardground',self.boardground)
            self.plotground = conf.get('plotground',self.plotground)
                
    def fixconfig(self):
        # 修复配置文件
        conf = {'font':self.font,
                'fontsize':self.fontsize,
                'boardground':self.boardground,
                'plotground':self.plotground}
        with open("setting.json",'w') as f:
            json.dump(conf,f)
    
    def cancel(self):
        self.root.attributes('-disabled',0)
        #print("config exit")
        self.top.destroy()
        
        
    def set(self,keyword):
        self.root.attributes('-disabled',1)
        if keyword == "font":
            self.top = Toplevel(self.root)
            self.top.geometry('420x100')
            self.top.resizable(False,False)
            self.top.title('字体')
            self.top.protocol("WM_DELETE_WINDOW",self.cancel)
            
            
            label = Label(self.top,text='设置字体(建议SimHei)')
            self.var = StringVar()
            combobox = ttk.Combobox(self.top,values=ParamSource().get_fonts(),textvariable=self.var)
            apply_button = Button(self.top,text='    应用    ',command=lambda : self.modify("font"))
            apply_store_button = Button(self.top,text='保存并应用',command=lambda: self.store("font"))
            cancel_button = Button(self.top,text='    取消    ',command=self.cancel)
            
            label.grid(row=0,column=0,columnspan=1,padx=10,pady=5)
            combobox.grid(row=0,column=2,columnspan=1,padx=5,pady=5)
            apply_button.grid(row=2,column=0,columnspan=1,padx=20,pady=5)
            apply_store_button.grid(row=2,column=1,columnspan=1,padx=10,pady=5)
            cancel_button.grid(row=2,column=2,columnspan=1,padx=10,pady=5)
            self.top.mainloop()
            
        elif keyword == "fontsize":
            self.top = Toplevel(self.root)
            self.top.geometry('420x100')
            self.top.resizable(False,False)
            self.top.title('字号')
            self.top.protocol("WM_DELETE_WINDOW",self.cancel)
            
            label = Label(self.top,text='设置字号(建议8-16)')
            self.var = IntVar()
            combobox = ttk.Combobox(self.top,values=list(range(0,20)),textvariable=self.var)
            apply_button = Button(self.top,text='    应用    ',command=lambda : self.modify("fontsize"))
            apply_store_button = Button(self.top,text='保存并应用',command=lambda: self.store("fontsize"))
            cancel_button = Button(self.top,text='    取消    ',command=self.cancel)
            
            label.grid(row=0,column=0,columnspan=1,padx=20,pady=5)
            combobox.grid(row=0,column=1,columnspan=2,padx=10,pady=5)
            apply_button.grid(row=2,column=0,columnspan=1,padx=10,pady=5)
            apply_store_button.grid(row=2,column=1,columnspan=1,padx=10,pady=5)
            cancel_button.grid(row=2,column=2,columnspan=1,padx=10,pady=5)
        elif keyword == "boardground":
            self.top = Toplevel(self.root)
            self.top.geometry('420x100')
            self.top.resizable(False,False)
            self.top.title('画板背景')
            self.top.protocol("WM_DELETE_WINDOW",self.cancel)
            
            label = Label(self.top,text='画板背景(建议gray)')
            self.var = StringVar()
            combobox = ttk.Combobox(self.top,values=ParamSource().get_colors(),textvariable=self.var)
            apply_button = Button(self.top,text='应用',command=lambda : self.modify("boardground"))
            apply_store_button = Button(self.top,text='保存并应用',command=lambda: self.store("boardground"))
            cancel_button = Button(self.top,text='取消',command=self.cancel)
            
            label.grid(row=0,column=0,columnspan=1,padx=10,pady=5)
            combobox.grid(row=0,column=2,columnspan=1,padx=5,pady=5)
            apply_button.grid(row=2,column=0,columnspan=1,padx=20,pady=5)
            apply_store_button.grid(row=2,column=1,columnspan=1,padx=10,pady=5)
            cancel_button.grid(row=2,column=2,columnspan=1,padx=10,pady=5)
            self.top.mainloop()
        elif keyword == "plotground":
            self.top = Toplevel(self.root)
            self.top.geometry('420x100')
            self.top.resizable(False,False)
            self.top.title('绘图背景')
            self.top.protocol("WM_DELETE_WINDOW",self.cancel)
            
            label = Label(self.top,text='绘图背景(建议silver)')
            self.var = StringVar()
            combobox = ttk.Combobox(self.top,values=ParamSource().get_colors(),textvariable=self.var)
            apply_button = Button(self.top,text='    应用    ',command=lambda : self.modify("plotground"))
            apply_store_button = Button(self.top,text='保存并应用',command=lambda: self.store("plotground"))
            cancel_button = Button(self.top,text='    取消    ',command=self.cancel)
            
            label.grid(row=0,column=0,columnspan=1,padx=10,pady=5)
            combobox.grid(row=0,column=2,columnspan=1,padx=5,pady=5)
            apply_button.grid(row=2,column=0,columnspan=1,padx=20,pady=5)
            apply_store_button.grid(row=2,column=1,columnspan=1,padx=10,pady=5)
            cancel_button.grid(row=2,column=2,columnspan=1,padx=10,pady=5)
            self.top.mainloop()
        
    def modify(self,keyword):
        self.cancel()
        if keyword == "font":
            self.font = self.var.get()
        elif keyword == "fontsize":
            self.fontsize = self.var.get()
        elif keyword == "boardground":
            self.boardground = self.var.get()
        elif keyword == "plotground":
            self.plotground = self.var.get()
        
    def store(self,keyword):
        self.cancel()
        self.modify(keyword)
        conf = {'font':self.font,
                'fontsize':self.fontsize,
                'boardground':self.boardground,
                'plotground':self.plotground}
        with open("setting.json",'w') as f:
            json.dump(conf,f)
    