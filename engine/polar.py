# -*- coding: utf-8 -*-


import json


class Polar:
	def __init__(self, id, home, sources, callback = None):
		self._id = id
		self._data = {}
		self._home = home
		self._maxDist = 0
		self._sources = set(sources)
		self._callback = callback

	def setHome(self, home):
		self._home = home
		points = [p[0] for p in self._data.values()]
		self._data = {}
		self.addPoints(points)

	def loadFromFile(self, fn):
		f = open(fn, 'r')
		self._data = json.load(f)
		f.close()

	def saveToFile(self, fn):
		f = open(fn, 'w')
		json.save(f, self._data)
		f.close()

	def update(self, points):
		updated = False

		if not self._home:
			return

		for point in points:
			az = int(self._home.gazimuth(point))
			dt = self._home.dist(point)
			p_prev, dt_prev = self._data.get(az, (None, 0))
			if dt > dt_prev:
				self._data[az] = (point, dt)
				self._maxDist = max(self._maxDist, dt)
				updated = True

		if self._callback and updated:
			self._callback(self)
		return updated

	def addSource(self, source):
		self._sources.add(source)

	def sources(self):
		return self._sources

	def maxDistance(self):
		return self._maxDist

	def boundPoints(self):
		if not self._home:
			return []

		res = []

		for az in range(360):
			res.append(self._data.get(az, (self._home, 0)))
		return res

	def js(self):
		res = [self._home.js()]

		points = self.boundPoints()

		for point, dist in points:
			res.append(point.js())

		return '[%s]' % (','.join(res));

	def id(self):
		return self._id