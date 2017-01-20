#!/usr/bin/python
# -*- coding: utf-8 -*-


def load():
	f = open('dumps/uvd.dump.medv1', 'r')
	raw = bytearray(f.read())
	f.close()

	raw = raw[12582912 +538000 -200 + (22098*2*2):]

	m = []
	mlen = len(raw)/2
	print mlen
	for i in xrange(0, mlen, 2):
		m.append(raw[i] + raw[i+1]*256)
	return m


def graph():

	data = load()

	offs = 12582912 +538000 -200 + (22098*2*2)

	for i in range(10):
		print ''

	i = 0
	for y in range(120 * 2):
		val = data[i+offs] + data[i+1+offs]*256
		i += 2
		l = ''
		for x in range(int(float(val)/65536*160)):
			l += '*'
		print "%04d: %s" % ((y/2), l)


def pulse(m, i):
	high = (m[i] + m[i+1])/2
	if m[i-1] * 4 < high and m[i+2] * 4 < high:
		return (True, i if (m[i] > m[i+1]) else (i+1))
	return (False, 0)


def main():
	m = load()

	mlen = len(m)

	i = 1

	for i in xrange (1, mlen-400):
		p, n = pulse(m, i)
		if not p:
			continue
		rk1 = n

		p, n = pulse(m, i + 28)
		if not p:
			continue
		rk3 = n

		p, n = pulse(m, i + 28 + 17)
		if not p:
			continue
		rki1 = n

		p, n = pulse(m, i + 28 + 17 + 16)
		if not p:
			continue
		rki2 = n

		p, n = pulse(m, i + 28 + 17 + 16 + 24)
		if not p:
			continue
		rki3 = n

		print '----------', rk1
		b = m[rki3+8:]
		for i in range(20):
			d0 = b[i*16]
			d1 = b[i*16 + 8]

			d = 1 if d0 > d1 else 0

			d0 = b[320 + i*16]
			d1 = b[320 + i*16 + 8]
			dd = 1 if d0 > d1 else 0

			print d, dd


main()