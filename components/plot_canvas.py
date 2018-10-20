from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotCanvas(FigureCanvas):
    def __init__(self, hist, parent=None, width=5, height=4, dpi=100):
        FigureCanvas.__init__(self, Figure(figsize=(width, height), dpi=dpi))
        self.plotHistogram(hist)

    def plotHistogram(self, hist):
        common_range = range(0, 256)

        axes1 = self.figure.add_subplot(311)
        axes1.bar(common_range, hist[0], color=[1, 0 ,0])

        axes2 = self.figure.add_subplot(312)
        axes2.bar(common_range, hist[1], color=[0, 1, 0])

        axes3 = self.figure.add_subplot(313)
        axes3.bar(common_range, hist[2], color=[0, 0, 1])

        self.draw()
