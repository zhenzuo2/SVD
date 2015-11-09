'''
Created on Sep 25, 2015

@author: mingruizhang
'''
import numpy
from math import sqrt

"""
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
print "A:"
print(Matrix)
"""

#"""
Matrix = numpy.matrix( ((1,2,3,1),(4,5,6,2),(7,8,9,3)) )
print "A:"
print(Matrix)

#"""


MatrixT=Matrix.transpose()
print "A*:"
print(MatrixT)

MatrixU=numpy.dot(Matrix, MatrixT)
print "AA*:"
print(MatrixU)

MatrixV=numpy.dot(MatrixT, Matrix)
print "A*A:"
print(MatrixV)

valueU=numpy.linalg.eig(MatrixU)[0]
print "Eigenvalue of U:"
print(valueU)
vectorU=numpy.linalg.eig(MatrixU)[1]
print "Eigenvector of U:"
print(vectorU)

valueV=numpy.linalg.eig(MatrixV)[0]
print "Eigenvalue of V:"
print(valueV)
vectorV=numpy.linalg.eig(MatrixV)[1]
print "Eigenvector of V:"
print(vectorV)

x=len(valueU)
y=len(valueV)
if x<=y:
    Singular=valueU
else:
    Singular=valueV


m=len(Singular)
for i in range(m):
    if Singular[i] < 0.0000000001:
        Singular[i]=0

Singular=numpy.sqrt(Singular)
print "singluar value:"
print(Singular)


sigma=numpy.zeros( (x, y) )
for i in range(x):
    sigma[i][i]=Singular[i]
            
print "sigma:"
print(sigma)

vectorVT= numpy.transpose(vectorV)
print "vectorVT:"
print(vectorVT)

M=numpy.dot(vectorU, sigma)
M=numpy.dot(M, vectorVT)
print "Restore:"
print(M)

print "U E V*:"
print(vectorU)
print(sigma)
print( vectorVT)