# This is my python script to update my website with jemdoc
import sys
import os
print sys.version
files = ['index', 'research', 'teaching', 'talk_videos']

for i in files:
	os.system('C:\Python27\python.exe jemdoc.py '+i)
