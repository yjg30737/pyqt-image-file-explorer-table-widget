from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGraphicsView, QGridLayout, QGraphicsScene


class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.__fixInViewFlag = True
        self.__filename = ''

        self.__initUi()

    def __initUi(self):
        self.__p = ''
        self.__scene = ''
        self.__graphicItem = ''

        self.__image_view = QGraphicsView()

        self.__defaultStyleSheet = self.styleSheet()

        layout = QGridLayout()
        layout.addWidget(self.__image_view)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def setPixmap(self, p):
        self.__set_pixmap(p)

    def __set_pixmap(self, p):
        self.__p = p
        self.__scene = QGraphicsScene()
        self.__graphicItem = self.__scene.addPixmap(self.__p)
        self.__image_view.setScene(self.__scene)
        self.__image_view.show()
        if self.__fixInViewFlag:
            self.__image_view.fitInView(self.__graphicItem, Qt.KeepAspectRatio)

    def getPixmap(self):
        return self.__p

    def getFileName(self):
        return self.__filename

    def resizeEvent(self, e):
        if self.__graphicItem:
            if self.__fixInViewFlag:
                self.__image_view.fitInView(self.__graphicItem, Qt.KeepAspectRatio)
        return super().resizeEvent(e)

    def setFixInView(self, f: bool):
        self.__fixInViewFlag = f

    def get_image_view(self):
        return self.__image_view
