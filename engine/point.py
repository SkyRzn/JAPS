# -*- coding: utf-8 -*-


from math import pi, sqrt, sin, cos, acos, atan2
from time import time


earth_r = 6371.0
rad = pi/180.0


class Point:
	def __init__(self, lat, lng, info = None, grad = False):
		if grad:
			self._lat = lat*rad
			self._lng = lng*rad
		else:
			self._lat = lat
			self._lng = lng
		self._info = info or {}
		self._info['timestamp'] = time()
		self._alt = self._info.get('alt', -10000)
		if self._alt:
			self._alt *= 0.3048

	def dist(self, other):
		return acos(sin(self._lat)*sin(other._lat) +
					cos(self._lat)*cos(other._lat) * cos(self._lng - other._lat)) * earth_r

	def azimuth(self, other):
		y = sin(other._lng-self._lng)*cos(other._lat)
		x = cos(self._lat)*sin(other._lat) - sin(self._lat)*cos(other._lat)*cos(other._lng-self._lng)
		res = atan2(y, x)
		return (res + pi*2) if (res < 0) else res

	def gazimuth(self, other):
		return self.azimuth(other)/rad

	def js(self):
		return '{lat:%f, lng:%f, alt:%d}' % (self.glat(), self.glng(), self._alt)

	def lat(self):
		return self._lat

	def lng(self):
		return self._lng

	def glat(self):
		return self._lat/rad

	def glng(self):
		return self._lng/rad

	def setInfo(self, info):
		self._info = info

	def info(self, field = None):
		if field:
			return self._info.get(field)
		return self._info

	def alt(self):
		return self._alt

	def __eq__(self, other):
		if not isinstance(other, Point):
			return False
		return self._lat == other._lat and self._lng == other._lng
