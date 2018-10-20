from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class ImageGroup(QGroupBox):
    def __init__(self, str, parent=None):
        super().__init__(str, parent)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.setAlignment(Qt.AlignHCenter)

        self.imageLabel = QLabel()

        vbox.addWidget(self.imageLabel)
        self.setLayout(vbox)

    def getImageLabel(self):
        return self.imageLabel

    def addWidget(self, widget):
        self.layout().addWidget(widget)
