# Thompson Sampling

## Importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Importing the dataset

dataset=pd.read_csv('dataset name goes here')


## Implementing Thompson Sampling

import random
N=500
d=10
ads_selected=[]
ad_0=[0]*d
ad_1=[0]*d
total_reward=0
for n in range(0,N):
  ad=0
  max_random=0
  for i in range(0,d):
    random_beta=random.betavariate(ad_1[i]+1,ad_0[i]+1)
    if (random_beta>max_random):
      max_random=random_beta
      ad=i
  ads_selected.append(ad)
  reward=dataset.values[n,ad]
  if reward==1:
    ad_1[ad]=ad_1[ad]+1
  else:
    ad_0[ad]=ad_0[ad] +1
  total_reward=total_reward+reward





## Visualising the results - Histogram

plt.hist(ads_selected)
plt.show()