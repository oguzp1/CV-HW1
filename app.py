import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QGroupBox, QAction, QFileDialog
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        return NotImplementedError


        self.title = 'Histogram Equalization'
        # You can define other things in here
        self.initUI()

    def openInputImage(self):
        # This function is called when the user clicks File->Input Image.
        return NotImplementedError

    def openTargetImage(self):
        # This function is called when the user clicks File->Target Image.
        return NotImplementedError

    def initUI(self):
        return NotImplementedError
        # Write GUI initialization code

        self.show()

    def histogramButtonClicked(self):
        if not self.inputLoaded and not self.targetLoaded:
            # Error: "First load input and target images" in MessageBox
            return NotImplementedError
        if not self.inputLoaded:
            # Error: "Load input image" in MessageBox
            return NotImplementedError
        elif not self.targetLoaded:
            # Error: "Load target image" in MessageBox
            return NotImplementedError

    def calcHistogram(self, I):
        # Calculate histogram
        return NotImplementedError

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
