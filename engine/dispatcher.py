# -*- coding: utf-8 -*-


from input import Input
from tracker import Tracker
from polar import Polar
import json


#class DispatcherError(Exception):
    #pass


class Dispatcher:
	def __init__(self):
		self._input = Input()
		self._trackers = {}
		self._polars = {}

	def update(self):
		data = self._input.getPoints()

		for id, points in data.items():
			for tracker in self._trackers.values():
				if id in tracker.sources():
					tracker.update(points)

			for polar in self._polars.values():
				if id in polar.sources():
					polar.update(points)

	def addTracker(self, id, sources, timeout, callback = None):
		self._trackers[id] = Tracker(id, sources, timeout, callback)
		return self._trackers[id]

	def removeTracker(self, id):
		if id in self._trackers:
			del self._trackers[id]

	def addPolar(self, id, home, sources, callback = None):
		self._polars[id] = Polar(id, home, sources, callback)
		return self._polars[id]

	def removePolar(self, id):
		if id in self._polars:
			del self._polars[id]

	def reset(self):
		self._input.clean()

	def input(self):
		return self._input

	def setCallbacks(self, tracker, polar):
		self._trackerCallback

	def start(self):
		self._input.startAll()

	def stop(self):
		self._input.stopAll()




config = """{
"input": {
	"radar1": { "type": "group",
		"items": {
			"net": {"type": "net", "format": "sbs", "address": "localhost", "port": 30003},
			"file": {"type": "file", "format": "sbs", "path": "2017-01-08.txt"}
		}
	},
	"radar2": {"type": "net", "format": "sbs", "address": "192.168.0.1", "port": 30003}
},

"polars": {
	"radar1": {
		"sources": ["radar1"],
		"period": "daily"
	},
	"radar2": {
		"sources": ["radar2"],
		"period": "daily",
		"log": "/tmp/radar2_%s.polar"
	}
},

"trackers": {
	"all": {
		"sources": ["radar1", "radar2"],
		"timeout": 3600
	}
},

"output": {
	"standard": {
		"direction": "in",
		"port": 10000
	}
}

}"""


