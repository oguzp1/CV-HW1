from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QLabel
from PyQt5.QtGui import QPixmap, QImage

class ImageGroup(QGroupBox):
    def __init__(self, str, parent=None):
        super().__init__(str, parent)
        vbox = QVBoxLayout()
        vbox.addStretch(1)

        self.labelTop = QLabel()
        self.labelBottom = QLabel()

        vbox.addWidget(self.labelTop)
        vbox.addWidget(self.labelBottom)
        self.setLayout(vbox)

    def setTop(self, topWidget):
        self.labelTop.addWidget(topWidget)

    def setBottom(self, bottomWidget):
        self.labelBottom.addWidget(bottomWidget)

    def setImage(self, im):
        pass
