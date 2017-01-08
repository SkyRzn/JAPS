#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from time import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebView, QWebPage

from point import Point
from polar import Polar
from plane import Plane
from net import Net
import sbs



class WebPage(QWebPage):
	def javaScriptConsoleMessage(self, msg, line, source):
		print '%d: %s' % (line, msg)

class Map(QWebView):
	initFinished = pyqtSignal()
	def __init__(self, parent = None):
		QWebView.__init__(self, parent)

		page = WebPage()
		self.setPage(page)

		self._frame = self.page().mainFrame()

		self._rscDir = '%s/resources' % os.path.dirname(os.path.realpath(__file__))
		f = open('%s/map.html' % self._rscDir, 'r')
		html = f.read()
		f.close()
		self.setHtml(html)
		#self.load(QUrl(self._rscDir + '/map.html'))

	def script(self, script):
		self._frame.evaluateJavaScript(script).toString();

	def setHome(self, point):
		self.script('setHome(%s, true);' % (point.js()));

	def addPlanes(self, planes):
		for id, plane in planes.items():
			self.script('addPlane("%s", %s, %s);' % (id, plane.jsTrack(), plane.jsInfo()));

	def updatePlanes(self, planes):
		for id, item in planes.items():
			plane, fromPoint = item
			self.script('addPlanePoints("%s", %s, %s);' % (id, plane.jsTrack(fromPoint-1), plane.jsInfo()));

	def removePlanes(self, ids = None):
		if ids == None:
			self.script('cleanPlanes();');
			return
		for id in ids:
			self.script('removePlane("%s");' % id);

	def addPolars(self, polars):
		for id, polar in polars.items():
			self.script('addPolar(%d, "#00ff00", %s);' % (id, polar.js()));

	def updatePolars(self, polars):
		for id, polar in polars.items():
			self.script('updatePolar(%d, "#00ff00", %s);' % (id, polar.js()));

	def removePolars(self, ids):
		for id in ids:
			#self.script('removePolar(%d);' % id);
			self._polars.pop(id)

	def setMapStyle(self, lightness, saturation):
		self.script('setMapStyle(%d, %d)' % (lightness, saturation))

	def setPlaneStyle(self, data):
		iconSize, iconColor, trackWidth, trackColor = data
		trackColor = ('"%s"' % trackColor.name()) if trackColor else 'null'
		self.script('setPlaneStyle(%d, "%s");' % (iconSize, iconColor.name()))
		self.script('setTrackStyle(%d, %s)' % (trackWidth, trackColor))



