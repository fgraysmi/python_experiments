# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 13:26:05 2017

@author: frase
"""

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   fh.close()
finally:
    print("all done!")