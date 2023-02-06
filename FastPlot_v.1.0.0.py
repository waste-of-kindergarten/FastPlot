import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure

import os
import clipboard
import Pmw
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import *
from tkintertable import TableCanvas,TableModel
from ast import literal_eval

import numpy as np
import pandas as pd
from PIL import Image,ImageTk

from mainui import *
if __name__ == "__main__":
    mainwindow = MainWindow()
    mainwindow.mainloop()
