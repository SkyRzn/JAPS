#!/usr/bin/python
# -*- coding: utf-8 -*-


from math import pi, sqrt, sin, cos, acos, atan2


earth_r = 6371
rad = pi/180

def grad2rad(p):
	return [p[0]*rad, p[1]*rad]

def rad2grad(p):
	return [p[0]/rad, p[1]/rad]

def dist(a, b):
	return acos(sin(a[0])*sin(b[0]) + cos(a[0])*cos(b[0])*cos(a[1] - b[1]))*earth_r

def azimuth(a, b):
	y = sin(b[1]-a[1])*cos(b[0])
	x = cos(a[0])*sin(b[0]) - sin(a[0])*cos(b[0])*cos(b[1]-a[1])
	res = atan2(y, x)
	return (res + pi*2) if (res < 0) else res

def calc_flower(home, points):
	home = grad2rad(home)
	points = map(grad2rad, points)

	petals = {}
	for point in points:
		az = int(azimuth(home, point)/rad)
		dt = dist(home, point)
		dt_prev, p_prev = petals.get(az, (0, None))
		if dt > dt_prev:
			petals[az] = (dt, point)

	res = []
	dt_max = 0
	first = True
	for a in range(360):
		dt, p = petals.get(a, (0, home))
		if dt == 0 and first:
			first = False
			#FIXME ^^^^
		res.append(rad2grad(p))
		if (dt > dt_max):
			dt_max = dt
	print dt_max
	return res

def py2js(p):
	return '{lat:%f, lng:%f}' % (p[0], p[1])


def load_lines(fn):
	f = open(fn, 'r')
	lines = f.readlines()
	f.close()

	res = []
	for line in lines:
		line = line.strip()
		if line:
			res.append(line)
	return res


def import_from_mybs(fn):
	lines = load_lines(fn)

	res = []

	for line in lines:
		try:
			vals = line.split(',')
			lat = vals[15]
			lng = vals[16]
		except Exception as exc:
			print line

		if lat and lng:
			lat, lng = float(lat), float(lng)
			if lat and lng:
				res.append([lat, lng])
			if lat > 60:
				print '!!!!!!!!!!!', line

	return res






