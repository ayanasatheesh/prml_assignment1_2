# -*- coding: utf-8 -*-
"""stochastic_gradient_descent_original.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1klY_cGy5yXaXMmTv5mEos3oHtUN-3fnn
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
print("The given dataset is:")
print(mylist)

from numpy import genfromtxt
testlist=genfromtxt("/content/gdrive/My Drive/Colab Notebooks/A2Q2Data_test.csv", delimiter=',')
print("The given test data is:")
print(testlist)

Xtrain=mylist.T[:-1]
Ytrain=mylist.T[-1]
Y= np.dot(Xtrain,Xtrain.transpose())
Y=np.linalg.inv(Y)
Y=np.dot(Y,Xtrain)
w=np.dot(Y,Ytrain)

import random

def createBatches():
  list=[]
  randomRows = np.random.randint(mylist.shape[0], size=100)
  for i in randomRows:
    list.append(mylist[i])

  xtrain=np.transpose(list)[:-1]
  ytrain=np.transpose(list)[-1]
  return (xtrain,ytrain)

wt=np.random.rand(100,)/10000

(xtrain,ytrain)=createBatches()
stepsize=1/(2*(10**5))
iterations=50000
temp=np.dot(xtrain,xtrain.transpose())
#temp.shape
temp=np.dot(temp,wt)
temp.shape
gradient=temp-(np.dot(xtrain,ytrain))
gradient=gradient*2

xtest=testlist.T[:-1]

ytest=testlist.T[-1]

def calculateError(wt):
  temp=np.dot(wt.transpose(),xtest)
  #print(temp.shape)
  #temp=temp.transpose()
  error=temp-ytest
  errorsum=0;
  for i in range(500):
    errorsum+=(error[i]**2)
  return errorsum

#gradient=np.dot((np.dot(xtrain,xtrain.transpose())),wt)-(np.dot(xtrain,ytrain))
xplot=[]
yplot=[]
error=calculateError(wt)
res=[]
res.append(wt)


preverror=0
i=0
while(abs(preverror-error)>0.0000001):
  preverror=error
  wtnext=wt-(gradient*stepsize)
  wt=wtnext
  res.append(wt)
  (xtrain,ytrain)=createBatches()
  temp=np.dot(xtrain,xtrain.transpose())    #calculating gradient 
  #temp.shape
  temp=np.dot(temp,wt)
  temp.shape
  gradient=temp-(np.dot(xtrain,ytrain))
  gradient=gradient*2
  gradient.shape
  diff=np.linalg.norm(wt-w)
  xplot.append(diff)
  yplot.append(i)
  error=calculateError(wt)
  
  i=i+1

res=np.transpose(res)

sum=[]
for i in range(res.shape[0]):
  s=0
  for j in range(res.shape[1]):
    s+=res[i][j]
  s=s/len(yplot)
  sum.append(s)


len(sum)
wavg=np.transpose(sum)

error=calculateError(wavg)
print("Error on test data using stochastic gradient is: ", error)

plt.plot(yplot,xplot)
plt.ylabel("||wt-wml||")
plt.xlabel("iterations")
plt.show()