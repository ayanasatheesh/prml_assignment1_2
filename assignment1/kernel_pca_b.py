# -*- coding: utf-8 -*-
"""kernel_pca_b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LBlrHB83gwgQWVQTqSToJQVzhK3a4sfW
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

ds=[x * 0.1 for x in range(1, 11)]
for d in ds:
  from math import exp
  K=np.zeros((mylist.shape[0],mylist.shape[0]))
  #K2=np.zeros((mylist.shape[0],mylist.shape[0]))
  #K=[[0]*mylist.shape[0] for i in range(mylist.shape[0])]
  for i in range(mylist.shape[0]):
    for j in range(mylist.shape[0]):
      K[i][j]=((-(mylist[i]-mylist[j])).dot(mylist[i]-mylist[j]).transpose())/(2*d*d)
      #K2[i][j]=(mylist[i].dot(mylist[j].transpose())+1)**3
  K=np.exp(K)
  #K[0:5]

  n=len(K)
  one=np.zeros((n,n))

  for i in range(n):
    for j in range(n):
      one[i][j]=1/n

  identity_matrix=np.identity(n)
  #identity_matrix

  K_centered=np.zeros((n,n))
#K_centered2=np.zeros((n,n))

  K_centered=(identity_matrix-one).dot(K).dot(identity_matrix-one)
  eigen_values , eigen_vectors = np.linalg.eig(K_centered)
  #print('Eigenvectors \n%s' %eigen_vectors)
#print('\nEigenvalues \n%s' %eigen_values1)
  eigen_vectors.shape

  sorted_index = np.argsort(eigen_values)
  sorted_index=sorted_index[::-1]
 
  sorted_eigenvalue = eigen_values[sorted_index]
  sorted_eigenvectors = eigen_vectors[:,sorted_index]
  #sorted_eigenvectors

  captured_var=[]
  j=0

  tot = sum(eigen_values)
  var=0
  for i in sorted_eigenvalue:
    var+=(i/tot)*100
    captured_var.append(var)
    j=j+1

  #print("Variance captured by each component:\n")
  #for i in range(j):
  #  print(captured_var[i])

  cum_var=0
  k=0
  threshold=95
  for i in range(j):
    cum_var=cum_var+captured_var[i]
    k=k+1
    if(cum_var>=threshold):
      break
  #print("\nThe number of principal components:", k)

  alpha=np.zeros((eigen_vectors.shape[0],k))
  for i in range(eigen_vectors.shape[0]):
    for j in range(k):
      alpha[i][j] = sorted_eigenvectors[i][j]/sorted_eigenvalue[j]

  #alpha.shape
  new=np.zeros((eigen_vectors.shape[0],k))
  new=K_centered.dot(alpha)

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