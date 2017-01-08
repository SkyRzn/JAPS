# -*- coding: utf-8 -*-


from planes_ui import Ui_Planes
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Planes(QWidget):
	mapStyleChanged = pyqtSignal(int, int)
	planeStyleChanged = pyqtSignal(tuple)

	def __init__(self, parent = None):
		QWidget.__init__(self, parent = None)
		self.ui = Ui_Planes()
		self.ui.setupUi(self)
