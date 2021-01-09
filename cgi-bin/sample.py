#!/usr/bin/python
# -*- coding: utf-8 -*-

#import subprocess
import cgi
import cgitb
#import pyautogui
#import time

cgitb.enable()

print("Content-Type: text/html")
print()   

form = cgi.FieldStorage()

#time.sleep(3)
#pyautogui.typewrite(form["Sentence"].value, 0.25)
print(form["Sentence"].value)