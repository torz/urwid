#!/usr/bin/env python
import os
import urwid

currentPath = '/'
choices = os.listdir(currentPath)

def update_cp_choices(choice):
    global currentPath
    global choices
    if choice == '..':
        currentPath = os.path.dirname(currentPath)
    else:
        currentPath = os.path.join(currentPath, choice)
    if os.path.isdir(currentPath):
        choices = os.listdir(currentPath)
    if currentPath != '/':
        choices.insert(0, '..')

def menu(title, choices):
    global currentPath
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        if os.path.isdir(os.path.join(currentPath, c)):
            urwid.connect_signal(button, 'click', update_choices, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def exit_program(button):
    if button == 'q':
        raise urwid.ExitMainLoop()

def update_choices(button, choice):
    global choices
    update_cp_choices(choice)
    main.original_widget = menu(title, choices)

title = u'File Browser - Press q to quit'
main = urwid.Padding(menu(title, choices), left=9, right=9)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
    align='center', width=('relative', 60),
    valign='middle', height=('relative', 60),
    min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')], unhandled_input=exit_program).run()
