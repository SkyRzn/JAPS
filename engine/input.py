# -*- coding: utf-8 -*-


from net import Net
from file import File
import sbs


class InputError(Exception):
    pass

class Input:
	def __init__(self, config = None):
		self._sources = {}
		if config:
			self.setConfig(config)

	def addGroup(self, name):
		if name in self._sources:
			raise  InputError('Name "%s" is already used' % name)
		self._sources[name] = {'type': 'group', 'sources': {}}

	def addSource(self, group, name, config):
		root = self._sources
		if group != None:
			if group not in self._sources:
				raise InputError('Group "%s" is not found' % group)
			root = self._sources[group]
			if root['type'] != 'group':
				raise InputError('"%s" is not group item' % group)
			root = root['sources']

		if name in root:
			raise InputError('Name "%s" is already used' % name)

		type_ = config['type']

		if type_ == 'net':
			source = Net(config)
		elif type_ == 'file':
			source = File(config)
		else:
			raise InputError('Unknown source type "%s"' % type_)

		root[name] = {'type': 'qsource', 'source': source}

		return source

	def _getSourceData(self, source):
		return source['source'].dequeue()

	def getPoints(self):
		res = {}
		for id, source in self._sources.items():
			points = []
			if source['type'] == 'group':
				for source_ in source['sources'].values():
					points += self._getSourceData(source_)
			else:
				points += self._getSourceData(source)
			if points:
				res[id] = points
		return res

	def start(self):
		sources = self.sources()
		for source in sources.values():
			source['source'].start()

	def stop(self):
		sources = self.sources()
		for id, source in sources.items():
			print '&&&&&&&&&&&&&&&&&&', id
			source['source'].stop()

	def sources(self): #FIXME не надо смешивать источники из разных групп.
		res = {}
		for id, source in self._sources.items():
			if source['type'] == 'group':
				res.update(source['sources'])
			else:
				res[id] = source
		return res

	def setConfig(self, config):
		for id, source in config.items():
			if source['type'] == 'group':
				self.addGroup(id)
				for id_, source_ in source['sources'].items():
					self.addSource(id, id_, source_)
			else:
				self.addSource(None, id, source)




