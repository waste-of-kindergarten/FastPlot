import os
from tkinter import *
from file import *
from config import *
from help import *
from board import *
from panel import *
class MainWindow:
    def __init__(self):
        # 主界面
        self.root = Tk()
        # 标题
        self.root.title("FastPlot")
        # 固定界面
        self.root.resizable(False,False)
        # 界面大小
        self.root.geometry("1200x600")
        # 父子窗口控制
        self.root.protocol("WM_DELETE_WINDOW",lambda : os._exit(0))
        
        # 菜单
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        
        ## 文件, 设置, 帮助
        self.file_menu = Menu(self.menubar)
        self.configuration_menu = Menu(self.menubar)
        self.help_menu = Menu(self.menubar)
        
        self.menubar.add_cascade(label='文件',menu=self.file_menu)
        self.menubar.add_cascade(label='设置',menu=self.configuration_menu)
        self.menubar.add_cascade(label='帮助',menu=self.help_menu)
        
        # 文件类 / 配置类
        self.file = file_()
        self.configuration = configuration_(self.root)
        #help = help_()
        
        ### 文件菜单内部
        self.file_menu.add_command(label="打开数据文件")
        self.file_menu.add_command(label="导入配置")
        self.file_menu.add_command(label="存档为..")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="退出",command=self.file.exit)
        ### 设置菜单内部
        self.configuration1_menu = Menu(self.configuration_menu)
        self.configuration_menu.add_cascade(label="基础配置",menu=self.configuration1_menu)
        self.configuration_menu.add_command(label="使用 latex 渲染")
        self.configuration_menu.add_command(label="仪表盘锁定")
        
        #### 基础配置
        self.configuration1_menu.add_command(label="字体",command = lambda : self.configuration.set('font'))
        self.configuration1_menu.add_command(label="字号",command = lambda : self.configuration.set('fontsize'))
        self.configuration1_menu.add_command(label="画板背景",command = lambda : self.configuration.set('boardground'))
        self.configuration1_menu.add_command(label="绘图背景",command = lambda : self.configuration.set('plotground'))
        
        ### 帮助
        self.help_menu.add_command(label="使用说明",command=help_().introduction)
        self.help_menu.add_command(label="关于软件",command=help_().software)
        self.help_menu.add_command(label="版本信息",command=help_().version)
        self.help_menu.add_command(label="作者",command=help_().author)
        self.help_menu.add_command(label="捐助",command=lambda : help_().donate(self.root))
        
        # 界面
        self.canvas_root = Canvas(self.root,width=1200,height=600,bd=4)
        self.canvas_root.pack()
        
        ## matplotlib 画板及工具
        self.plotboard = PlotBoard(self.root)
        self.canvas_root.create_window(900,230,width=600,height=400,window=self.plotboard.canvas.get_tk_widget())
        self.canvas_root.create_window(720,16,width=240,height=32,window=self.plotboard.toolbar)
        self.canvas_root.create_window(1020,16,width=360,height=32,window=self.plotboard.addition_toolbar)
        
        ## 状态栏
        self.state = Text(self.root,fg='Magenta')
        self.state.insert(END,"FastPlot 准备就绪啦")
        self.state.config(state='disabled')
        self.canvas_root.create_window(600,590,width=1200,height=20,window=self.state)
        
        ## 选项栏
        function_list = ['折线图','散点图','条形图','柱状图','饼形图','箱线图','极坐标图']
        self.listbox = Listbox(self.root,height=10)
        self.canvas_root.create_window(100,290,width=200,height=580,window=self.listbox)
        for i in function_list:
            self.listbox.insert(END,i)
        self.listbox.select_set(0)
        self.listbox.event_generate("<<ListboxSelect>>")
        self.listbox.bind("<<ListboxSelect>>",self.clickEvent)
        
        ## 数据录入板
        ##...
        self.table = LabelFrame(self.root,relief='groove',text='仪表盘',labelanchor='n')
        self.panel = Panel(self.root,self.table,self.plotboard)
        self.canvas_root.create_window(400,290,width=396,height=580,window=self.table)
        ## 控制台
        self.console = Text(self.root)
        self.console.insert(END,"---FastPlot Console---\n")
        self.console.config(state='disabled')
        self.canvas_root.create_window(900,495,width=600,height=130,window=self.console)
        self.console_entry = Entry(self.root,bd=2)
        self.canvas_root.create_window(880,570,width=560,height=20,window=self.console_entry)
        self.console_button = Button(self.root,text="提交")
        self.canvas_root.create_window(1180,570,width=40,height=20,window=self.console_button) 
        
    def clickEvent(self,event):
        # 选项栏信号
        if self.listbox.curselection() in [(i,) for i in range(7)]:
            self.panel.state = self.listbox.get(self.listbox.curselection())
            self.panel.flushtable(self.listbox.get(self.listbox.curselection()))
            
    def mainloop(self):
        self.root.mainloop()
        