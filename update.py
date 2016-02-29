# This is my python script to update my website with jemdoc

import os

files = ['index', 'biography', 'research']

for i in files:
	os.system('python jemdoc.py '+i)