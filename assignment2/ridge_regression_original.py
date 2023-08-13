# -*- coding: utf-8 -*-
"""ridge_regression_original.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14TTJgRY5YXbmx1xnyEFgphnm6rj476le
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
#on running this it will ask permission to mount with google drive. please click ok and allow. this program does not access any of the
# google drive documents except dataset which is uploaded

#%from google.colab import files
#%uploaded = files.upload()
#%for func in uploaded.keys():
#%       print('User uploaded file "{name}"'.format(name=func))

from numpy import genfromtxt
mylist=genfromtxt("/content/gdrive/My Drive/Colab Notebooks/A2Q2Data_train.csv", delimiter=',')
print("The given train dataset is:")
print(mylist)

from numpy import genfromtxt
testlist=genfromtxt("/content/gdrive/My Drive/Colab Notebooks/A2Q2Data_test.csv", delimiter=',')
print("The given test data is:")
print(testlist)

trainlist=mylist[:-2000]


validationlist=mylist[-2000:]

xtrain=trainlist.T[:-1]
ytrain=trainlist.T[-1]

x_train=mylist.T[:-1]
y_train=mylist.T[-1]
mat=np.dot(x_train,x_train.transpose())
eigen_values , eigen_vectors = np.linalg.eig(mat)
sorted_i = np.argsort(eigen_values)
sorted_i=sorted_i[::-1]
 
eigen_values = eigen_values[sorted_i]
print("The eigen values of XXT in descending order are:")
print(eigen_values)

print("Number of eigen values:",len(eigen_values))

xtest=validationlist.T[:-1]
ytest=validationlist.T[-1]

def calculateError(wt):
  temp=np.dot(wt.transpose(),xtest)
  
  error=temp-ytest
  errorsum=0;
  for i in range(500):
    errorsum+=(error[i]**2)
  return errorsum


def calcgrad(wt,grad,lmb):
  error=calculateError(wt)

  preverror=0
  i=0
  while(abs(preverror-error)>0.001):
    preverror=error
    wtnext=wt-(grad*stepsize)
    wt=wtnext
    temp=np.dot(xtrain,xtrain.transpose())    #calculating gradient 
    #temp.shape
    temp=np.dot(temp,wt)
    temp.shape
    grad=temp-(np.dot(xtrain,ytrain))
    grad=grad+lmb*wt
    grad=grad*2

    error=calculateError(wt)
    i=i+1
  
  return (wt,error)

wt=np.zeros(100,)
stepsize=1/(10**6)
iterations=10000


reserror=[]
print("Performing cross validation for various choices of lambda")
#the eigen values of XXT are lambda that is taken here
for i in range(len(eigen_values)):
  
  temp=np.dot(xtrain,xtrain.transpose())  #initial gradient
  
  temp=np.dot(temp,wt)
  
  gradient=temp-(np.dot(xtrain,ytrain))
  gradient=gradient+eigen_values[i]*wt
  gradient=gradient*2
  
  (wtnext,err)=calcgrad(wt,gradient,eigen_values[i])
  print("Error for lambda= ", eigen_values[i]," on validation set is:",err)
  reserror.append(err)
  wt=wtnext



plt.plot(eigen_values,reserror,'-o')
plt.xlabel('lambda')
plt.ylabel('error')
plt.show()

minindex=reserror.index(min(reserror))
print("The error is minimum at index:- ",minindex," for lambda=",eigen_values[minindex])

x_test=testlist.T[:-1]
y_test=testlist.T[-1]

#function to calculate error on test data

def calculateError(wt):
  temp=np.dot(wt.transpose(),x_test)
  #print(temp.shape)
  #temp=temp.transpose()
  error=temp-y_test
  errorsum=0;
  for i in range(500):
    errorsum+=(error[i]**2)
  return errorsum

#function to perform gradient descent on original train set
def calcgrad(wt,grad,lmb):
  error=calculateError(wt)

  preverror=0
  i=0
  while(abs(preverror-error)>0.0001):
    preverror=error
    wtnext=wt-(grad*stepsize)
    wt=wtnext
    temp=np.dot(x_train,x_train.transpose())    #calculating gradient 
    #temp.shape
    temp=np.dot(temp,wt)
    temp.shape
    grad=temp-(np.dot(x_train,y_train))
    grad=grad+lmb*wt
    grad=grad*2
    error=calculateError(wt)
    i=i+1
  
  return (wt,error)

(wr,erro)=calcgrad(wt,gradient,eigen_values[minindex])

print("Error on test data is: ",erro)

print("wr calculated for ridge regression is:")
print(wr)