#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from map import Map

from point import Point
from dispatcher import Dispatcher
from net import Net
import sbs

from ui.settings import Settings
from ui.polars import Polars


class Browser(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.resize(800, 600)
		self._map = Map(self)
		self._map.loadFinished.connect(self.mapLoaded)
		self.setCentralWidget(self._map)
		self._net = None

		self._dispatcher = Dispatcher(self)

		self._dispatcher.planesAdded.connect(self._map.addPlanes)
		self._dispatcher.planesUpdated.connect(self._map.updatePlanes)
		self._dispatcher.planesRemoved.connect(self._map.removePlanes)

		self._dispatcher.planesAdded.connect(self.addPlanes)
		self._dispatcher.planesRemoved.connect(self.removePlanes)

		self._dispatcher.polarsAdded.connect(self._map.addPolars)
		self._dispatcher.polarsUpdated.connect(self._map.updatePolars)

		self.createDocks()

		self._settings.restoreWindowState(self)
		for dock in self._docks.values():
			self._settings.restoreDockState(dock)

	def mapLoaded(self):

		self._settings.loadSettings()

		self._net = Net('192.168.0.111', 30003, sbs.strToPoints)
		self._dispatcher.addSourceQueue(0, self._net)
		self._net.start()

	def createDock(self, name, widget):
		dock = QDockWidget(name, self)
		dock.setObjectName(name)
		dock.setWidget(widget)
		self.addDockWidget(Qt.RightDockWidgetArea, dock)
		self._docks[name] = dock
		return widget

	def createDocks(self):
		self._docks = {}

		self._polars = self.createDock('Polars', Polars(self))
		self._planes = self.createDock('Planes', QListWidget(self))
		self._settings = self.createDock('Settings', Settings(self))

		self._settings.mapStyleChanged.connect(self._map.setMapStyle)
		self._settings.planeStyleChanged.connect(self.planeStyleChanged)
		self._settings.homeChanged.connect(self.setHome)

	def planeStyleChanged(self, style):
		self._map.setPlaneStyle(style)
		self._map.removePlanes()
		self._map.addPlanes(self._dispatcher.planes())

	def addPlanes(self, planes):
		items = []
		for code in planes:
			items.append(code)
		self._planes.addItems(items)

	def removePlanes(self, planes):
		items = []
		for code in planes:
			for i in range(self._planes.count()):
				if code == self._planes.item(i).text():
					self._planes.takeItem(i)
					break

	def setHome(self, alt, lng):
		#54.613579, 39.815831
		home = None
		if alt != 0 and lng != 0:
			home = Point(alt, lng, grad=True)
		self._dispatcher.setHome(home)
		self._map.setHome(home)

	def closeEvent(self, event):
		self._settings.saveWindowState(self)

		for dock in self._docks.values():
			self._settings.saveDockState(dock)

		if self._net:
			self._net.stop()

		QMainWindow.closeEvent(self, event)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setOrganizationName('Sky')
	app.setApplicationName('JAPS')

	splash = QSplashScreen()
	splash.show()
	app.processEvents()

	main = Browser()
	main.show()
	splash.finish(main)
	sys.exit(app.exec_())

