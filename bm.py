# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable

movies = pd.read_csv(
    'Boltzmann_Machines/ml-1m/movies.dat',
    sep='::',
    header=None,
    engine='python',
    encoding='latin-1'
)

users = pd.read_csv(
    'Boltzmann_Machines/ml-1m/users.dat',
    sep='::',
    header=None,
    engine='python',
    encoding='latin-1'
)

ratings = pd.read_csv(
    'Boltzmann_Machines/ml-1m/ratings.dat',
    sep='::',
    header=None,
    engine='python',
    encoding='latin-1'
)

training_set = pd.read_csv(
    'Boltzmann_Machines/ml-100k/u1.base',
    delimiter='\t',
    header=None
)

training_set = np.array(training_set, dtype='int64')

test_set = pd.read_csv(
    'Boltzmann_Machines/ml-100k/u1.test',
    delimiter='\t',
    header=None
)

test_set = np.array(test_set, dtype='int64')

#Number of users
nb_users = int(max(max(training_set[:,0]), max(test_set[:,0])))
#Number of movies
nb_movies = int(max(max(training_set[:,1]), max(test_set[:,1])))

#Convert data into matrix
def convert(data):
    new_data = []
    for user_id in range(1, nb_users + 1):
        movies_id = data[data[:,0] == user_id, 1]
        ratings_id = data[data[:,0] == user_id, 2]
        movie_ratings = np.zeros(nb_movies)
        movie_ratings[movies_id - 1] = ratings_id
        new_data.append(list(movie_ratings))
    return new_data

training_set = convert(training_set)
test_set = convert(test_set)

#Convert data into tensor
training_set = torch.FloatTensor(training_set)
test_set = torch.FloatTensor(test_set)

#Convert ratings to 1 and 0
training_set[training_set == 0] = -1
training_set[training_set <= 2] = 0
training_set[training_set >= 3] = 1

test_set[test_set == 0] = -1
test_set[test_set <= 2] = 0
test_set[test_set >= 3] = 1

#Create neural network architecture
class RBM():
    def __init__(self, nv, nh):
        self.W = torch.randn(nh, nv)
        self.a = torch.randn(1, nh)
        self.b = torch.randn(1, nv)
    
    def sample_h(self, x):
        wx = torch.mm(x, self.W.t())
        activation = wx + self.a.expand_as(wx)
        p_h_given_v = torch.sigmoid(activation)
        return p_h_given_v, torch.bernoulli(p_h_given_v)
    
    def sample_v(self, y):
        wy = torch.mm(y, self.W)
        activation = wy + self.b.expand_as(wy)
        p_v_given_h = torch.sigmoid(activation)
        return p_v_given_h, torch.bernoulli(p_v_given_h)
    
    def train(self, v0, vk, ph0, phk):
      self.W += (torch.mm(v0.t(), ph0) - torch.mm(vk.t(), phk)).t()
      self.b += torch.sum((v0 - vk), 0)
      self.a += torch.sum((ph0 - phk), 0)
        

nv = nb_movies
nh = 200
batch_size = 100

#Create a restricted boltzmann machine
rbm = RBM(nv=nv, nh=nh)

#Train RBM
epochs = 10
for epoch in range(1, epochs + 1):
    train_loss = 0
    s = 0.
    for user_id in range(0, nb_users - batch_size, batch_size ):
        v0 = training_set[user_id:user_id + batch_size]
        vk = v0
        ph0, _ = rbm.sample_h(v0)
        for k in range(10):
            _, hk = rbm.sample_h(vk)
            _, vk = rbm.sample_v(hk)
            vk[v0 < 0] = v0[v0 < 0]
        phk, _ = rbm.sample_h(vk)
        rbm.train(v0, vk, ph0, phk)
        train_loss += torch.mean(torch.abs(v0[v0 >= 0] - vk[v0 >= 0]))
        s += 1.
    print(f"epoch: {epoch}, loss: {train_loss / s}")
        
#Test RBM
test_loss = 0
s = 0.
for id_user in range(nb_users):
    v = training_set[id_user:id_user+1]
    vt = test_set[id_user:id_user+1]
    if len(vt[vt>=0]) > 0:
        _, h = rbm.sample_h(v)
        _, v = rbm.sample_v(h)
        test_loss += torch.mean(torch.abs(vt[vt>=0] - v[vt>=0]))
        s += 1.
print(f"loss: {test_loss / s}")