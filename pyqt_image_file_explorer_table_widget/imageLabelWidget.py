import os.path

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

from pyqt_image_file_explorer_table_widget.imageWidget import ImageWidget


class ImageLabelWidget(QWidget):
    def __init__(self, filename='', parent=None):
        super().__init__(parent)
        self.__absname = filename
        self.__initUi(filename)

    def __initUi(self, filename=''):
        self.__topWidget = ImageWidget()
        self.__topWidget.setPixmap(QPixmap(filename))

        self.__bottomWidget = QLabel(os.path.basename(filename))
        self.__bottomWidget.setAlignment(Qt.AlignCenter)
        self.__bottomWidget.setWordWrap(True)

        lay = QVBoxLayout()
        lay.addWidget(self.__topWidget)
        lay.addWidget(self.__bottomWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        self.setLayout(lay)

    def getText(self):
        return self.__bottomWidget.text()

    def getTextAsAbsName(self):
        return self.__absname

    def setText(self, text):
        self.__bottomWidget.setText(text)

    def showTinyImageBigger(self, f: bool):
        self.__topWidget.showTinyImageBigger(f)