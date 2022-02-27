from os import path
import os
import time
import shutil

yes = "yes"

sure = input("Are U sure to Uninstall Discord app? 'yes' To remove 'no' to cancel: \n ")
if(yes==sure):
    print("Deleting Discord App... Wait.. Seconds")
    time.sleep(7)
    dumps_dir = path.expandvars(r'%LOCALAPPDATA%\Discord')
    shutil.rmtree(dumps_dir)
    print("Uninstalled successfully!")
else:
    print("Uninstall Discord Cancelled!")
    time.sleep(3)









