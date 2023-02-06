from tkinter import *
import pandas as pd
import numpy as np
from params import *
from tkintertable import TableCanvas, TableModel
class Panel:
    def __init__(self,root,table,board):
        self.state = None
        self.lock = False
        self.root = root
        self.table = table
        self.board = board
        Label(table,text="欢迎使用FastPlot").pack()
    def flushtable(self,keyword,**k):
        self.root.attributes("-disabled",0)
        # 销毁之前仪表盘上的内容
        if not self.lock:
            for widgets in self.table.winfo_children():
                widgets.destroy()
        if keyword == "折线图":
            self.x_var = StringVar()
            x_label = Label(self.table,text='      自变量      ')
            x_label.grid(row=1,column=0,columnspan=1,padx=20,pady=5)
            x_entry = Entry(self.table,textvariable=self.x_var)
            x_entry.grid(row=1,column=3,columnspan=2,padx=10,pady=5)
            
            self.y_var = StringVar()
            y_label = Label(self.table,text='      因变量      ')
            y_label.grid(row=2,column=0,columnspan=1,padx=20,pady=5)
            y_entry = Entry(self.table,textvariable=self.y_var)
            y_entry.grid(row=2,column=3,columnspan=2,padx=10,pady=5)
            
            File = Button(self.table,text='导入\n文件',command=self.input_data)
            File.grid(row=1,column=5,rowspan=2,padx=10,pady=0)
            
            self.xlabel_var = StringVar()
            xlabel_label = Label(self.table,text='     X轴名称     ')
            xlabel_entry = Entry(self.table,textvariable=self.xlabel_var)
            xlabel_label.grid(row=3,column=0,columnspan=1,padx=20,pady=5)
            xlabel_entry.grid(row=3,column=3,columnspan=2,padx=10,pady=5)
            
            self.ylabel_var = StringVar()
            ylabel_label = Label(self.table,text='     Y轴名称     ')
            ylabel_entry = Entry(self.table,textvariable=self.ylabel_var)
            ylabel_label.grid(row=4,column=0,columnspan=1,padx=20,pady=5)
            ylabel_entry.grid(row=4,column=3,columnspan=2,padx=10,pady=5)
            
            self.datalabel_var = StringVar()
            datalabel_label = Label(self.table,text='  数据标签名称 ')
            datalabel_entry = Entry(self.table,textvariable=self.datalabel_var)
            datalabel_label.grid(row=5,column=0,columnspan=1,padx=20,pady=5)
            datalabel_entry.grid(row=5,column=3,columnspan=2,padx=10,pady=5)
            
            self.title_var = StringVar()
            title_label = Label(self.table,text='       标题        ')
            title_entry = Entry(self.table,textvariable=self.title_var)
            title_label.grid(row=6,column=0,columnspan=1,padx=20,pady=5)
            title_entry.grid(row=6,column=3,columnspan=2,padx=10,pady=5)
            
            self.color_var = StringVar()
            color_label = Label(self.table,text='     画笔色彩    ')
            color_combobox = ttk.Combobox(self.table,values = ParamSource().get_colors(),textvariable=self.color_var)
            color_combobox.current(0)
            color_label.grid(row=7,column=0,columnspan=1,padx=20,pady=5)
            color_combobox.grid(row=7,column=3,columnspan=2,padx=10,pady=5)
            
            self.marker_var = StringVar()
            marker_label = Label(self.table,text='     点迹形状    ')
            marker_combobox = ttk.Combobox(self.table,values=ParamSource().get_markers(),textvariable=self.marker_var)
            marker_combobox.current(0)
            marker_label.grid(row=8,column=0,columnspan=1,padx=20,pady=5)
            marker_combobox.grid(row=8,column=3,columnspan=2,padx=10,pady=5)
            
            self.line_var = StringVar()
            line_label = Label(self.table,text='     线条样式    ')
            line_combobox = ttk.Combobox(self.table,values=ParamSource().get_lines(),textvariable=self.line_var)
            line_combobox.current(0)
            line_label.grid(row=9,column=0,columnspan=1,padx=20,pady=5)
            line_combobox.grid(row=9,column=3,columnspan=2,padx=10,pady=5)
            
            self.markersize_var = IntVar()
            markersize_label = Label(self.table,text='     点迹大小    ')
            markersize_combobox= ttk.Combobox(self.table,values=list(range(0,20)),textvariable=self.markersize_var)
            markersize_combobox.current(0)
            markersize_label.grid(row=10,column=0,columnspan=1,padx=20,pady=5)
            markersize_combobox.grid(row=10,column=3,columnspan=2,padx=10,pady=5)
            
            self.linewidth_var = IntVar()
            linewidth_label = Label(self.table,text='     线条粗细    ')
            linewidth_combobox=ttk.Combobox(self.table,values=list(range(0,10)),textvariable=self.linewidth_var)
            linewidth_combobox.current(0)
            linewidth_label.grid(row=11,column=0,columnspan=1,padx=2,pady=5)
            linewidth_combobox.grid(row=11,column=3,columnspan=2,padx=10,pady=5)
            
            self.grid_var = StringVar()
            grid_label = Label(self.table,text='     网格线样式    ')
            grid_combobox=ttk.Combobox(self.table,values=ParamSource().get_lines(),textvariable=self.grid_var)
            grid_combobox.current(0)
            grid_label.grid(row=12,column=0,columnspan=1,padx=20,pady=5)
            grid_combobox.grid(row=12,column=3,columnspan=2,padx=10,pady=5)
            
            self.gridcolor_var = StringVar()
            gridcolor_label = Label(self.table,text='   网格线颜色   ')
            gridcolor_combobox = ttk.Combobox(self.table,values=ParamSource().get_colors(),textvariable=self.gridcolor_var)
            gridcolor_combobox.current(0)
            gridcolor_label.grid(row=13,column=0,columnspan=1,padx=20,pady=5)
            gridcolor_combobox.grid(row=13,column=3,columnspan=2,padx=10,pady=5)
            
            self.gridlinewidth_var = IntVar()
            gridlinewidth_label = Label(self.table,text='  网格线条粗细  ')
            gridlinewidth_combobox=ttk.Combobox(self.table,values=list(range(0,10)),textvariable=self.gridlinewidth_var)
            gridcolor_combobox.current(0)
            gridlinewidth_label.grid(row=14,column=0,columnspan=1,padx=20,pady=5)
            gridlinewidth_combobox.grid(row=14,column=3,columnspan=2,padx=10,pady=5)
            
            # save_button
            load_button = Button(self.table,text='加 载 数 据')
            load_button.grid(row=15,column=4,columnspan=3,padx=10,pady=30)
            

            
        elif keyword == "散点图":
            self.x_var = StringVar()
            x_label = Label(self.table,text='      自变量      ')
            x_label.grid(row=1,column=0,columnspan=1,padx=20,pady=5)
            x_entry = Entry(self.table,textvariable=self.x_var)
            x_entry.grid(row=1,column=3,columnspan=2,padx=10,pady=5)
            
            self.y_var = StringVar()
            y_label = Label(self.table,text='      因变量      ')
            y_label.grid(row=2,column=0,columnspan=1,padx=20,pady=5)
            y_entry = Entry(self.table,textvariable=self.y_var)
            y_entry.grid(row=2,column=3,columnspan=2,padx=10,pady=5)
            
            File = Button(self.table,text='导入\n文件',command=self.input_data)
            File.grid(row=1,column=5,rowspan=2,padx=10,pady=0)
            
            self.xlabel_var = StringVar()
            xlabel_label = Label(self.table,text='     X轴名称     ')
            xlabel_entry = Entry(self.table,textvariable=self.xlabel_var)
            xlabel_label.grid(row=3,column=0,columnspan=1,padx=20,pady=5)
            xlabel_entry.grid(row=3,column=3,columnspan=2,padx=10,pady=5)
            
            self.ylabel_var = StringVar()
            ylabel_label = Label(self.table,text='     Y轴名称     ')
            ylabel_entry = Entry(self.table,textvariable=self.ylabel_var)
            ylabel_label.grid(row=4,column=0,columnspan=1,padx=20,pady=5)
            ylabel_entry.grid(row=4,column=3,columnspan=2,padx=10,pady=5)
            
            self.datalabel_var = StringVar()
            datalabel_label = Label(self.table,text='  数据标签名称 ')
            datalabel_entry = Entry(self.table,textvariable=self.datalabel_var)
            datalabel_label.grid(row=5,column=0,columnspan=1,padx=20,pady=5)
            datalabel_entry.grid(row=5,column=3,columnspan=2,padx=10,pady=5)
            
            self.title_var = StringVar()
            title_label = Label(self.table,text='       标题        ')
            title_entry = Entry(self.table,textvariable=self.title_var)
            title_label.grid(row=6,column=0,columnspan=1,padx=20,pady=5)
            title_entry.grid(row=6,column=3,columnspan=2,padx=10,pady=5)
            
            self.marker_var = StringVar()
            marker_label = Label(self.table,text='     点迹形状    ')
            marker_combobox = ttk.Combobox(self.table,values=ParamSource().get_markers(),textvariable=self.marker_var)
            marker_combobox.current(0)
            marker_label.grid(row=7,column=0,columnspan=1,padx=20,pady=5)
            marker_combobox.grid(row=7,column=3,columnspan=2,padx=10,pady=5)
            
            self.markersize_var = IntVar()
            markersize_label = Label(self.table,text='     点迹大小    ')
            markersize_combobox= ttk.Combobox(self.table,values=list(range(0,20))+['随机1-5','随机1-10','随机1-20','随机20-50'],textvariable=self.markersize_var)
            markersize_combobox.current(0)
            markersize_label.grid(row=8,column=0,columnspan=1,padx=20,pady=5)
            markersize_combobox.grid(row=8,column=3,columnspan=2,padx=10,pady=5)
            
            self.alpha_var = StringVar()
            alpha_label = Label(self.table,text='      透明度      ')
            alpha_entry = Entry(self.table,textvariable=self.alpha_var)
            alpha_label.grid(row=9,column=0,columnspan=1,padx=20,pady=5)
            alpha_entry.grid(row=9,column=3,columnspan=2,padx=10,pady=5)
            
            self.color_var = StringVar()
            color_label = Label(self.table,text='     色谱    ')
            color_combobox = ttk.Combobox(self.table,values = ParamSource().get_cmaps() + ParamSource().get_colors(),textvariable=self.color_var)
            color_combobox.current(0)
            color_label.grid(row=10,column=0,columnspan=1,padx=20,pady=5)
            color_combobox.grid(row=10,column=3,columnspan=2,padx=10,pady=5)
            
            self.colorpower_var =  StringVar()
            colorpower_label = Label(self.table,text='     着色权重    ')
            colorpower_entry = Entry(self.table,textvariable=self.colorpower_var)
            colorpower_label.grid(row=11,column=0,columnspan=1,padx=20,pady=5)
            colorpower_entry.grid(row=11,column=3,columnspan=2,padx=10,pady=5)
            
            
            self.grid_var = StringVar()
            grid_label = Label(self.table,text='     网格线样式    ')
            grid_combobox=ttk.Combobox(self.table,values=ParamSource().get_lines(),textvariable=self.grid_var)
            grid_combobox.current(0)
            grid_label.grid(row=12,column=0,columnspan=1,padx=20,pady=5)
            grid_combobox.grid(row=12,column=3,columnspan=2,padx=10,pady=5)
            
            self.gridcolor_var = StringVar()
            gridcolor_label = Label(self.table,text='   网格线颜色   ')
            gridcolor_combobox = ttk.Combobox(self.table,values=ParamSource().get_colors(),textvariable=self.gridcolor_var)
            gridcolor_combobox.current(0)
            gridcolor_label.grid(row=13,column=0,columnspan=1,padx=20,pady=5)
            gridcolor_combobox.grid(row=13,column=3,columnspan=2,padx=10,pady=5)
            
            self.gridlinewidth_var = IntVar()
            gridlinewidth_label = Label(self.table,text='  网格线条粗细  ')
            gridlinewidth_combobox=ttk.Combobox(self.table,values=list(range(0,10)),textvariable=self.gridlinewidth_var)
            gridcolor_combobox.current(0)
            gridlinewidth_label.grid(row=14,column=0,columnspan=1,padx=20,pady=5)
            gridlinewidth_combobox.grid(row=14,column=3,columnspan=2,padx=10,pady=5)
            
            # save_button
            load_button = Button(self.table,text='加 载 数 据')
            load_button.grid(row=15,column=4,columnspan=3,padx=10,pady=30)
            
        elif keyword == "条形图":
            self.x_var = StringVar()
            x_label = Label(self.table,text='      自变量      ')
            x_label.grid(row=1,column=0,columnspan=1,padx=20,pady=5)
            x_entry = Entry(self.table,textvariable=self.x_var)
            x_entry.grid(row=1,column=3,columnspan=2,padx=10,pady=5)
            
            self.y_var = StringVar()
            y_label = Label(self.table,text='      因变量      ')
            y_label.grid(row=2,column=0,columnspan=1,padx=20,pady=5)
            y_entry = Entry(self.table,textvariable=self.y_var)
            y_entry.grid(row=2,column=3,columnspan=2,padx=10,pady=5)
            
            File = Button(self.table,text='导入\n文件',command=self.input_data2)
            File.grid(row=1,column=5,rowspan=2,padx=10,pady=0)
            
            self.xlabel_var = StringVar()
            xlabel_label = Label(self.table,text='     X轴名称     ')
            xlabel_entry = Entry(self.table,textvariable=self.xlabel_var)
            xlabel_label.grid(row=3,column=0,columnspan=1,padx=20,pady=5)
            xlabel_entry.grid(row=3,column=3,columnspan=2,padx=10,pady=5)
            
            self.ylabel_var = StringVar()
            ylabel_label = Label(self.table,text='     Y轴名称     ')
            ylabel_entry = Entry(self.table,textvariable=self.ylabel_var)
            ylabel_label.grid(row=4,column=0,columnspan=1,padx=20,pady=5)
            ylabel_entry.grid(row=4,column=3,columnspan=2,padx=10,pady=5)
            
            self.datalabel_var = StringVar()
            datalabel_label = Label(self.table,text='  数据标签名称 ')
            datalabel_entry = Entry(self.table,textvariable=self.datalabel_var)
            datalabel_label.grid(row=5,column=0,columnspan=1,padx=20,pady=5)
            datalabel_entry.grid(row=5,column=3,columnspan=2,padx=10,pady=5)
            
            self.title_var = StringVar()
            title_label = Label(self.table,text='       标题        ')
            title_entry = Entry(self.table,textvariable=self.title_var)
            title_label.grid(row=6,column=0,columnspan=1,padx=20,pady=5)
            title_entry.grid(row=6,column=3,columnspan=2,padx=10,pady=5)
            
            self.color_var = StringVar()
            color_label = Label(self.table,text='     画笔色彩    ')
            color_combobox = ttk.Combobox(self.table,values = ParamSource().get_colors(),textvariable=self.color_var)
            color_combobox.current(0)
            color_label.grid(row=7,column=0,columnspan=1,padx=20,pady=5)
            color_combobox.grid(row=7,column=3,columnspan=2,padx=10,pady=5)
            
            self.edgecolor_var = StringVar()
            edgecolor_label = Label(self.table,text='     边线颜色    ')
            edgecolor_combobox = ttk.Combobox(self.table,values=ParamSource().get_colors(),textvariable=self.edgecolor_var)
            edgecolor_combobox.current(0)
            edgecolor_label.grid(row=8,column=0,columnspan=1,padx=20,pady=5)
            edgecolor_combobox.grid(row=8,column=3,columnspan=2,padx=10,pady=5)
            
            self.edgelinewidth_var = StringVar()
            edgelinewidth_label = Label(self.table,text='     边线宽度    ')
            edgelinewidth_combobox = ttk.Combobox(self.table,values=list(range(0,20)),textvariable=self.edgelinewidth_var)
            edgelinewidth_combobox.current(0)
            edgelinewidth_label.grid(row=9,column=0,columnspan=1,padx=20,pady=5)
            edgelinewidth_combobox.grid(row=9,column=3,columnspan=2,padx=10,pady=5)
            
            self.hatch_var = IntVar()
            hatch_label = Label(self.table,text='       影线       ')
            hatch_combobox= ttk.Combobox(self.table,values=ParamSource().get_hatchs(),textvariable=self.hatch_var)
            hatch_combobox.current(0)
            hatch_label.grid(row=10,column=0,columnspan=1,padx=20,pady=5)
            hatch_combobox.grid(row=10,column=3,columnspan=2,padx=10,pady=5)
            
            self.grid_var = StringVar()
            grid_label = Label(self.table,text='     网格线样式    ')
            grid_combobox=ttk.Combobox(self.table,values=ParamSource().get_lines(),textvariable=self.grid_var)
            grid_combobox.current(0)
            grid_label.grid(row=11,column=0,columnspan=1,padx=20,pady=5)
            grid_combobox.grid(row=11,column=3,columnspan=2,padx=10,pady=5)
            
            self.gridcolor_var = StringVar()
            gridcolor_label = Label(self.table,text='   网格线颜色   ')
            gridcolor_combobox = ttk.Combobox(self.table,values=ParamSource().get_colors(),textvariable=self.gridcolor_var)
            gridcolor_combobox.current(0)
            gridcolor_label.grid(row=12,column=0,columnspan=1,padx=20,pady=5)
            gridcolor_combobox.grid(row=12,column=3,columnspan=2,padx=10,pady=5)
            
            self.gridlinewidth_var = IntVar()
            gridlinewidth_label = Label(self.table,text='  网格线条粗细  ')
            gridlinewidth_combobox=ttk.Combobox(self.table,values=list(range(0,10)),textvariable=self.gridlinewidth_var)
            gridcolor_combobox.current(0)
            gridlinewidth_label.grid(row=13,column=0,columnspan=1,padx=20,pady=5)
            gridlinewidth_combobox.grid(row=13,column=3,columnspan=2,padx=10,pady=5)
            
            # save_button
            load_button = Button(self.table,text='加 载 数 据')
            load_button.grid(row=15,column=4,columnspan=3,padx=10,pady=30)
            
        elif keyword == "柱状图":
            self.x_var = StringVar()
            x_label = Label(self.table,text='      自变量      ')
            x_label.grid(row=1,column=0,columnspan=1,padx=20,pady=5)
            x_entry = Entry(self.table,textvariable=self.x_var)
            x_entry.grid(row=1,column=3,columnspan=2,padx=10,pady=5)
            
            self.y_var = StringVar()
            y_label = Label(self.table,text='      因变量      ')
            y_label.grid(row=2,column=0,columnspan=1,padx=20,pady=5)
            y_entry = Entry(self.table,textvariable=self.y_var)
            y_entry.grid(row=2,column=3,columnspan=2,padx=10,pady=5)
            
            File = Button(self.table,text='导入\n文件',command=self.input_data)
            File.grid(row=1,column=5,rowspan=2,padx=10,pady=0)
            
            self.xlabel_var = StringVar()
            xlabel_label = Label(self.table,text='     X轴名称     ')
            xlabel_entry = Entry(self.table,textvariable=self.xlabel_var)
            xlabel_label.grid(row=3,column=0,columnspan=1,padx=20,pady=5)
            xlabel_entry.grid(row=3,column=3,columnspan=2,padx=10,pady=5)
            
            self.ylabel_var = StringVar()
            ylabel_label = Label(self.table,text='     Y轴名称     ')
            ylabel_entry = Entry(self.table,textvariable=self.ylabel_var)
            ylabel_label.grid(row=4,column=0,columnspan=1,padx=20,pady=5)
            ylabel_entry.grid(row=4,column=3,columnspan=2,padx=10,pady=5)
            
            self.datalabel_var = StringVar()
            datalabel_label = Label(self.table,text='  数据标签名称 ')
            datalabel_entry = Entry(self.table,textvariable=self.datalabel_var)
            datalabel_label.grid(row=5,column=0,columnspan=1,padx=20,pady=5)
            datalabel_entry.grid(row=5,column=3,columnspan=2,padx=10,pady=5)
            
            self.title_var = StringVar()
            title_label = Label(self.table,text='       标题        ')
            title_entry = Entry(self.table,textvariable=self.title_var)
            title_label.grid(row=6,column=0,columnspan=1,padx=20,pady=5)
            title_entry.grid(row=6,column=3,columnspan=2,padx=10,pady=5)
            
            self.color_var = StringVar()
            color_label = Label(self.table,text='     画笔色彩    ')
            color_combobox = ttk.Combobox(self.table,values = ParamSource().get_colors(),textvariable=self.color_var)
            color_combobox.current(0)
            color_label.grid(row=7,column=0,columnspan=1,padx=20,pady=5)
            color_combobox.grid(row=7,column=3,columnspan=2,padx=10,pady=5)
            
            self.edgecolor_var = StringVar()
            edgecolor_label = Label(self.table,text='     边线颜色    ')
            edgecolor_combobox = ttk.Combobox(self.table,values=ParamSource().get_colors(),textvariable=self.edgecolor_var)
            edgecolor_combobox.current(0)
            edgecolor_label.grid(row=8,column=0,columnspan=1,padx=20,pady=5)
            edgecolor_combobox.grid(row=8,column=3,columnspan=2,padx=10,pady=5)
            
            self.edgelinewidth_var = StringVar()
            edgelinewidth_label = Label(self.table,text='     边线宽度    ')
            edgelinewidth_combobox = ttk.Combobox(self.table,values=list(range(0,20)),textvariable=self.edgelinewidth_var)
            edgelinewidth_combobox.current(0)
            edgelinewidth_label.grid(row=9,column=0,columnspan=1,padx=20,pady=5)
            edgelinewidth_combobox.grid(row=9,column=3,columnspan=2,padx=10,pady=5)
            
            self.hatch_var = IntVar()
            hatch_label = Label(self.table,text='       影线       ')
            hatch_combobox= ttk.Combobox(self.table,values=ParamSource().get_hatchs(),textvariable=self.hatch_var)
            hatch_combobox.current(0)
            hatch_label.grid(row=10,column=0,columnspan=1,padx=20,pady=5)
            hatch_combobox.grid(row=10,column=3,columnspan=2,padx=10,pady=5)
            
            self.grid_var = StringVar()
            grid_label = Label(self.table,text='     网格线样式    ')
            grid_combobox=ttk.Combobox(self.table,values=ParamSource().get_lines(),textvariable=self.grid_var)
            grid_combobox.current(0)
            grid_label.grid(row=11,column=0,columnspan=1,padx=20,pady=5)
            grid_combobox.grid(row=11,column=3,columnspan=2,padx=10,pady=5)
            
            self.gridcolor_var = StringVar()
            gridcolor_label = Label(self.table,text='   网格线颜色   ')
            gridcolor_combobox = ttk.Combobox(self.table,values=ParamSource().get_colors(),textvariable=self.gridcolor_var)
            gridcolor_combobox.current(0)
            gridcolor_label.grid(row=12,column=0,columnspan=1,padx=20,pady=5)
            gridcolor_combobox.grid(row=12,column=3,columnspan=2,padx=10,pady=5)
            
            self.gridlinewidth_var = IntVar()
            gridlinewidth_label = Label(self.table,text='  网格线条粗细  ')
            gridlinewidth_combobox=ttk.Combobox(self.table,values=list(range(0,10)),textvariable=self.gridlinewidth_var)
            gridcolor_combobox.current(0)
            gridlinewidth_label.grid(row=13,column=0,columnspan=1,padx=20,pady=5)
            gridlinewidth_combobox.grid(row=13,column=3,columnspan=2,padx=10,pady=5)
            
            # save_button
            load_button = Button(self.table,text='加 载 数 据')
            load_button.grid(row=15,column=4,columnspan=3,padx=10,pady=30)
        elif keyword == "饼形图":
            self.x_var = StringVar()
            x_label = Label(self.table,text='      自变量      ')
            x_label.grid(row=1,column=0,columnspan=1,padx=20,pady=5)
            x_entry = Entry(self.table,textvariable=self.x_var)
            x_entry.grid(row=1,column=3,columnspan=2,padx=10,pady=5)
            
            self.y_var = StringVar()
            y_label = Label(self.table,text='      因变量      ')
            y_label.grid(row=2,column=0,columnspan=1,padx=20,pady=5)
            y_entry = Entry(self.table,textvariable=self.y_var)
            y_entry.grid(row=2,column=3,columnspan=2,padx=10,pady=5)
            
            File = Button(self.table,text='导入\n文件',command=self.input_data)
            File.grid(row=1,column=5,rowspan=2,padx=10,pady=0)
            
            self.autopct_var = StringVar()
            autopct_label = Label(self.table,text='      百分比格式      ')
            autopct_combobox = ttk.Combobox(self.table,values=["%.0f%%","%.1f%%","%.2f%%","%.3ff","%.4f%%"],textvariable=self.autopct_var)
            autopct_combobox.current(0)
            autopct_label.grid(row=3,column=0,columnspan=1,padx=20,pady=5)
            autopct_combobox.grid(row=3,column=3,columnspan=2,padx=10,pady=5)
            
            self.explode_var = StringVar()
            explode_label = Label(self.table,text='  突出显示扇形距离  ')
            explode_entry = Entry(self.table,textvariable=self.explode_var)
            explode_label.grid(row=4,column=0,columnspan=1,padx=20,pady=5)
            explode_entry.grid(row=4,column=3,columnspan=2,padx=10,pady=5)
            
            self.title_var = StringVar()
            title_label = Label(self.table,text='       标题        ')
            title_entry = Entry(self.table,textvariable=self.title_var)
            title_label.grid(row=6,column=0,columnspan=1,padx=20,pady=5)
            title_entry.grid(row=6,column=3,columnspan=2,padx=10,pady=5)
            
            # save_button
            load_button = Button(self.table,text='加 载 数 据')
            load_button.grid(row=15,column=4,columnspan=3,padx=10,pady=30)
            
        elif keyword == "极坐标图":
            self.x_var = StringVar()
            x_label = Label(self.table,text='      自变量      ')
            x_label.grid(row=1,column=0,columnspan=1,padx=20,pady=5)
            x_entry = Entry(self.table,textvariable=self.x_var)
            x_entry.grid(row=1,column=3,columnspan=2,padx=10,pady=5)
            
            self.y_var = StringVar()
            y_label = Label(self.table,text='      因变量      ')
            y_label.grid(row=2,column=0,columnspan=1,padx=20,pady=5)
            y_entry = Entry(self.table,textvariable=self.y_var)
            y_entry.grid(row=2,column=3,columnspan=2,padx=10,pady=5)
            
            File = Button(self.table,text='导入\n文件',command=self.input_data)
            File.grid(row=1,column=5,rowspan=2,padx=10,pady=0)
            
            self.datalabel_var = StringVar()
            datalabel_label = Label(self.table,text='  数据标签名称 ')
            datalabel_entry = Entry(self.table,textvariable=self.datalabel_var)
            datalabel_label.grid(row=3,column=0,columnspan=1,padx=20,pady=5)
            datalabel_entry.grid(row=3,column=3,columnspan=2,padx=10,pady=5)
            
            self.title_var = StringVar()
            title_label = Label(self.table,text='       标题        ')
            title_entry = Entry(self.table,textvariable=self.title_var)
            title_label.grid(row=4,column=0,columnspan=1,padx=20,pady=5)
            title_entry.grid(row=4,column=3,columnspan=2,padx=10,pady=5)
            
            self.color_var = StringVar()
            color_label = Label(self.table,text='     画笔色彩    ')
            color_combobox = ttk.Combobox(self.table,values = ParamSource().get_colors(),textvariable=self.color_var)
            color_combobox.current(0)
            color_label.grid(row=5,column=0,columnspan=1,padx=20,pady=5)
            color_combobox.grid(row=5,column=3,columnspan=2,padx=10,pady=5)
            
            self.marker_var = StringVar()
            marker_label = Label(self.table,text='     点迹形状    ')
            marker_combobox = ttk.Combobox(self.table,values=ParamSource().get_markers(),textvariable=self.marker_var)
            marker_combobox.current(0)
            marker_label.grid(row=6,column=0,columnspan=1,padx=20,pady=5)
            marker_combobox.grid(row=6,column=3,columnspan=2,padx=10,pady=5)
            
            self.line_var = StringVar()
            line_label = Label(self.table,text='     线条样式    ')
            line_combobox = ttk.Combobox(self.table,values=ParamSource().get_lines(),textvariable=self.line_var)
            line_combobox.current(0)
            line_label.grid(row=7,column=0,columnspan=1,padx=20,pady=5)
            line_combobox.grid(row=7,column=3,columnspan=2,padx=10,pady=5)
            
            self.markersize_var = IntVar()
            markersize_label = Label(self.table,text='     点迹大小    ')
            markersize_combobox= ttk.Combobox(self.table,values=list(range(0,20)),textvariable=self.markersize_var)
            markersize_combobox.current(0)
            markersize_label.grid(row=8,column=0,columnspan=1,padx=20,pady=5)
            markersize_combobox.grid(row=8,column=3,columnspan=2,padx=10,pady=5)
            
            self.linewidth_var = IntVar()
            linewidth_label = Label(self.table,text='     线条粗细    ')
            linewidth_combobox=ttk.Combobox(self.table,values=list(range(0,10)),textvariable=self.linewidth_var)
            linewidth_combobox.current(0)
            linewidth_label.grid(row=9,column=0,columnspan=1,padx=2,pady=5)
            linewidth_combobox.grid(row=9,column=3,columnspan=2,padx=10,pady=5)
            
            self.grid_var = StringVar()
            grid_label = Label(self.table,text='     网格线样式    ')
            grid_combobox=ttk.Combobox(self.table,values=ParamSource().get_lines(),textvariable=self.grid_var)
            grid_combobox.current(0)
            grid_label.grid(row=10,column=0,columnspan=1,padx=20,pady=5)
            grid_combobox.grid(row=10,column=3,columnspan=2,padx=10,pady=5)
            
            self.gridcolor_var = StringVar()
            gridcolor_label = Label(self.table,text='   网格线颜色   ')
            gridcolor_combobox = ttk.Combobox(self.table,values=ParamSource().get_colors(),textvariable=self.gridcolor_var)
            gridcolor_combobox.current(0)
            gridcolor_label.grid(row=11,column=0,columnspan=1,padx=20,pady=5)
            gridcolor_combobox.grid(row=11,column=3,columnspan=2,padx=10,pady=5)
            
            self.gridlinewidth_var = IntVar()
            gridlinewidth_label = Label(self.table,text='  网格线条粗细  ')
            gridlinewidth_combobox=ttk.Combobox(self.table,values=list(range(0,10)),textvariable=self.gridlinewidth_var)
            gridcolor_combobox.current(0)
            gridlinewidth_label.grid(row=12,column=0,columnspan=1,padx=20,pady=5)
            gridlinewidth_combobox.grid(row=12,column=3,columnspan=2,padx=10,pady=5)
            
            # save_button
            load_button = Button(self.table,text='加 载 数 据')
            load_button.grid(row=15,column=4,columnspan=3,padx=10,pady=30)
            
    def load(self,**k):
        self.board.plot(**k)
        
    def cancel(self,top):
        self.root.attributes('-disabled',0)
        top.destroy()

        
        
    def input_data2(self):

        choice = filedialog.askopenfilename(filetypes=[('CSV','csv'),('XLSX','xlsx'),('xls','xls')])
        if choice == '':
            return 
        self.root.attributes("-disabled",1)
        self.data = pd.read_excel(choice,sheet_name=None)
        if len(self.data.keys()) > 1:
            self.top = Toplevel(self.root)
            self.top.geometry('360x180')
            self.top.resizable(False,False)
            self.top.title('提示')
            self.top.protocol('WM_DELETE_WINDOW',lambda : self.cancel(self.top))
            
            self.top_canvas = Canvas(self.top,width=360,height=180,bd=4)
            self.top_canvas.pack()
            prompt_label = Label(self.top,text="似乎您的文件有多个sheet,请选择一个")
            self.top_canvas.create_window(180,30,width=360,height=60,window=prompt_label)
            self.prompt_choice_var = StringVar()
            prompt_choice = ttk.Combobox(self.top,values=list(self.data.keys()),textvariable=self.prompt_choice_var)
            prompt_choice.current(0)
            self.top_canvas.create_window(180,90,width=300,height=20,window=prompt_choice)
            
            prompt_button = Button(self.top,text='确认',command=lambda : self.prompt_confirm2(multi=True,choice=prompt_choice.get()))
            self.top_canvas.create_window(180,150,width=300,height=20,window=prompt_button) 
            self.top.mainloop()
        else:
            self.prompt_confirm2(multi=False,choice=list(self.data.keys())[0])
            
    def input_data(self):
        
        choice = filedialog.askopenfilename(filetypes=[('CSV','csv'),('XLSX','xlsx'),('xls','xls')])
        if choice == '':
            return 
        self.root.attributes("-disabled",1)
        self.data = pd.read_excel(choice,sheet_name=None)
        if len(self.data.keys()) > 1:
            
            self.top = Toplevel(self.root)
            self.top.geometry('360x180')
            self.top.resizable(False,False)
            self.top.title('提示')
            self.top.protocol('WM_DELETE_WINDOW',lambda : self.cancel(self.root))
            
            self.top_canvas = Canvas(self.top,width=360,height=180,bd=4)
            self.top_canvas.pack()
            prompt_label = Label(self.top,text="似乎您的文件有多个sheet,请选择一个")
            self.top_canvas.create_window(180,30,width=360,height=60,window=prompt_label)
            self.prompt_choice_var = StringVar()
            prompt_choice = ttk.Combobox(self.top,values=list(self.data.keys()),textvariable=self.prompt_choice_var)
            prompt_choice.current(0)
            self.top_canvas.create_window(180,90,width=300,height=20,window=prompt_choice)
            
            prompt_button = Button(self.top,text='确认',command=lambda : self.prompt_confirm(multi=True,choice=prompt_choice.get()))
            self.top_canvas.create_window(180,150,width=300,height=20,window=prompt_button) 
            
            self.top.mainloop()
        else:
            self.prompt_confirm(multi=False,choice=list(self.data.keys())[0])
    
    def prompt_confirm2(self,multi,choice):
        if multi:
            self.top.destroy()
        self.data = self.data[choice]
        if len(self.data) == 0:
            messagebox.showwarning("警告","这个sheet中没有数据,导入数据失败")
            return
        top1 = Toplevel(self.table)
        top1.geometry('720x720')
        top1.resizable(False,False)
        top1.title("数据导入")
        top1.protocol('WM_DELETE_WINDOW',self.cancel(top1))
        
        top_canvas1 = Canvas(top1,width=720,height=720)
        top_canvas1.pack()
        
        tframe = Frame(top1)
        top_canvas1.create_window(360,150,width=720,height=300,window=tframe)
        
        a,b = self.data.shape
        col = np.array(self.data.columns).tolist()
        data = np.array(self.data).tolist()
        data1 = {'rec%d'%i : {  str(col[j]) : data[i][j] for j in range(b)  } for i in range(a)}
        ttable = TableCanvas(tframe,data=data1,cellbackgr=None,rowselectedcolor=None,read_only=True)
        ttable.show()
        c1_label = Label(top1,text='自变量选择')
        self.c1_var = StringVar()
        c1_combobox = ttk.Combobox(top1,values=col,textvariable=self.c1_var)
        top_canvas1.create_window(120,310,width=240,height=20,window=c1_label)
        top_canvas1.create_window(480,310,width=480,height=20,window=c1_combobox)
        
        c2_label = Label(top1,text='因变量选择')
        self.c2_var = [IntVar() for i in col]
        c2_buttons = []
        group_ = Frame(top1)
        for i in range(len(col)):
            c2_buttons.append(Checkbutton(group_,text=col[i],variable=self.c2_var[i],width=70,indicatoron=True,bd=0))
            
        for i in range(len(col)):
            c2_buttons[i].pack()
        #group_.insert('','end',col[i])
        #vbar = Scrollbar(top1,orient=VERTICAL)
        #vbar.place(x=940,width=20,height=380)
        #vbar.configure(command = group_.yview)
        #top_canvas1.config(yscrollcommand=vbar.set)
        top_canvas1.create_window(120,330,width=240,height=18,window=c2_label)
        top_canvas1.create_window(470,510,width=460,height=380,window=group_)
        #top_canvas1.create_window(710,510,width=20,height=380,window=vbar)
        
        def confirm2():
            self.x_var.set(str(np.array(self.data[self.c1_var.get()]).tolist())[1:-1])
            self.y_var.set(str(np.array(self.data[[col[k] for k,i in enumerate(self.c2_var) if i.get() == 1]]).tolist())[1:-1])
            self.xlabel_var.set(self.c1_var.get())
            #self.ylabel_var.set(self.c2_var.get())
            top1.destroy()
            self.root.attributes('-disabled',0)
            
        def cancel2():
            top1.destroy()
            self.root.attributes('-disabled',0)
        
        confirm_button = Button(top1,text='确认',command = confirm2)
        cancel_button = Button(top1,text='取消',command = cancel2)
        top_canvas1.create_window(120,710,width=240,height=20,window=confirm_button)
        top_canvas1.create_window(600,710,width=240,height=20,window=cancel_button)
            
    def prompt_confirm(self,multi,choice):
        if multi:
            self.top.destroy()
        self.data = self.data[choice]
        if len(self.data) == 0:
            messagebox.showwarning("警告","这个sheet中没有数据,导入数据失败")
            return
        top1 = Toplevel(self.table)
        top1.geometry('720x360')
        top1.resizable(False,False)
        top1.title("数据导入")
        top1.protocol('WM_DELETE_WINDOW',lambda : self.cancel(top1))
        
        top_canvas1 = Canvas(top1,width=720,height=360)
        top_canvas1.pack()
        
        tframe = Frame(top1)
        top_canvas1.create_window(360,150,width=720,height=300,window=tframe)
        
        a,b = self.data.shape
        col = np.array(self.data.columns).tolist()
        data = np.array(self.data).tolist()
        data1 = {'rec%d'%i : {  str(col[j]) : data[i][j] for j in range(b)  } for i in range(a)}
        ttable = TableCanvas(tframe,data=data1,cellbackgr=None,rowselectedcolor=None,read_only=True)
        ttable.show()
        c1_label = Label(top1,text='自变量选择')
        self.c1_var = StringVar()
        c1_combobox = ttk.Combobox(top1,values=col,textvariable=self.c1_var)
        top_canvas1.create_window(60,310,width=120,height=20,window=c1_label)
        top_canvas1.create_window(240,310,width=240,height=20,window=c1_combobox)
        
        c2_label = Label(top1,text='因变量选择')
        self.c2_var = StringVar()
        c2_combobox = ttk.Combobox(top1,values=col,textvariable=self.c2_var)
        top_canvas1.create_window(420,310,width=120,height=20,window=c2_label)
        top_canvas1.create_window(600,310,width=240,height=20,window=c2_combobox)
        
         
        
        def confirm():
            self.x_var.set(str(np.array(self.data[self.c1_var.get()]).tolist())[1:-1])
            self.y_var.set(str(np.array(self.data[self.c2_var.get()]).tolist())[1:-1])
            #self.xlabel_var.set(self.c1_var.get())
            #self.ylabel_var.set(self.c2_var.get())
            top1.destroy()
            self.root.attributes('-disabled',0)
            
        def cancel():
            top1.destroy()
            self.root.attributes('-disabled',0)
        
        confirm_button = Button(top1,text='确认',command = confirm)
        cancel_button = Button(top1,text='取消',command = cancel)
        top_canvas1.create_window(120,350,width=240,height=20,window=confirm_button)
        top_canvas1.create_window(600,350,width=240,height=20,window=cancel_button)
        
        