from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib import pyplot as plt 
from matplotlib.figure import Figure

import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setUI()

    def setUI(self):
        w = QWidget()
        self.f = QFormLayout()

        self.cb = QComboBox()
        self.cb.addItems(['Solarize_Light2',
                        '_classic_test_patch',
                        'bmh',
                        'classic',
                        'dark_background',
                        'fast',
                        'fivethirtyeight',
                        'ggplot',
                        'grayscale',
                        'seaborn',
                        'seaborn-bright',
                        'seaborn-colorblind',
                        'seaborn-dark',
                        'seaborn-dark-palette',
                        'seaborn-darkgrid',
                        'seaborn-deep',
                        'seaborn-muted',
                        'seaborn-notebook',
                        'seaborn-paper',
                        'seaborn-pastel',
                        'seaborn-poster',
                        'seaborn-talk',
                        'seaborn-ticks',
                        'seaborn-white',
                        'seaborn-whitegrid',
                        'tableau-colorblind10'])
        
        self.cb.currentIndexChanged.connect(self.change)

        self.fig = FigureCanvas(plt.figure(figsize=(5, 15)))
        self.ax = self.fig.figure.add_subplot(111)
        
        x = [1,2,3,4]
        y = [1,4,9,17]

        self.ax.plot(x,y)

        self.f.addRow(self.cb)
        self.f.addRow(self.fig)
        
        
        w.setLayout(self.f)
        self.setCentralWidget(w)
    
    def change(self):
        plt.style.use(self.cb.currentText())
        self.f.removeRow(self.fig)

        self.fig = FigureCanvas(plt.figure(figsize=(5, 15)))
        self.ax = self.fig.figure.add_subplot(111)
        
        x = [1,2,3,4]
        y = [1,4,9,17]

        self.ax.plot(x,y)

        self.f.addRow(self.fig)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = Window()
    m.show()
    sys.exit(app.exec())