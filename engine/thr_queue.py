# -*- coding: utf-8 -*-


from multiprocessing import Process, Queue


class AbstractSource:
	def __init__(self):
		self._queue = Queue()
		self._proc = Process(target=run, args=(self._queue,))

	def start(self):
		self._proc.start()

	def join(self):
		self._proc.join()

	def dequeue(self):
		res = []
		while not self._queue.empty():
			data = self._queue.get_nowait()
			res += data
		return res

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()

    p.start()
    print q.get()    # prints "[42, None, 'hello']"
    p.join()
		self._stop = False
		self._queue = Queue()

#from time import sleep
#from threading import Thread
#from Queue import Queue
#from Queue import Empty as QueueEmpty


#class ThreadQueue(Thread):
	#def __init__(self):
		#Thread.__init__(self)
		#self._stop = False
		#self._queue = Queue()

	#def dequeue(self):
		#res = []
		#try:
			#data = self._queue.get_nowait()
			#res += data
		#except QueueEmpty:
			#pass
		#return res

	#def stop(self):
		#self._stop = True
