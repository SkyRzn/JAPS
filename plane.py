# -*- coding: utf-8 -*-


import json
from time import time


class Plane:
	def __init__(self, points):
		self._points = []
		self._pointsCount = 0
		self._azimuth = 0
		self._code = points[0].info('code')
		self.addPoints(points)

	def addPoints(self, points):
		self._lastSeen = time()
		self._points += points
		self._pointsCount += len(points)
		if self._pointsCount > 1:
			self._azimuth = self._points[-2].gazimuth(self._points[-1])

	def lastSeen(self):
		return self._lastSeen

	def code(self):
		return self._code

	def pointsCount(self):
		return self._pointsCount

	def jsTrack(self, fromPoint = 0):
		if fromPoint < 0:
			fromPoint = 0
		return '[%s]' % (','.join([p.js() for p in self._points[fromPoint:]]))

	def jsCurrentPosition(self):
		return self._points[-1].js()

	def jsInfo(self):
		res = {'azimuth': self._azimuth}
		return res
