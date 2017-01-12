# -*- coding: utf-8 -*-


#from time import sleep
from threading import Thread
from Queue import Queue
from Queue import Empty as QueueEmpty


class File(Thread):
	def __init__(self, path, handler):
		Thread.__init__(self)
		self._stop = False
		self._handler = handler
		self._queue = Queue()
		self._readed = False

		self._f = open(path, 'r')

	def run(self):
		while data = f.readline():
			if self._stop:
				break
			res = self._handler(data)
			self._queue.put(res)
		f.close()

	def dequeue(self):
		res = []
		try:
			data = self._queue.get_nowait()
			res += data
		except QueueEmpty:
			pass
		return res
	
	def stop(self):
		self._stop = True
