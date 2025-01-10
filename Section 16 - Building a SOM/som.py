# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:16:09 2024

@author: MPEIRRON
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Self_Organizing_Maps/Credit_Card_Applications.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1:].values

#Scaling
from sklearn.preprocessing import MinMaxScaler

sc= MinMaxScaler()
X = sc.fit_transform(X)

#Train SOM
from minisom import MiniSom

som = MiniSom(x=15, y=15, input_len=15)

som.random_weights_init(X)

som.train_random(X, num_iteration=100)

#Visualisation
from pylab import bone, pcolor, colorbar, plot, show

bone()

pcolor(som.distance_map().T)
colorbar()

markers = ['o', 's']
colors = ['r', 'g']

for index, values in enumerate(X):
    w = som.winner(values)
    plot(
        w[0]+0.5, w[1]+0.5,
        markers[int(Y[index])],
        markeredgecolor=colors[int(Y[index])],
        markerfacecolor='None',
        markersize=10,
        markeredgewidth=2
    )

show()

#Detect Fraud
mappings = som.win_map(X)
frauds = frauds = np.concatenate((mappings[(11,7)], mappings[(9,8)]), axis = 0)
frauds = sc.inverse_transform(frauds)

#Printing the Fraunch Clients
print('Fraud Customer IDs')
for i in frauds[:, 0]:
  print(int(i))