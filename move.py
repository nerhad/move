from multiprocessing.connection import wait
import os
import shutil
import easygui
from easygui import *
from sre_constants import SUCCESS

Images = ".jpg", ".jpeg", ".png", ".webp", "JPG"
Videos = '.mp4', '.mov', '.avi'
Documents = '.txt', '.docx', '.dox', '.pdf'

text = "Select wich files you want to move"
title = "Move program"
choices = Images, Videos, Documents

def kill_function():
    exit()

output = multchoicebox(text, title, choices)
if output == None:
    kill_function()
    
sourcepath = easygui.diropenbox('Location?')
if sourcepath == None:
    kill_function()

sourcefiles = os.listdir(sourcepath)

destinationpath = easygui.diropenbox('Destination!')

for file in sourcefiles:
    if file.endswith(tuple(output[0])):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
        if SUCCESS:
           print("OK!", file)
        else:
            print('sorry somthing is wrong this file is corupt', file)
            break

msgbox("ALL files have been transferd")
