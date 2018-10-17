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

        self.inputLoaded = False
        self.targetLoaded = False
        
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
        self.inputLoaded = True
        print('input')

    def openTargetImage(self):
        # This function is called when the user clicks File->Target Image.
        self.targetLoaded = True
        print('target')

    def initUI(self):
        # Write GUI initialization code
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.right, self.width, self.height)
        self.show()

    def histogramButtonClicked(self):
        if not self.inputLoaded and not self.targetLoaded:
            QMessageBox.warning(self, "Input and Target Missing!", "Please load input and target images first!", QMessageBox.Ok)
        elif not self.inputLoaded:
            QMessageBox.warning(self, "Input Missing!", "Please load an input image first!", QMessageBox.Ok)
        elif not self.targetLoaded:
            QMessageBox.warning(self, "Target Missing!", "Please load a target image first!", QMessageBox.Ok)
        else:
            print('success')

    def calcHistogram(self, I):
        # Calculate histogram
        return NotImplementedError

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
