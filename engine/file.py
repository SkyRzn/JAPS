# -*- coding: utf-8 -*-


from abstract_source import AbstractSource


CHUNK_SIZE = 4096 * 100


class File(AbstractSource):
	def __init__(self, config):
		AbstractSource.__init__(self, config)

	def run(self, config):
		try:
			path = config['path']
			handler = config['handler']
		except:
			raise Exception('File config error')

		f = open(path, 'r')

		tail = ''
		while not self._stop.is_set():
			data = tail + f.read(CHUNK_SIZE)
			if not data:
				break

			res, tail = handler(data)
			self._queue.put(res)

		print 'file close'
		f.close()
		print 'file exit'

