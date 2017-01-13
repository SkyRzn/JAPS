# -*- coding: utf-8 -*-


from plane import Plane
from time import time


DEFAULT_TIMEOUT = 3600


class TrackerError(Exception):
    pass


class Tracker:
	def __init__(self, id, sources, timeout, callback = None):
		self._id = id
		self._planes = {}
		self._sources = set(sources)
		self._timeout = timeout
		self._callback = callback

	def update(self, points):
		planes = {}
		for point in points:
			id = point.info('code')
			if not id:
				continue

			if id not in planes:
				planes[id] = []

			planes[id].append(point)

		added = {}
		updated = {}
		removed = {}

		for id, points in planes.items():
			if id not in self._planes:
				self._planes[id] = Plane(points)
				added[id] = self._planes[id]
			else:
				updated[id] = (self._planes[id], self._planes[id].pointsCount())
				self._planes[id].addPoints(points)

		t = time()
		for id, plane in self._planes.items():
			if plane.lastSeen() + self._timeout <= t:
				removed[id] = plane
				del self._planes[id]

		if self._callback and (added or updated or removed):
			self._callback(added, updated, removed)

	def addSource(self, source):
		if not source:
			raise TrackerError('Source is null')
		self._sources.add(source)

	def sources(self):
		return self._sources

	def setTimeout(self, timeout):
		self._timeout = timeout

	def timeout(self):
		return timeout

	def setConfig(self, conf):
		self._sources = set(conf.get('sources', []))
		self._timeout = conf.get('timeout', DEFAULT_TIMEOUT)

	def id(self):
		return self._id

	def plane(self, id):
		return self._planes.get(id)

	def planes(self):
		return self._planes


