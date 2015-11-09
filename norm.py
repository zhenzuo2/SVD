'''
Created on Oct 6, 2015

@author: mingruizhang
'''


import numpy


def getnorm(Matrix):
    
    Matrix= numpy.absolute(Matrix)
    norm = numpy.sum(Matrix)
    #print "norm is"
    #print norm
    
    return norm


L= numpy.matrix( ((1,2,3),(4,5,6),(7,8,9)) )
getnorm(L)
