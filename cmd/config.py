#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
sys.path.insert(0,'..')

from engine.input import Input
from time import sleep
import json


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

"plane_tracking": {
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
print json.loads(config)


def main():
	inp = Input()

	inp.addGroup('hui')

	data = {'type':'file','format':'sbs','path':'2017-01-08.txt'}
	fsrc = inp.addSource('hui', 'pizda', data)

	data = {'type':'net','format':'sbs','address':'localhost', 'port':10000}
	nsrc = inp.addSource('hui', 'djigurda', data)

	nsrc.start()
	fsrc.start()

	i = 0
	while 1:
		data = inp.getPoints()
		for p in data['hui']:
			print p.glat(), p.glng()

		sleep(1)

		i += 1
		if (i == 2):
			fsrc.stop()

	nsrc.join()

#main()

