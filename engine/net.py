# -*- coding: utf-8 -*-


import socket
from select import select
from abstract_source import AbstractSource
from time import sleep


BUF_LEN = 4096*20
DEFAULT_TIMEOUT = 5


class Net(AbstractSource):
	def __init__(self, config):

		AbstractSource.__init__(self, config)

	def run(self, config):
		try:
			addr = config['address']
			port = int(config['port'])
			handler = config['handler']
		except:
			raise Exception('Net config error')
		timeout = int(config.get('timeout', DEFAULT_TIMEOUT))

		wait = 0
		while not self._stop.is_set():
			wait += 1
			if wait == 1:
				try:
					sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					sock.connect((addr, port))
				except socket.error, exc:
					sleep(0.1)
					continue
			else:
				if wait >= timeout*10:
					wait = 0
				continue

			sock.setblocking(0)

			tail = ''
			while not self._stop.is_set():
				try:
					select([sock], [],[])
					data = tail + sock.recv(BUF_LEN)

					res, tail = handler(data)
					self._queue.put(res)
				except socket.error, exc:
					break
			sock.close()

