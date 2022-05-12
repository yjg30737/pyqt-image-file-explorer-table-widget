# pyqt-image-file-explorer-table-widget
PyQt QTableWidget for image file explorer

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-image-file-explorer-table-widget`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>

## Feature
* Being able to set column count with `setColumnCount(columns: int)`
* Being able to remove selected cells with `removeSelectedCells()`
* Set cell padding with `setCellPadding(padding: int)`. No padding by defeault.
* Set cell margin (set space between cells) with `setCellMargin(margin: int)` - This doesn't give the space between cells, just looks like it. I will figure it out how to set the space between cells properly. No margin by default.
* Resize friendly
* If you want to add grid(no grid by default), use `setShowGrid(f: bool)` even though this is provided by `QTableWidget` originally.
* `showTinyImageBigger(f: bool)` to expand image which is so small that it's hard to see

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
                                    [filename for filename in filenames])) # In this example, png only
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

![image](https://user-images.githubusercontent.com/55078043/160266304-248efc38-052c-4b40-baf8-9504c7dd90db.png)

After select add.png, addTab.png, bold.png and remove all of them

![image](https://user-images.githubusercontent.com/55078043/160266313-61612265-55fd-46fe-a9c3-9d5dcd4ce80e.png)

