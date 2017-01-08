# -*- coding: utf-8 -*-


from time import time
from PyQt4.QtCore import *

from point import Point
from polar import Polar
from plane import Plane


PLANE_TIMEOUT = 60


class Dispatcher(QObject):
	planesAdded = pyqtSignal(dict)
	planesUpdated = pyqtSignal(dict)
	planesRemoved = pyqtSignal(list)

	polarsAdded = pyqtSignal(dict)
	polarsUpdated = pyqtSignal(dict)

	def __init__(self, parent = None):
		QObject.__init__(self, parent)
		self._queues = {}
		self._polars = {}
		self._planes = {}
		self._home = None

		self._timer = QTimer(self)
		self._timer.timeout.connect(self.renew)
		self._timer.start(100)

	def setHome(self, point):
		if self._home == point:
			return
		self._home = point
		for polar in self._polars.values():
			polar.setHome(point)
		self.emit(SIGNAL('updatePolars'))

	def renew(self):

		####### prepare points
		planesPoints = {}
		polarsPoints = {}

		for qid, queue in self._queues.items():
			points = queue.dequeue()
			if not points:
				continue

			for point in points:
				code = point.info('code')
				if code not in planesPoints:
					planesPoints[code] = []
				planesPoints[code].append(point)

				if qid not in polarsPoints:
					polarsPoints[qid] = []
				polarsPoints[qid].append(point)

		####### handle planes
		added = {}
		updated = {}

		for code, points in planesPoints.items():
			if code not in self._planes:
				self._planes[code] = Plane(points)
				added[code] = self._planes[code]
			else:
				updated[code] = (self._planes[code], self._planes[code].pointsCount())
				self._planes[code].addPoints(points)

		if added:
			self.planesAdded.emit(added)
		if updated:
			self.planesUpdated.emit(updated)


		####### handle polars
		added = {}
		updated = {}

		for qid, points in polarsPoints.items():
			if qid not in self._polars:
				self._polars[qid] = Polar(self._home, points)
				added[qid] = self._polars[qid]
			else:
				if self._polars[qid].addPoints(points):
					updated[qid] = self._polars[qid]

		if added:
			self.polarsAdded.emit(added)
		if updated:
			self.polarsUpdated.emit(updated)

		####### remove timed out planes
		t = time()
		removed = []
		for id, plane in self._planes.items():
			if t > plane.lastSeen() + PLANE_TIMEOUT:
				self._planes.pop(id)
				removed.append(id)
		self.planesRemoved.emit(removed)

	def addSourceQueue(self, id, queue):
		self._queues[id] = queue

	def removeSourceQueue(self, id):
		if id in self._queues:
			self._queues.pop(id)

	def planes(self):
		return self._planes


