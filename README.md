# pyqt-image-file-explorer-table-widget
PyQt QTableWidget for image file explorer

## Requirements
PyQt5

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-image-file-explorer-table-widget.git --upgrade```

## Example
```python
import os

from pyqt_image_file_explorer_table_widget.imageFileExplorerTableWidget import ImageFileExplorerTableWidget
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QGridLayout, QFileDialog, QApplication


class ImageFileExplorerExample(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__tableWidget = ImageFileExplorerTableWidget()

        addBtn = QPushButton('Add')
        addBtn.clicked.connect(self.__add)

        delBtn = QPushButton('Remove')
        delBtn.clicked.connect(self.__delete)

        lay = QHBoxLayout()
        lay.addWidget(addBtn)
        lay.addWidget(delBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        btns = QWidget()
        btns.setLayout(lay)

        self.__tableWidget.setColumnCount(6)
        self.__tableWidget.setAllCellsAsSquare()

        lay = QGridLayout()
        lay.addWidget(btns)
        lay.addWidget(self.__tableWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        self.setLayout(lay)

    def __add(self):
        dirname = QFileDialog.getExistingDirectory(self, 'Open directory', '')
        if dirname:
            filenames = [os.path.join(dirname, filename) for filename in os.listdir(dirname)]
            filenames = list(filter(lambda x: os.path.splitext(x)[-1] in ['.png'],
                                    [filename for filename in filenames]))
            self.__tableWidget.addCells(filenames)

    def __delete(self):
        self.__tableWidget.removeSelectedCells()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    imageFileExplorerExample = ImageFileExplorerExample()
    imageFileExplorerExample.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/146850027-f3f68b75-ec47-406d-ae54-0cf5f2cbf31d.png)
