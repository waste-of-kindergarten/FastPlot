import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import Pmw

from tkinter import *
class PlotBoard:
    def __init__(self,root):
        # 画板
        self.board = Figure(figsize=(5,4),dpi=80,edgecolor='silver',frameon=True)
        # 工具栏
        self.canvas = FigureCanvasTkAgg(self.board,root)
        self.toolbar = NavigationToolbar2Tk(self.canvas,root)
        self.toolbar.update()
        # 附加工具栏
        self.addition_toolbar = LabelFrame(root,relief="flat")
        self.photo_refresh = PhotoImage(file="refresh.png").subsample(6,6)
        self.photo_upload = PhotoImage(file="upload.png").subsample(6,6)
        self.photo_clear = PhotoImage(file="clear.png").subsample(6,6)
        self.button_refresh = Button(self.addition_toolbar,command=self.refresh)
        self.button_upload = Button(self.addition_toolbar)
        self.button_clear = Button(self.addition_toolbar,command=self.clear)
        self.button_refresh['image'] = self.photo_refresh
        self.button_upload['image'] = self.photo_upload
        self.button_clear['image'] = self.photo_clear
        self.button_refresh.grid(row=0,column=0)
        self.button_upload.grid(row=0,column=1)
        self.button_clear.grid(row=0,column=2)
        self.ppm1_tips = Pmw.Balloon(root)
        self.ppm2_tips = Pmw.Balloon(root)
        self.ppm3_tips = Pmw.Balloon(root)
        self.ppm1_tips.bind(self.button_refresh,"刷新")
        self.ppm2_tips.bind(self.button_upload,"上传到云")
        self.ppm3_tips.bind(self.button_clear,"清空画板")
        
        
        
    def initial(self,k):
        pass
    def refresh(self):
        pass
    def clear(self):
        pass
    def plot(self,**k):
        pass

        