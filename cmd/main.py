#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
sys.path.insert(0,'..')

from engine.dispatcher import Dispatcher
import json, signal


from time import sleep #TEST


def trcb(added, updated, removed):
	print added, updated, removed

def main():
	argc = len(sys.argv)
	if argc < 2 or argc > 3:
		print 'Usage: %s config_file [sleep_time]' % sys.argv[0]
		print '\tconfig_file - path to configuration file'
		print '\tsleep_time - time between requests in seconds'
		return

	sleepTime = 0.1
	if argc == 3:
		try:
			sleepTime = float(sys.argv[2])
		except:
			print 'Sleep_time should be float type'

	with open(sys.argv[1], 'r') as f:
		config = json.load(f)

	dispatcher = Dispatcher()
	dispatcher.setConfig(config)

	def sigint_handler(signal_, frame):
		print '!!!!!!!!!!!!!!!!!!!'
		signal.signal(signal.SIGINT, signal.SIG_IGN)
		print '!!!!!!!!!!!!!!!!!!!22222222222222222222222'
		dispatcher.stop()
		print 'Interrupted'
		sys.exit(0)

	signal.signal(signal.SIGINT, sigint_handler)

	dispatcher.addTracker('test', ['radar_group1'], 10, trcb)

	dispatcher.start()

	cnt = 0
	while True:
		if not dispatcher.update():
			sleep(sleepTime)
		cnt += 1
		if cnt>10:
			sys.exit(0)

	dispatcher.stop()

main()

