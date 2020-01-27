#!/usr/bin/python

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

i = 1
for root, dirs, files in os.walk(dir_path):
    for file in files:

        if not (file.endswith('.jar') or file.endswith('.py')):
            print root+'/'+str(file)
            i = i + 1
            #os.rename(root+'/'+str(file),root+'/'+str(file)+str(i))

            oldext = os.path.splitext(file)[1]
            os.rename(root+'/'+str(file) , root+'/'+str(os.path.splitext(file)[0])+str(i) + oldext)
