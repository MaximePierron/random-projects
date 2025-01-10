# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:21:36 2024

@author: MPEIRRON
"""

# Detect Fraud with SOM
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

# Detect Fraud
threshold = 0.9
distance_map = som.distance_map().T
fraud_neurons = np.argwhere(distance_map > threshold)

frauds = np.empty((0, X.shape[1]))

for neuron in fraud_neurons:
    neuron_frauds = som.win_map(X).get((neuron[0], neuron[1]), [])
    if len(neuron_frauds) > 0:
        frauds = np.concatenate((frauds, neuron_frauds), axis=0)

frauds = sc.inverse_transform(frauds)

print("Fraudulent applications:")
print(frauds)

##From non-supervised to supervised

#Create variable matrix
customers = dataset.iloc[:, 1:].values

#Create dependant variable
is_fraudulent = np.zeros(len(dataset))

for i in range(len(dataset)):
    if dataset.iloc[i, 0] in frauds:
        is_fraudulent[i] = 1
        
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(customers)

from keras.models import Sequential
from keras.layers import Dense
#Dropout
from keras.layers import Dropout

#Initiation
classifier = Sequential()

#Ajouter la couche d'entrée et une couche cachée
classifier.add(
    Dense(
        3,
        activation='relu',
        kernel_initializer='uniform',
        input_dim=15
    )
)

classifier.add(Dropout(0.1))


#Ajouter la couche de sortie
classifier.add(
    Dense(
        1,
        activation='sigmoid',
        kernel_initializer='uniform'
    )
)

#Reseau de neurones initialisés
#Compiler le réseau de neurones
classifier.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

#Entraîner le réseau de neurones
classifier.fit(
    customers,
    is_fraudulent,
    batch_size=1,
    epochs=10
)

# Prediction des résultats du set de test
y_pred_prob = classifier.predict(customers)

# Convert probabilities to binary class labels
y_pred = (y_pred_prob > 0.2).astype(int)

results = np.concatenate((dataset.iloc[:, 0:1], y_pred_prob), axis=1)

results = results[results[:, 1].argsort()]
