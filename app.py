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

        self.title = 'Histogram Equalization'
        
        self.left = 100
        self.right = 100
        self.width = 640
        self.height = 400
        
        inputAction = QAction("&Open Input", self)
        inputAction.triggered.connect(self.openInputImage)

        targetAction = QAction("&Open Target", self)
        targetAction.triggered.connect(self.openTargetImage)

        exitAction = QAction("&Exit", self)
        exitAction.triggered.connect(self.close)

        menu = self.menuBar()
        fileMenu = menu.addMenu("&File")
        fileMenu.addAction(inputAction)
        fileMenu.addAction(targetAction)
        fileMenu.addAction(exitAction)

        self.initUI()

    def openInputImage(self):
        # This function is called when the user clicks File->Input Image.
        print('input')

    def openTargetImage(self):
        # This function is called when the user clicks File->Target Image.
        print('target')

    def initUI(self):
        # Write GUI initialization code
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.right, self.width, self.height)
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
