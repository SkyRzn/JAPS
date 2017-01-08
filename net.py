#!/usr/bin/python
# -*- coding: utf-8 -*-


import socket
from threading import Thread, currentThread
from time import sleep
from Queue import Queue
from Queue import Empty as QueueEmpty


class Net(Thread):
	def __init__(self, addr, port, handler):
		Thread.__init__(self)
		self._stop = False
		self._addr = addr
		self._port = port
		self._handler = handler
		self._queue = Queue()

	def run(self):
		print currentThread()
		BUF_LEN = 1024

		print 'LISTEN TO %s:%d' % (self._addr, self._port)

		while not self._stop:
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.connect((self._addr, self._port))
			except socket.error, exc:
				time.sleep(5)
				print '.',
				continue

			print 'ok'

			sock.setblocking(0)

			while not self._stop:
				try:
					data = sock.recv(BUF_LEN)
					if data:
						res = self._handler(data)
						self._queue.put(res)
					sleep(0.1)
				except socket.error, exc:
					if exc.errno != 11:
						break
			sock.close()

	def stop(self):
		self._stop = True

	def dequeue(self):
		res = []
		try:
			data = self._queue.get_nowait()
			res += data
		except QueueEmpty:
			pass
		return res

