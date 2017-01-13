# -*- coding: utf-8 -*-


from multiprocessing import Process, Event, Queue
import sbs

from time import sleep #TEST
import os #TEST

class AbstractSource:
	def __init__(self, config):
		self._config = config
		self._queue = Queue()

		fmt = config.get('format', 'none')
		if fmt == 'sbs':
			self._config['handler'] = sbs.strToPoints
		else:
			raise Exception('Unknown format "%s"' % fmt)

	def start(self):
		self._stop = Event()
		self._proc = Process(target=self.run, args=(self._config,))
		self._proc.start()

	def join(self):
		if self._proc:
			self._proc.join()

	def dequeue(self):
		res = []
		while not self._queue.empty():
			data = self._queue.get()
			res += data

		return res

	def stop(self):
		if self._proc:
			self._stop.set()
			print 'pid', os.getpid(), self._proc.pid
			print 'alive', self._proc.is_alive()
			try:
				self._proc.join()
			except:
				pass
			print 'stopped ok'

