from PyQt5 import QtWidgets , uic
from PyQt5.QtWidgets import *
from pyqtgraph import *
from pyqtgraph import PlotWidget, PlotItem
import pyqtgraph as pg
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import pathlib
import numpy as np
#from MainWindow import Ui_MainWindow

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('task2.ui', self)
        self.show()

        # creating timers
        self.timer1 = QtCore.QTimer()
        self.Timer= self.timer1 
        self.GraphicsView= self.graphicsView
        self.handle_buttons()

    def handle_buttons(self):
        self.browse.clicked.connect(lambda : self.load())
        pass

    def read_file(self):
                path = QFileDialog.getOpenFileName()[0]
                if pathlib.Path(path).suffix == ".csv":
                    self.data = np.genfromtxt(path, delimiter=',')
                    self.x = list(self.data[:, 0])
                    self.y = list(self.data[:, 1])
     
    def load(self): 
                self.read_file()
                self.data_line =self.GraphicsView.plot(self.x, self.y,)
                self.GraphicsView.plotItem.setLimits(xMin=0, xMax=12, yMin=-0.6, yMax=0.6)
                self.IDX= 0
                self.Timer.setInterval(100)
                self.Timer.timeout.connect(lambda : self.update_plot_data())
                self.Timer.start()
    
    def update_plot_data(self):
                x = self.x[:self.IDX]
                y = self.y[:self.IDX]
                self.IDX += 10
                if self.IDX > len(self.x):
                    self.IDX = 0
                if self.x[self.IDX] > 0.5:
                    self.GraphicsView.setLimits(xMin=min(x, default=0), xMax=max(x, default=0))  # disable paning over xlimits
                self.GraphicsView.plotItem.setXRange(max(x, default=0) - 0.5, max(x, default=0))
                self.data_line.setData(x, y)   

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()