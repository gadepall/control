###################################################################

# This a python code for verifying system using routh array.    
# By Moparthi Varun Sankar
# April 17 , 2020 
# Released under GNU GPL

###################################################################
import numpy as np
import itertools as itert
import math
import matplotlib.pyplot as plt
import control
import scipy as sp

degree = 3
c = [4,3,16,12,0,0] #Taking coefficients as input

Rou_matrix=np.zeros([degree+1,degree+1])            #Form first and second row of the Routh Matrix
for j in range (0,degree-1):
	Rou_matrix[0,j]=c[2*j]
	Rou_matrix[1,j]=c[(2*j)+1]
	
	
	
for i in range(2,degree+1):                    #Calculating the remaining rows in the Routh matrix
	for j in range (0,degree-1):
		Rou_matrix[i,j]= (((Rou_matrix[i-1,0]*Rou_matrix[i-2,j+1])-(Rou_matrix[i-1,j+1]*Rou_matrix[i-2,0]))/(Rou_matrix[i-1,0]))
	if(Rou_matrix[i,0]== 0 ):
		Rou_matrix[i,0]=0.0000001
        

for i in range(0,degree+1):                               # checking whether system is oscillatory 
	n=0
	for j in range(0,degree+1):
		if (round(Rou_matrix[i,j],4) == 0.0000):
			n =n+1
	if(n == degree+1):
		print("System is Oscillatory")
        		
rou_first_row=[]
for i in range (0,degree+1):                    #Taking the first row elements 
	rou_first_row.append(Rou_matrix[i,0])

sign_changes=(len(list(itert.groupby(rou_first_row, lambda rou_first_row: rou_first_row > 0)))-1)     #calculating no of sign changes 
if sign_changes==0:
	print("System is stable because no poles on right half of s plane")
else:
	print("System is unsbale because it has poles on right half of s plane and No.of poles on right half of s plane is:",sign_changes) 
print(Rou_matrix)
