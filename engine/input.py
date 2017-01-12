# -*- coding: utf-8 -*-


from net import Net
from file import File
import sbs


class InputError(Exception):
    pass

class Input:
	def __init__(self):
		self._sources = {}

	def addGroup(self, name):
		if name in self._sources:
			raise  InputError('Name "%s" is already used' % name)
		self._sources[name] = {'type': 'group', 'items': {}}

	def addSource(self, group, name, data):
		root = self._sources
		if group != None:
			if group not in self._sources:
				raise InputError('Group "%s" is not found' % group)
			root = self._sources[group]
			if root['type'] != 'group':
				raise InputError('"%s" is not group item' % group)
			root = root['items']

		if name in root:
			raise InputError('Name "%s" is already used' % name)

		type_ = data['type']
		fmt = data['format']

		if fmt == 'sbs':
			handler = sbs.strToPoints
		else:
			raise InputError('Unknown format "%s"' % fmt)

		if type_ == 'net':
			addr = data['address']
			port = int(data['port'])
			source = Net(addr, port, handler)
			type_ = 'qsource'
		elif type_ == 'file':
			source = File(data['path'], handler)
			type_ = 'fsource'
		else:
			raise InputError('Unknown source type "%s"' % type_)

		root[name] = {'type': 'qsource', 'source': source}

		return source

	def _getSourceData(self, item):
		return item['source'].dequeue()

	def getPoints(self):
		res = {}
		for id, item in self._sources.items():
			points = []
			if item['type'] == 'group':
				for iid, iitem in item['items'].items():
					points += self._getSourceData(iitem)
			else:
				points += self._getSourceData(item)
			res[id] = points
		return res

	def startAll(self):
		items = self.sources()
		for item in items.values():
			item['source'].start()

	def stopAll(self):
		items = self.sources()
		for item in items.values():
			item['source'].stop()

	def sources(self):
		res = {}
		for id, item in self._sources.items():
			if item['type'] == 'group':
				res.update(item['items'])
			else:
				res[id] = item
		return res

	def clean(self):
		self.stopAll()
		self._sources = {}




