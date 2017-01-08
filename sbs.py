# -*- coding: utf-8 -*-


from point import Point
import socket


def lineToPoint(line):
	vals = line.strip().split(',')

	if len(vals) != 22:
		return None

	fields = ('hdr', 'type', '2', '3', 'code', '5',
			'time1', 'time2', '8', '9', 'flight',
			'alt', 'speed', 'track', 'lat', 'lng',
			'vr', 'identity', 'alert', 'emergency', 'spi', 'ground')


	types = {'type': int, 'lat': float, 'lng': float, 'alt': float, 'speed': float}

	info = dict(zip(fields, vals))

	for k, v in types.items():
		try:
			info[k] = v(info[k])
		except:
			info[k] = 0

	lat = info.pop('lat')
	lng = info.pop('lng')
	if not (lat and lng and info['code']):
		return None

	return Point(lat, lng, info = info, grad = True)

def strToPoints(data):
	lines = data.split('\n')
	res = []

	for line in lines:
		p = lineToPoint(line)

		if p:
			res.append(p)

	return res


def loadFromFile(fn):
	f = open(fn, 'r')
	lines = f.read()
	f.close()
	return strToPoints(lines)



