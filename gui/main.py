#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
sys.path.insert(0, '..')

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from map import Map

from engine.point import Point
from engine.dispatcher import Dispatcher
from engine.net import Net

from ui.settings import Settings
from ui.polars import Polars


class Browser(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.resize(800, 600)

		self._timer = QTimer()
		self._timer.timeout.connect(self.updateDispatcher)

		self._map = Map(self)
		self._map.loadFinished.connect(self.mapLoaded)
		self.setCentralWidget(self._map)

		self._dispatcher = Dispatcher()
		inp = self._dispatcher.input()
		inp.addGroup('hui')
		data = {'type':'net','format':'sbs','address':'localhost', 'port':30003}
		inp.addSource('hui', 'djigurda', data)

		self.createDocks()

		self._settings.restoreWindowState(self)
		for dock in self._docks.values():
			self._settings.restoreDockState(dock)

	def mapLoaded(self):
		self._settings.loadSettings()

		self._dispatcher.addTracker('lol', ['hui'], 600, self.trackerCallback)

		home = Point(54.613579, 39.815831, grad=True)
		polar = self._dispatcher.addPolar('lol', home, ['hui'], self.polarCallback)
		self._map.addPolar(polar)

		self._dispatcher.start()
		self._timer.start(100)

	def updateDispatcher(self):
		self._dispatcher.update()

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

	def planeStyleChanged(self, style):
		self._map.setPlaneStyle(style)
		#self._map.removePlanes()
		#self._map.addPlanes(self._dispatcher.planes())

	def trackerCallback(self, added, updated, removed):
		self._map.addPlanes(added)
		self._map.updatePlanes(updated)
		self._map.removePlanes(removed)

	def polarCallback(self, polar):
		self._map.updatePolar(polar)

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

	def closeEvent(self, event):
		self._settings.saveWindowState(self)

		for dock in self._docks.values():
			self._settings.saveDockState(dock)

		self._dispatcher.stop()

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

