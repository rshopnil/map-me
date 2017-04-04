#! /usr/bin/env/python
# script to launch a map in the browser using the cmd line arguments
# clipboard text instead of cmd line args will do too!

import sys,webbrowser,pyperclip

if(len(sys.argv)>1):
    addr= ' '.join(sys.argv[1:])

else:
    addr= pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+ addr)
