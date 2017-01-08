# -*- coding: utf-8 -*-


from settings_ui import Ui_Settings
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Settings(QWidget):
	mapStyleChanged = pyqtSignal(int, int)
	planeStyleChanged = pyqtSignal(tuple)

	def __init__(self, parent = None):
		QWidget.__init__(self, parent = None)
		self.ui = Ui_Settings()
		self.ui.setupUi(self)

		self._settings = QSettings(self)

		self.ui.planeIconColorButton.clicked.connect(self.colorDialog)
		self.ui.trackColorButton.clicked.connect(self.colorDialog)

		self.ui.planeApply.clicked.connect(self.planeApply)
		self.ui.mapApply.clicked.connect(self.mapApply)

	def saveWindowState(self, window):
		self._settings.setValue('geometry', window.saveGeometry())
		self._settings.setValue('state', window.saveState())

	def restoreWindowState(self, window):
		window.restoreGeometry(self._settings.value('geometry', '').toByteArray())
		window.restoreState(self._settings.value('state', '').toByteArray())

	def saveDockState(self, dock):
		self._settings.setValue('%s/geometry' % dock.objectName(), dock.saveGeometry())

	def restoreDockState(self, dock):
		dock.restoreGeometry(self._settings.value('%s/geometry' % dock.objectName(), '').toByteArray())

	def colorDialog(self):
		color = self.sender().palette().background().color()
		color = QColorDialog.getColor(color, self)
		self.setColor(self.sender(), color)

	def setColor(self, obj, color):
		if color.isValid():
			qss = 'background-color: %s' % color.name()
			obj.setStyleSheet(qss)

	def loadSettings(self):
		# Map
		l = self._settings.value('map/lightness', 0).toInt()[0]
		s = self._settings.value('map/saturation', 0).toInt()[0]
		alt = self._settings.value('home/altitude', 0).toFloat()[0]
		lng = self._settings.value('home/longitude', 0).toFloat()[0]
		self.ui.lightnessSlider.setValue(l)
		self.ui.saturationSlider.setValue(s)
		self.ui.altitudeEdit.setValue(alt)
		self.ui.longitudeEdit.setValue(lng)

		# Plane icons and tracks
		size = self._settings.value('plane/icon/size', 32).toInt()[0]
		self.ui.planeIconSizeSpinBox.setValue(size)
		color = self._settings.value('plane/icon/color', QColor(255, 255, 0)).toPyObject()
		self.setColor(self.ui.planeIconColorButton, color)

		width = self._settings.value('track/width', 2).toInt()[0]
		self.ui.trackWidthSpinBox.setValue(width)
		rainbow = self._settings.value('track/rainbow', True).toBool()
		self.ui.trackRainbowRadio.setChecked(rainbow)
		self.ui.trackSingleColorRadio.setChecked(not rainbow)
		color = self._settings.value('track/color', QColor(255, 0, 0)).toPyObject()
		self.setColor(self.ui.trackColorButton, color)

		self.updateMap(False)
		self.updatePlane(False)

	def mapApply(self):
		self.updateMap(True)

	def updateMap(self, save):
		lightness = self.ui.lightnessSlider.value()
		saturation = self.ui.saturationSlider.value()

		if save:
			self._settings.setValue('map/lightness', lightness)
			self._settings.setValue('map/saturation', saturation)

		self.mapStyleChanged.emit(lightness, saturation)

	def planeApply(self):
		self.updatePlane(True)

	def updatePlane(self, save):
		iconSize = self.ui.planeIconSizeSpinBox.value()
		iconColor = self.ui.planeIconColorButton.palette().background().color()
		trackWidth = self.ui.trackWidthSpinBox.value()

		trackColor = None
		if self.ui.trackSingleColorRadio.isChecked():
			trackColor = self.ui.trackColorButton.palette().background().color()

		if save:
			self._settings.setValue('plane/icon/size', iconSize)
			self._settings.setValue('plane/icon/color', iconColor)
			self._settings.setValue('track/width', trackWidth)
			if trackColor:
				self._settings.setValue('track/color', trackColor)
			self._settings.setValue('track/rainbow', not bool(trackColor))

		self.planeStyleChanged.emit((iconSize, iconColor, trackWidth, trackColor))

