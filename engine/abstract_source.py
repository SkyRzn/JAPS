# -*- coding: utf-8 -*-


from multiprocessing import Process, Event, Queue


class AbstractSource:
	def __init__(self, args):
		self._queue = Queue()
		#self._pConn, self._cConn = Pipe()

		self._proc = Process(target=self.run, args=args)
		self._stop = Event()

	def start(self):
		self._proc.start()

	def join(self):
		self._proc.join()

	def dequeue(self):
		res = []
		while not self._queue.empty():
			data = self._queue.get()
			res += data

		return res

	def stop(self):
		self._stop.set()
		self._proc.join()

