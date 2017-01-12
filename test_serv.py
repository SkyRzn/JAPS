#!/usr/bin/python
# -*- coding: utf-8 -*-



import socket
import sys
from time import sleep

while 1:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	server_address = ('localhost', 30003)
	print >>sys.stderr, 'starting up on %s port %s' % server_address
	sock.bind(server_address)

	sock.listen(1)

	while True:
		print >>sys.stderr, 'waiting for a connection'
		connection, client_address = sock.accept()

		f = open('2017-01-08.txt', 'r')

		try:
			print >>sys.stderr, 'connection from', client_address

			while True:
				line = f.readline()
				if not line:
					break
				connection.sendall(line)
				sleep(0.01)
		except socket.error:
			pass
		finally:
			connection.close()

