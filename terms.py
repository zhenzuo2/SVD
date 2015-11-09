'''
Created on Sep 30, 2015

@author: mingruizhang
'''
from getdecom import getdecom
from norm import getnorm
import numpy


def useterm(num, Matrix):
    
    Z=getdecom(Matrix)
    
    sigma = Z[1]
    #print ("original sigma")
    #print (sigma)
    
    x=len(sigma.transpose())
    y=len(sigma)
    m=y
    
    if x <= y:
        m=x
    
    
    for i in range(m):
        if i>num-1:
            sigma[i][i]=0
    
    #print ("new sigma")
    #print (sigma)
    print('the length of sigma')
    print(len(sigma))
    
    vectorinvU=numpy.linalg.inv(Z[0])
    
    sigmainv=numpy.zeros((x, y))
    for i in range(num-1):
        sigmainv[i][i]=1/sigma[i][i]
        
    #sigmainv=sigmainv.transpose()
        
    #print ("1/sigma of Sigma")
    #print (sigmainv)
    
    vectorVT=numpy.dot(vectorinvU, Matrix)
    vectorVT=numpy.dot(sigmainv,vectorVT)
    
    
    o=len(Z[0].transpose())
    b=len(Z[0])
    zen=Z[0]
    for i in range(o):
        for j in range(b):
            if j > num-1:
                zen[i,j]=0
    
    M=numpy.dot(zen, sigma)
    M=numpy.dot(M,vectorVT)
    #print ("new restoration")
    #print (M)
    
    A=getnorm(Matrix)
    B=getnorm(Matrix - M)
    error=B/A
    error=error*100
    if error < 0.0000000001:
        error = 0
    
    print ("the error is")
    print (error, "%")
    return M

    