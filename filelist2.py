#!/usr/bin/env python
import os
import urwid


def create_walker_wid(path=None):
	# get filelist from path
	try:
		listFiles = os.listdir(path)
	except:
		path = '/'
		listFiles = os.listdir(path)
	# create empty list for widget list
	buttonList = []
	# create button list
	for oneFile in listFiles:
		buttonList.append(urwid.Button(oneFile))
	# pass  button list to simple walker
	simpleWalker = urwid.SimpleListWalker(buttonList)
	# return boxList
	return urwid.ListBox(simpleWalker)


def quit_on_q(key):
	if key == 'q':
		raise urwid.ExitMainLoop

loop = urwid.MainLoop(create_walker_wid(), unhandled_input=quit_on_q)
loop.run()

