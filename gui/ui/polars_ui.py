# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'polars.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Polars(object):
    def setupUi(self, Polars):
        Polars.setObjectName(_fromUtf8("Polars"))
        Polars.resize(408, 426)
        self.gridLayout = QtGui.QGridLayout(Polars)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.addButton = QtGui.QToolButton(Polars)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/icons/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 0, 0, 1, 1)
        self.deleteButton = QtGui.QToolButton(Polars)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/icons/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridLayout.addWidget(self.deleteButton, 0, 1, 1, 1)
        self.editButton = QtGui.QToolButton(Polars)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/icons/application_edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon2)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.gridLayout.addWidget(self.editButton, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(291, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.table = QtGui.QTableWidget(Polars)
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setRowCount(1)
        self.table.setColumnCount(3)
        self.table.setObjectName(_fromUtf8("table"))
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.table, 1, 0, 1, 4)

        self.retranslateUi(Polars)
        QtCore.QMetaObject.connectSlotsByName(Polars)

    def retranslateUi(self, Polars):
        Polars.setWindowTitle(_translate("Polars", "Form", None))
        self.addButton.setText(_translate("Polars", "...", None))
        self.deleteButton.setText(_translate("Polars", "...", None))
        self.editButton.setText(_translate("Polars", "...", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Polars", "Source", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Polars", "Color", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Polars", "Visible", None))

import rsc_rc
