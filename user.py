'''
Created on Sep 30, 2015

@author: mingruizhang
'''

from getdecom import getdecom
import numpy

print("What is the size of the matrix you want?")
row = input("How many rows do you want?")
row= int(row)
column = input("How many column do you want?")
column=int(column)
Matrix=numpy.zeros((row,column))
for i in range(row):
    for j in range(column):
        a = "Which number do you want for row {} and column {}: "
        i=i+1
        j=j+1
        b=a.format(i,j)
        i=i-1
        j=j-1
        Matrix[i][j]=input(b)


Z=getdecom( Matrix )

print "This is U"
print Z[0]