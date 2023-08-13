# -*- coding: utf-8 -*-
"""kernel_pca_a_d=3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GT6dQhjA4lX1DuX7h3_Gj9vDcZl_ZIav
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import pprint
import matplotlib.pyplot as plt
# %matplotlib inline
#%precision 4
#np.set_printoptions(precision=4)
import pylab as pl

from google.colab import drive
drive.mount("/content/gdrive")

from google.colab import files
uploaded = files.upload()
for func in uploaded.keys():
       print('User uploaded file "{name}"'.format(name=func))
       
#on running this it will ask permission to mount with google drive. please click ok and allow. this program does not access any of the
# google drive documents except dataset which is uploaded
#a choose file button is displayed and on clicking that it will ask to choose the file. select the dataset in the question 
#and on running this, the dataset gets uploaded to google drive



from numpy import genfromtxt
mylist=genfromtxt("/content/gdrive/My Drive/Colab Notebooks/Dataset.csv", delimiter=',')
print(mylist)

import matplotlib.pyplot as plt
import numpy as np
# Compute the x and y coordinates for points on a sine curve
#x = np.arange(0, 3 * np.pi, 0.1,)
#y = np.sin(x)
x=np.zeros(mylist.shape[0])
y=np.zeros(mylist.shape[0])
for i in range(mylist.shape[0]):
  x[i]=mylist[i][0]
  y[i]=mylist[i][1]

# Plot the points using matplotlib
plt.plot(x,y,'o')
plt.show()

mylist.shape

K=np.zeros((mylist.shape[0],mylist.shape[0]))
#K2=np.zeros((mylist.shape[0],mylist.shape[0]))
#K=[[0]*mylist.shape[0] for i in range(mylist.shape[0])]
for i in range(mylist.shape[0]):
  for j in range(mylist.shape[0]):
    K[i][j]=(mylist[i].dot(mylist[j].transpose())+1)**3
    #K2[i][j]=(mylist[i].dot(mylist[j].transpose())+1)**3

print(len(K),len(K[0]))
#print(len(K1),len(K1[0]))

#from numpy.core.numeric import identity
n=len(K)
one=np.zeros((n,n))

for i in range(n):
  for j in range(n):
    one[i][j]=1/n

identity_matrix=np.identity(n)
identity_matrix

K_centered=np.zeros((n,n))
#K_centered2=np.zeros((n,n))

K_centered=(identity_matrix-one).dot(K).dot(identity_matrix-one)
#K_centered2=(identity_matrix-one).dot(K2).dot(identity_matrix-one)
K_centered.shape
#K_centered2.shape

#K_mean=np.mean(K, axis = 0)
#K_centered = K


#for i in range(len(K)):
#  for j in range(len(K)):
#    K_centered[i][j]=K[i][j]-K_mean[j]

#print(list_mean)
#print(list_centered)

eigen_values , eigen_vectors = np.linalg.eig(K_centered)
#eigen_values2 , eigen_vectors2 = np.linalg.eig(K_centered2)

print('Eigenvectors \n%s' %eigen_vectors)
print('\nEigenvalues \n%s' %eigen_values)
eigen_vectors.shape

sorted_index = np.argsort(eigen_values)
sorted_index=sorted_index[::-1]
 
sorted_eigenvalue = eigen_values[sorted_index]
sorted_eigenvectors = eigen_vectors[:,sorted_index]
sorted_eigenvectors

captured_var=[]
j=0

tot = sum(eigen_values)
var=0
for i in sorted_eigenvalue:
  var+=(i/tot)*100
  captured_var.append(var)
  j=j+1

print("Variance captured by each component:\n")
for i in range(j):
  print(captured_var[i])

cum_var=0
k=0
threshold=95
for i in range(j):
  cum_var=cum_var+captured_var[i]
  k=k+1
  if(cum_var>=threshold):
    break
print("\nThe number of principal components:", k)

alpha=np.zeros((eigen_vectors.shape[0],k))
for i in range(eigen_vectors.shape[0]):
  for j in range(k):
   alpha[i][j] = sorted_eigenvectors[i][j]/sorted_eigenvalue[j]

alpha.shape

new=np.zeros((eigen_vectors.shape[0],k))
new=K_centered.dot(alpha)

new.shape

newx=np.zeros(new.shape[0])
newy=np.zeros(new.shape[0])
for i in range(new.shape[0]):
  newx[i]=new[i][0]
  newy[i]=new[i][1]

plt.plot(newx,newy,'o')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

fig=plt.figure
plt.show()