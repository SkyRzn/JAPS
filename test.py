#!/usr/bin/python
# -*- coding: utf-8 -*-


from engine.dispatcher import Dispatcher
from engine.point import Point
from time import sleep
import json

def callback(added, updated, removed):
	print 'added: %d' % len(added)
	for id in added:
		print '\t', id
	print 'updated: %d' % len(updated)
	for id in updated:
		print '\t', id
	print 'removed: %d' % len(removed)
	for id in removed:
		print '\t', id

def callbackPolar(polar):
	print 'POLAR UPDATED: %f' % polar.maxDistance()

def main():
	disp = Dispatcher()
	inp = disp.input()

	inp.addGroup('hui')

	#data = {'type':'file','format':'sbs','path':'2017-01-08.txt'}
	#inp.addSource('hui', 'pizda', data)

	data = {'type':'net','format':'sbs','address':'localhost', 'port':30003}
	inp.addSource('hui', 'djigurda', data)

	home = Point(54.613579, 39.815831, grad=True)
	disp.addTracker('lol', ['hui'], 5, callback)
	disp.addPolar('lol', home, ['hui'], callbackPolar)

	inp.startAll()

	i = 0
	for i in range(15):
		disp.update()
		#print len(disp._trackers['lol']._planes)
		#for plane in disp._trackers['lol']._planes.values():
			#print plane.code(), plane.pointsCount()

		sleep(1)


	inp.stopAll()

main()

