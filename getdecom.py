'''
Created on Sep 30, 2015

@author: mingruizhang
'''
import numpy





def getdecom(Matrix):
    
    #print ("A:")
    #print(Matrix)
    
    x=len(Matrix)
    y=len(Matrix.transpose())
    #print x, y
           
    MatrixT=Matrix.transpose()
    #print ("A*:")
    #print(MatrixT)

    MatrixU=numpy.dot(Matrix, MatrixT)
    #print ("AA*:")
    #print(MatrixU)

    MatrixV=numpy.dot(MatrixT, Matrix)
    #print ("A*A:")
    #print(MatrixV)

    valueU=numpy.linalg.eig(MatrixU)[0]
    #print ("Eigenvalue of U:")
    #print(valueU)
    

    vectorU=numpy.linalg.eig(MatrixU)[1]
    #print ("Eigenvector of U:")
    #print(vectorU)

    '''
    valueV=numpy.linalg.eig(MatrixV)[0]
    print "Eigenvalue of V:"
    print(valueV)
    vectorV=numpy.linalg.eig(MatrixV)[1]
    print "Eigenvector of V:"
    print(vectorV)
    '''

    Singu=valueU
    z=len(Singu)
    Singular=[None]*z
    for i in range(z):
        Singular[i]=Singu[i].real
    print(Singular)
    print(type(Singular[0]))
    
    flag=0
    for i in range(z):
        if Singular[i] < 0.000001:
            Singular[i]=0
        if Singular[i]==0:
            flag=flag+1
            
    temp=numpy.zeros(z-flag)  
    for i in range(z-flag):
        temp[i]=Singular[i]   
    
    Singular=temp
    m=len(Singular)
    print(m)
    #print ("sorted Singular")
    #print (Singular)
    

    Singular=numpy.sqrt(Singular)
    #print ("singluar value:")
    #print(Singular)


    sigma=numpy.zeros( (x, y) )
    for i in range(m):
        sigma[i][i]=Singular[i]
            
    #print ("sigma:")
    #print(sigma)
    
    vectorinvU=numpy.linalg.inv(vectorU)
    #print ("inverse of U")
    #print (vectorinvU)
    
    sigmainv=numpy.zeros((x, y))
    for i in range(m):
        sigmainv[i][i]=1/sigma[i][i]
        
    sigmainv=sigmainv.transpose()
        
    #print ("1/sigma of Sigma")
    #print (sigmainv)
    
    vectorVT=numpy.dot(vectorinvU, Matrix)
    vectorVT=numpy.dot(sigmainv,vectorVT)
    #print ("VT")
    #print (vectorVT)


    '''
    vectorVT= numpy.transpose(vectorV)
    print "vectorVT:"
    print(vectorVT)
    '''

    M=numpy.dot(vectorU, sigma)
    M=numpy.dot(M, vectorVT)
    
    #for i in range(x):
    #    for j in range(y):
    #        if (numpy.absolute( M[i,j] ) < 0.0000000001):
    #            M[i,j]=0
                
    M[M<0.0000000001]=0
    #print ("Restore:")
    #print(M)

    #print ("U E V*:")
    #print(vectorU)
    #print(sigma)
    #print( vectorVT)
    #print('The number of singular values')
    #print(m)
    
    return vectorU, sigma, vectorVT



