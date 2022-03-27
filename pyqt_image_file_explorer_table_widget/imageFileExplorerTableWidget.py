import operator
import os
from collections import defaultdict

from PyQt5.QtWidgets import QWidget, QTableWidget, QHBoxLayout
from pyqt_resource_helper import PyQtResourceHelper

from pyqt_image_file_explorer_table_widget.imageLabelWidget import ImageLabelWidget


class ImageFileExplorerTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.__basename_absname_dict = defaultdict(str)
        self.__padding = 0
        self.__initUi()

    def __initUi(self):
        self.setShowGrid(False)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        PyQtResourceHelper.setStyleSheet([self], ['style/table.css'])

    def resizeEvent(self, e):
        self.setAllCellsAsSquare()
        return super().resizeEvent(e)

    def outerCellWidget(self, row: int, column: int):
        return self.indexWidget(self.model().index(row, column))

    def cellWidget(self, row: int, column: int):
        widget = super().cellWidget(row, column)
        if widget:
            item = widget.layout().itemAt(0)
            if item:
                return item.widget()

    def setAllCellsAsSquare(self):
        sq_width = self.viewport().width() // self.columnCount()
        for r_idx in range(self.rowCount()):
            self.setRowHeight(r_idx, sq_width)
        for c_idx in range(self.columnCount()):
            self.setColumnWidth(c_idx, sq_width)

    def setRowCount(self, rows: int) -> None:
        super().setRowCount(rows)
        self.setAllCellsAsSquare()

    def setColumnCount(self, columns: int) -> None:
        super().setColumnCount(columns)
        self.setAllCellsAsSquare()

    def get_last_idx(self):
        last_r, last_c = divmod(self.count(), self.columnCount())
        return last_r, last_c

    def count(self):
        cnt = len(self.__basename_absname_dict)
        return cnt

    def getFilenamesDuplicateFiltered(self, filenames):
        filenames_filtered_duplicated = []
        for filename in filenames:
            basename = os.path.basename(filename)
            if self.__basename_absname_dict.get(basename, '') == filename:
                pass
            else:
                filenames_filtered_duplicated.append(filename)
        return filenames_filtered_duplicated

    def addCells(self, filenames):
        filenames = self.getFilenamesDuplicateFiltered(filenames)

        for i in range(len(filenames)):
            start_r, start_c = self.get_last_idx()
            if start_c == 0:
                self.setRowCount(start_r+1)
            self.addCell(start_r, start_c, filenames[i])

    def addCell(self, r, c, filename: str):
        innerWidget = ImageLabelWidget(filename)
        innerWidget.setText(os.path.basename(filename))

        lay = QHBoxLayout()
        lay.addWidget(innerWidget)
        lay.setContentsMargins(self.__padding, self.__padding, self.__padding, self.__padding)

        widget = QWidget()
        widget.setLayout(lay)
        self.setCellWidget(r, c, widget)

        basename = os.path.basename(filename)
        self.__basename_absname_dict[basename] = filename

    def get_sorted_selected_indexes(self):
        indexes = self.selectedIndexes()
        rc_idx_lst = [[index.row(), index.column(), index] for index in indexes]
        sorted_rc_idx_lst = sorted(rc_idx_lst, key=operator.itemgetter(0, 1))
        indexes = [i[2] for i in sorted_rc_idx_lst]
        return indexes

    def removeSelectedCells(self):
        indexes = self.get_sorted_selected_indexes()

        group_unit_lst = []
        group_unit = []
        for i in range(1, len(indexes)):
            idx1, idx2 = indexes[i - 1], indexes[i]
            r1, c1, r2, c2 = idx1.row(), idx1.column(), idx2.row(), idx2.column()
            r_diff, c_diff = abs(r2 - r1), abs(c1 - c2)
            group_unit.append(idx1)
            if (r_diff == 0 and c_diff == 1) or (r_diff == 1 and c_diff == self.columnCount() - 1):
                pass
            else:
                group_unit_lst.append(group_unit)
                group_unit = []

        group_unit.append(indexes[-1])
        group_unit_lst.append(group_unit)
        group_unit = []

        cell_cnt_to_move = 0
        cell_cnt_to_move_whole = 0

        for i in range(len(group_unit_lst)):
            group_unit = group_unit_lst[i]
            r_start = group_unit[-1].row()
            c_start = group_unit[-1].column()

            for j in group_unit:
                r_to_remove = j.row()
                c_to_remove = j.column()
                r_to_move, c_to_remove = divmod(c_to_remove - cell_cnt_to_move_whole, self.columnCount())
                r_to_remove += r_to_move
                widget = self.cellWidget(r_to_remove, c_to_remove)
                if widget:
                    self.removeImageCell(r_to_remove, c_to_remove)
                    r_start = r_to_remove
                    c_start = c_to_remove

            cell_cnt_to_move = len(group_unit)
            cell_cnt_to_move_whole += len(group_unit)
            self.moveRowsUpward(r_start, c_start, cell_cnt_to_move)
        # self.removeEmptyCell()

    def moveRowsUpward(self, r_start, c_start, cell_cnt_to_move):
        self.moveColumnLeftward(r_start, c_start, cell_cnt_to_move)
        r_start += 1
        for r in range(r_start, self.rowCount()):
            self.moveColumnLeftward(r, 0, cell_cnt_to_move)

    # fixme please
    def removeEmptyCell(self):
        start_r, start_c = divmod(self.count(), self.columnCount())
        print(self.count(), start_r, start_c)
        for i in range(start_c, self.columnCount()):
            self.removeCellWidget(start_r, i)
        start_r += 1
        for i in range(start_r, self.rowCount()):
            self.removeRow(i)

    def moveColumnLeftward(self, r_start, c_start, cell_cnt_to_move):
        c_start = c_start
        while True:
            r_to_move, c_to_move = divmod(cell_cnt_to_move, self.columnCount())
            r_end = r_start - r_to_move
            c_end = c_start - c_to_move
            innerWidget = self.cellWidget(r_start, c_start)

            if innerWidget:
                if c_end < 0:
                    self.moveImageCell(r_end - 1, self.columnCount() + c_end,
                                       innerWidget)
                else:
                    self.moveImageCell(r_end, c_end, innerWidget)

            else:
                if c_end < 0:
                    pass
                else:
                    pass

            c_start += 1
            if c_start >= self.columnCount():
                break

    def moveImageCell(self, r, c, innerWidget):
        lay = QHBoxLayout()
        lay.addWidget(innerWidget)
        lay.setContentsMargins(self.__padding, self.__padding, self.__padding, self.__padding)

        widget = QWidget()
        widget.setLayout(lay)

        self.setCellWidget(r, c, widget)

    def removeImageCell(self, r, c):
        widget = self.cellWidget(r, c)
        if widget:
            filename = widget.getText()
            basename = os.path.basename(filename)
            del (self.__basename_absname_dict[basename])
            return super().removeCellWidget(r, c)

    def setPadding(self, padding: int):
        self.__padding = padding