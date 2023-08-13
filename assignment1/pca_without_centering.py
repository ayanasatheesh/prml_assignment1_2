# -*- coding: utf-8 -*-
"""pca_without_centering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iYAMChxxyyZopLyh2LqfPCUVfbf6J9VY
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

covmat=np.dot(mylist.T, mylist)/(mylist.shape[0])
covmat

eigen_values , eigen_vectors = np.linalg.eig(covmat)

print('Eigenvectors \n%s' %eigen_vectors)
print('\nEigenvalues \n%s' %eigen_values)

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
  var=(i/tot)*100
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

w=[[0]*k for i in range(k)]
for i in range(k):
  for j in range(k):
   w[i][j] = sorted_eigenvectors[j][i]
  
w

Y = mylist.dot(w)
Y

x=np.zeros(mylist.shape[0])
y=np.zeros(mylist.shape[0])
for i in range(mylist.shape[0]):
  x[i]=mylist[i][0]
  y[i]=mylist[i][1]


# Plot the points using matplotlib
#plt.plot(x,y,'o')
#plt.xlim(0, 8), plt.ylim(-2, 8)
plt.plot(w[1],label="W1")
plt.xlabel("X values")
plt.ylabel("Y values")

#plt.plot(w[0],label="W2")

plt.legend(loc='best')
plt.show()

plt.plot(w[0],label="W2")
plt.legend(loc='best')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()