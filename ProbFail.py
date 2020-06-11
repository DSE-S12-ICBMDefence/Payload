# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:58:37 2020

@author: Gabriel
"""
import numpy as np

def matrixfiller(planes,scinplane,pfail):
    matrix = np.ones((planes,scinplane))*99
    for i in range(planes):
        for j in range(scinplane):
            matrix[i,j]=np.random.choice(np.arange(0, 2), p=[pfail,1-pfail])
    return matrix

# print(matrixfiller(planes,scinplane,pfail))

def failcheck(matrix):
    dim = matrix.shape
    failure = False
    
    for i in range(dim[0]):
        
        errors = []
        if failure:
            break
        
        for j in range(dim[1]):
            
            if matrix[i,j]==0:
                errors.append(j)
                
        initial_length = len(errors)
        
        if len(errors)>0:
            errors.extend([errors[0]+dim[1]])
        
            for k in range(initial_length):                          
                if errors[k]+4 >= errors[k+1]:
                    failure = True
                    break             
                
    return failure
        
# matrix = np.ones((2,10)) 
# matrix[1,0] = 0
# matrix[1,5] = 0 

# print(failcheck(matrix)) 

# pfail = 0.5/100

for pfail in np.linspace(0.01,0.5,100)/100:
    
    planes = 7
    scinplane = 65
            
    runs = 100000
    failcount = 0
    for i in range(runs):
        matrix = matrixfiller(planes,scinplane,pfail)
        result = failcheck(matrix)
        if result == True:
            failcount += 1
        if i == runs/4:
            print('one quarter there')
        if i == runs/2:
            print('halfway there')
        if i == runs*3/4:
            print('three quarters there')
        if failcount/runs*100>=1:
            break
    print(pfail,failcount/runs*100)
    
