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


#choices = u'Chapman Cleese Gilliam Idle Jones Palin'.split()
choices	= listFiles = os.listdir('/')

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
    response = urwid.Text([u'You chose ', choice, u'\n'])
    done = urwid.Button(u'Ok')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response,
        urwid.AttrMap(done, None, focus_map='reversed')]))

def exit_program(button):
    raise urwid.ExitMainLoop()

main = urwid.Padding(menu(u'Pythons', choices), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
    align='center', width=('relative', 60),
    valign='middle', height=('relative', 60),
    min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()

