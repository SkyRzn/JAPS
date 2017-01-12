# -*- coding: utf-8 -*-


from abstract_source import AbstractSource

CHUNK_SIZE = 4096 * 100

class File(AbstractSource):
	def __init__(self, path, handler):
		self._eof = False
		f = open(path, 'r')

		AbstractSource.__init__(self, (handler, f))

	def run(self, handler, f):
		tail = ''
		while not self._isStopped():
			data = tail + f.read(CHUNK_SIZE)
			if not data:
				break

			res, tail = handler(data)
			self._queue.put(res)

		f.close()

		try:
			self._cConn.send('eof')
		except:
			pass

		self._cConn.close()

	def eof(self):
		if self._pConn.poll() and self._pConn.recv() == 'eof':
			self._eof = True
		return self._eof
