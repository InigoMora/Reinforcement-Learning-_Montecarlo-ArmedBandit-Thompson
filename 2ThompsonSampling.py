#!/usr/bin/python3
    # Iñigo Auza de la Mora - Student ID 2824537

import random

from matplotlib import pyplot as plt



a = b = 1

#def beta_distribution(a,b):

def mean_beta_distribution(a,b):
    return ( 1/ (1+(b/a)) )

def variance_beta_distribution(a,b):
    return ( (a+b)/(pow((a+b),2)*(a+b+1)) )

def sample_bandit():
    # Uknown probability  0 ≤ p ≤ 1
    p = .6

    if random.uniform(0, 1) < p:
        return 1
    else:
        return 0
    

#History
a_history = [1]
b_history = [1]
mean_history = [mean_beta_distribution(a,b)]
variance_history = [variance_beta_distribution(a,b)]

epochs = 300

for i in range (epochs-1):
    # sample from arm
    sample = sample_bandit()
    if sample == 1:
        a += 1
    else:   # sample == 0
        b += 1

    a_history.append(a)
    b_history.append(b)
    mean_history.append(mean_beta_distribution(a,b))
    variance_history.append(variance_beta_distribution(a,b))


range_ = list(range(1,epochs+1))    # List for plot's x axis

plt.plot(range_, mean_history)
plt.title("Beta-Distribution: Mean Histogram")
plt.xlabel("Epochs")
plt.ylabel('Mean')
plt.show()

plt.plot(range_, variance_history)
plt.title("Beta-Distribution: Variance Histogram")
plt.xlabel("Epochs")
plt.ylabel('Variance')
plt.show()