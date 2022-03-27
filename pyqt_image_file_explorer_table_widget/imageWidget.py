from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem


class ImageWidget(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__p = ''
        self.__scene = ''
        self.__graphicItem = ''

        self.verticalScrollBar().blockSignals(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet('background-color: transparent; border: 0;')

    def setPixmap(self, p):
        self.__set_pixmap(p)

    def __set_pixmap(self, p):
        self.__p = p
        self.__scene = QGraphicsScene()
        self.__graphicItem = self.__scene.addPixmap(self.__p)
        self.setScene(self.__scene)

    def getPixmap(self):
        return self.__p

    def resizeEvent(self, e):
        if isinstance(self.__graphicItem, QGraphicsItem):
            real_size = self.__graphicItem.boundingRect()
            view_size = self.rect()
            if real_size.width() > view_size.width() or real_size.height() > view_size.height():
                self.fitInView(self.__graphicItem, Qt.KeepAspectRatio)
        return super().resizeEvent(e)