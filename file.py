#!/usr/bin/python

fileName=raw_input('Enter File Name:')
data=open(fileName,'r')
print data.read()
data.close()