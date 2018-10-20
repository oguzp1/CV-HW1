from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotCanvas(FigureCanvas):
    def __init__(self, hist, parent=None, width=5, height=4, dpi=100):
        FigureCanvas.__init__(self, Figure(figsize=(width, height), dpi=dpi))
        self.plotHistogram(hist)

    def plotHistogram(self, hist):
        axes1 = self.figure.add_subplot(311)
        axes1.hist(hist[0], color=[1, 0 ,0])

        axes2 = self.figure.add_subplot(312)
        axes2.hist(hist[1], color=[0, 1, 0])

        axes3 = self.figure.add_subplot(313)
        axes3.hist(hist[2], color=[0, 0, 1])

        self.draw()
