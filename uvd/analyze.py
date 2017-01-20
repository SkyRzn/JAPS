#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Browser(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.resize(1024, 768)

		f = open('/tmp/uvd.dump.medv1', 'r')
		self.data = bytearray(f.read())
		f.close()

		self.offs = 12582912 +538000 -200

		#with open('/tmp/uvd.dump', 'r') as f:
			#f.write

	def lg(self, val):
		i = 0
		while val:
			i += 1
			val = val >> 1
		return i

	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		mcol = 0
		mval = 0
		i = 0
		prev = 0
		for i in range(0, 100000, 2):
			val = self.data[i+self.offs] + self.data[i+1+self.offs]*256
			if val > 16000:
				val = i/4.0
				if val-prev == 0.5:
					continue
				print val - prev
				prev = val

		for y in range(50):
			i = 0
			for x in range(1024):
				#i = (x + y*1024)*2
				val = self.data[i+self.offs] + self.data[i+1+self.offs]*256
				val -= 30000
				if val < 0:
					val = 0
				col = self.lg(val)*16
				if col > 255:
					col = 255
				if mcol < col:
					mcol = col
				if mval < val:
					mval = val

				qp.setPen(QColor(0, col, 3))
				qp.drawPoint(x, y)
				i += 2
		qp.end()
		print mcol, mval

	#def mouseReleaseEvent(self, event):
		#if self.offs + 1024*768*2 > len(self.data):
			#print 'STOOOOOOOOP'
			#return

		#self.offs += 1024*768*2
		#print self.offs
		#self.update()

	def mouseMoveEvent(self, event):
		x = event.x()
		y = event.y()
		print (x + y*1024)*2

def main():
	f = open('/tmp/uvd.dump.old', 'r')
	data = bytearray(f.read())
	f.close()

	offs = 323320+1024+1024+800+100-100
	prev = 0
	for i in range(0, 160000, 2):
		val = data[i+offs] + data[i+1+offs]*256
		if val > 18000:
			val = i/4.0
			if val-prev == 0.5:
				continue
			print val - prev
			prev = val


if __name__ == '__main__':
	#main()
	app = QApplication(sys.argv)

	main = Browser()
	main.show()
	sys.exit(app.exec_())



