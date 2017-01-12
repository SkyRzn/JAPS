#!/usr/bin/python


from os import listdir, system


for fn in listdir('.'):
	if fn.endswith('.ui'):
		print '...%s' % fn
		fn = fn[:-3]
		system('pyuic4 %s.ui > %s_ui.py' % (fn, fn))

system('pyrcc4 ../resources/rsc.qrc > rsc_rc.py')
