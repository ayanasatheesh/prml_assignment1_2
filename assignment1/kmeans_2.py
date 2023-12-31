# -*- coding: utf-8 -*-
"""kmeans_b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rim0_eku1LAzM0j6swzTb7LEu46e6sFO
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

#from sympy import Point, Segment, perpendicular_bisector
import random
fixedpartition = []
for i in range(mylist.shape[0]):
  n = random.randint(0,10)
  fixedpartition.append(n)
  

def kmeans(k):
  initialpartition=[]
  for i in range(len(fixedpartition)):
    initialpartition.append(fixedpartition[i]%k)

  sum=np.zeros((k,mylist.shape[1]))
  count=np.zeros((k,mylist.shape[1]))
  for i in range(len(initialpartition)):
    sum[initialpartition[i]]+=mylist[i]
    count[initialpartition[i]]+=1
  mean=np.zeros((k,mylist.shape[1]))
  for i in range(k):
      for j in range(mylist.shape[1]):
        if(count[i][j]==0):
          mean[i][j]=0
        else:
          mean[i][j]=sum[i][j]/count[i][j]
  #mean
  dist=np.zeros(k)
  newpartition=[]
  errorfunction=[]
  c=0
  prevpartition=initialpartition
  while prevpartition!=newpartition:
    prevpartition=newpartition
    newpartition=[]
    s=0
    for i in range(mylist.shape[0]):
      for j in range(k):
        dist[j]=np.linalg.norm(mylist[i]-mean[j])
      mink=np.argmin(dist)
      newpartition.append(mink)
      s+=dist[mink]
    errorfunction.append(s)

    sum=np.zeros((k,mylist.shape[1]))
    count=np.zeros((k,mylist.shape[1]))
    for i in range(len(newpartition)):
      sum[newpartition[i]]+=mylist[i]
      count[newpartition[i]]+=1

    for i in range(k):
      for j in range(mylist.shape[1]):
        if(count[i][j]==0):
          mean[i][j]=0
        else:
          mean[i][j]=sum[i][j]/count[i][j]
    c=c+1;

  iterations=[i for i in range(1,c+1)]   
  #newpartition

  
  #for i in range(mean.shape[0]):
  #  for j in range(mean.shape[0]):
   #   p1,p2=Point(mean[i][0], mean[i][1]), Point(mean[j][0], mean[j][1])
   #   s1 = Segment(p1, p2)
   #   perpendicularBisector = s1.perpendicular_bisector()
    #  plt.plot(perpendicular_bisector)

  plt.scatter(mylist[:, 0], mylist[:, 1], c=newpartition)
  plt.xlabel('Xvalues')
  plt.ylabel('Yvalues')
  plt.show()
  #plt.plot(iterations,errorfunction)
  #plt.show()
  #colors = ['b', 'g', 'r','y']
 # for i in range(len(newpartition)):
  #  plt.plot(mylist[i][0], mylist[i][1], color=colors[newpartition[i]-1])

#K=[2,3,4,5]
for i in range(2,6):
  kmeans(i)
#kmeans(2)