import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QGroupBox, QAction, QFileDialog, QSpacerItem, QGridLayout
from PyQt5.QtGui import QPixmap, QImage, QColor
from components.image_group import ImageGroup
from components.plot_canvas import PlotCanvas

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.title = 'Histogram Equalization'
        
        self.left = 100
        self.right = 100
        self.width = 1600
        self.height = 900

        self.inputLoaded = False
        self.targetLoaded = False

        self.inputPixMap = None
        self.targetPixMap = None

        self.groupInput = ImageGroup("Input")
        self.groupTarget = ImageGroup("Target")
        self.groupResult = ImageGroup("Result")

        self.setCentralWidget(QWidget())

        self.initUI()

    def openInputImage(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Input File", ".", "Image Files (*.png *.jpg)")
        
        if filename != '':
            self.inputLoaded = True
            self.inputPixMap = QPixmap(filename)
            self.groupInput.getImageLabel().setPixmap(self.inputPixMap)

    def openTargetImage(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Target File", ".", "Image Files (*.png *.jpg)")
        
        if filename != '':
            self.targetLoaded = True
            self.targetPixMap = QPixmap(filename)
            self.groupTarget.getImageLabel().setPixmap(self.targetPixMap)

    def initUI(self):
        inputAction = QAction("&Open Input", self)
        inputAction.triggered.connect(self.openInputImage)

        targetAction = QAction("&Open Target", self)
        targetAction.triggered.connect(self.openTargetImage)

        exitAction = QAction("&Exit", self)
        exitAction.triggered.connect(self.close)

        equalizeAction = QAction("&Equalize Histogram", self)
        equalizeAction.triggered.connect(self.histogramButtonClicked)

        menu = self.menuBar()
        fileMenu = menu.addMenu("&File")
        fileMenu.addAction(inputAction)
        fileMenu.addAction(targetAction)
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar("&File")
        toolbar.addAction(equalizeAction)

        grid = QGridLayout()

        grid.addWidget(self.groupInput, 0, 1)
        grid.addWidget(self.groupTarget, 0, 3)
        grid.addWidget(self.groupResult, 0, 5)

        grid.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Maximum), 0, 0)
        grid.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Maximum), 0, 2)
        grid.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Maximum), 0, 4)
        grid.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Maximum), 0, 6)

        self.centralWidget().setLayout(grid)
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
