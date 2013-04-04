#!/usr/bin/env python
import os
import urwid

currentPath = '/'
dirList = []

def update_curent_path(nextPath):
    global currentPath
    if nextPath == '..':
        currentPath = os.path.dirname(currentPath)
    else:
        currentPath = os.path.join(currentPath, nextPath)
    
def update_dir_list():
    global currentPath
    global dirList
    try:
        dirList = os.listdir(currentPath)
    except:
        currentPath = '/'
        dirList = os.listdir(currentPath)
    if currentPath != '/':
        dirList.append('..')

def create_buttons():
    global dirList
    # create empty list for widget list
    buttonList = []
    # create button list
    for oneFile in dirList:
        button = urwid.Button(oneFile)
        urwid.connect_signal(button, 'click', create_main_wid, oneFile)
        buttonList.append(button)
    # pass  button list to simple walker
    return urwid.ListBox(urwid.SimpleListWalker(buttonList))

def quit_on_q(self, key):
    if key == 'q':
        raise urwid.ExitMainLoop

def main():
    update_dir_list()

    loop = urwid.MainLoop(mainWid, unhandled_input=quit_on_q)
    loop.run()

if __name__ == '__main__':
    main()
