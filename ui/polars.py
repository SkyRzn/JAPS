# -*- coding: utf-8 -*-


from polars_ui import Ui_Polars
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Polars(QWidget):
	mapStyleChanged = pyqtSignal(int, int)
	planeStyleChanged = pyqtSignal(tuple)

	def __init__(self, parent = None):
		QWidget.__init__(self, parent = None)
		self.ui = Ui_Polars()
		self.ui.setupUi(self)
