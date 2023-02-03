# -*- coding: utf-8 -*-
""" This is FreezeTableWidget module """
 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
 
 
class FreezeTableWidget(QTableView):
    def __init__(self, parent=None, fixed_col_count=1, *args):
        QTableView.__init__(self, parent, *args)
 
        self._fixed_col_count = fixed_col_count
 
        self.frozenTableView = QTableView(self)
 
        self.frozenTableView.verticalHeader().hide()
        self.frozenTableView.setFocusPolicy(Qt.NoFocus)
        self.frozenTableView.setStyleSheet('''border: none; background-color: #CCC''')
        self.frozenTableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.frozenTableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.frozenTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
 
        self.viewport().stackUnder(self.frozenTableView)
 
        self.setShowGrid(True)
 
        hh = self.horizontalHeader()
        hh.setDefaultAlignment(Qt.AlignCenter)
        hh.setStretchLastSection(True)
 
        self.resizeColumnsToContents()
 
        vh = self.verticalHeader()
        vh.setDefaultSectionSize(25)
        vh.setDefaultAlignment(Qt.AlignCenter)
        vh.setVisible(True)
        self.frozenTableView.verticalHeader().setDefaultSectionSize(vh.defaultSectionSize())
 
        self.frozenTableView.show()
        self.updateFrozenTableGeometry()
 
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.frozenTableView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
 
        # connect the headers and scrollbars of both table view's together
        self.horizontalHeader().sectionResized.connect(self.updateSectionWidth)
        self.verticalHeader().sectionResized.connect(self.updateSectionHeight)
        self.frozenTableView.verticalScrollBar().valueChanged.connect(self.verticalScrollBar().setValue)
        self.verticalScrollBar().valueChanged.connect(self.frozenTableView.verticalScrollBar().setValue)
 
    @property
    def fixed_col_count(self):
        return self._fixed_col_count
 
    @fixed_col_count.setter
    def fixed_col_count(self, value):
        self._fixed_col_count = value
 
    def setModel(self, model: QAbstractTableModel):
        QTableView.setModel(self, model)
        self.frozenTableView.setModel(model)
        self.frozenTableView.verticalHeader().hide()
        self.frozenTableView.setFocusPolicy(Qt.NoFocus)
 
        cols = model.columnCount()
        for col in range(cols):
            if col not in range(self._fixed_col_count):
                self.frozenTableView.setColumnHidden(col, True)
            else:
                self.frozenTableView.setColumnWidth(col, self.columnWidth(col))
 
    def updateSectionWidth(self, logicalIndex, oldSize, newSize):
        if logicalIndex in range(self._fixed_col_count):
            self.frozenTableView.setColumnWidth(logicalIndex, newSize)
            self.updateFrozenTableGeometry()
 
    def updateSectionHeight(self, logicalIndex, oldSize, newSize):
        self.frozenTableView.setRowHeight(logicalIndex, newSize)
 
    def resizeEvent(self, event):
        QTableView.resizeEvent(self, event)
        self.updateFrozenTableGeometry()
 
    def scrollTo(self, index, hint):
        if index.column() >= self._fixed_col_count:
            QTableView.scrollTo(self, index, hint)
 
    def updateFrozenTableGeometry(self):
        frozen_width = sum([self.frozenTableView.columnWidth(col) for col in range(self._fixed_col_count)])
        if self.verticalHeader().isVisible():
            self.frozenTableView.setGeometry(self.verticalHeader().width() + self.frameWidth(),
                                             self.frameWidth(), frozen_width,
                                             self.viewport().height() + self.horizontalHeader().height())
        else:
            self.frozenTableView.setGeometry(self.frameWidth(),
                                             self.frameWidth(), frozen_width,
                                             self.viewport().height() + self.horizontalHeader().height())
 
    def moveCursor(self, cursorAction, modifiers):
        current = QTableView.moveCursor(self, cursorAction, modifiers)
        x = self.visualRect(current).topLeft().x()
        frozen_width = sum([self.frozenTableView.columnWidth(col) for col in range(self._fixed_col_count)])
        if cursorAction == self.MoveLeft:
            if current.column() >= self._fixed_col_count and x < frozen_width:
                new_value = self.horizontalScrollBar().value() + x - frozen_width
                self.horizontalScrollBar().setValue(new_value)
            elif current.column() < self._fixed_col_count:
                current = self.model().index(current.row(), current.column() + 1)
        elif cursorAction == self.MoveHome:
            new_value = self.horizontalScrollBar().value() + x - frozen_width
            self.horizontalScrollBar().setValue(new_value)
            current = self.model().index(current.row(), self._fixed_col_count)
 
        return current