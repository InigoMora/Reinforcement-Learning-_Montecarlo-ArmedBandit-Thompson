#!/usr/bin/python3
    # Iñigo Auza de la Mora - Student ID 2824537

import numpy as np

import random
#from random import randint

import statistics

import numpy as np

"""
import sympy as smp
import matplotlib.pyplot as plt
import scipy as sp
"""


# Sickness probability range
p_min = .0001
p_max = .1
# From text: p can take values between 10−1 and 10−4
# As there is no specification of the distribution, we will use random.uniform

# Number of patients
N = 1000000
#N = 100








def is_sick(sick_prob_min, sick_prob_max):
    # Decide if patient is sick
    if random.uniform(sick_prob_min, 1) > sick_prob_max:
        return False
    else:
        return True





def test_batch_size(batch):
    #Because the tree only has two layers, there is no need to keep recod of decisitions beyond one layer

    patients_tested = 0
    batch_size = batch
    num_tests = 0


    while patients_tested < N:
        #patients_counter += 1

        # Check batch together
        sick_in_batch = False

        curr_batch = batch_size
        if (patients_tested + batch_size) > N:  #If making a whole batch would suppass N
            curr_batch = N - patients_tested    # Test just the remainder of the patients

        patients_tested += curr_batch

        for patient in range(curr_batch):
            if is_sick(p_min, p_max) == True:
                sick_in_batch = True

        num_tests += 1 #The test for the batch

        if sick_in_batch == True:   #If there is a sick in the batch
            num_tests += curr_batch #Rules say will have to test them all individually


    return num_tests





trials = 1

best_ks = []
tests_needed = []

percentage = 0

for i in range(trials):
    seed=i
    best_batch = 1  #values for the batch size = 1 (individual tests)
    min_tests = N
    for batch in range(2,N+1):  #We already knoe the answer for batch size 1. Also, the rules apply different because batch size 1 does not need to repeat tests if the result is possitive(would be redundant)
        random.seed(seed)
        num_tests = test_batch_size(batch)

        if num_tests < min_tests:
            min_tests = num_tests
            best_batch = batch

            print("New Best")
            print("optimal batch: ", best_batch)
            print("number of tests: ", min_tests)

    best_ks.append(best_batch)
    tests_needed.append(min_tests)


    if  (i % 10 )== 0:
        percentage += 10
        print(str(percentage) + '%')



np_best_ks = np.array(best_ks)
np.savetxt('1MonteCarloSimulation_V2/optimal_ks.txt', np_best_ks)

np_tests_needed = np.array(tests_needed)
np.savetxt('1MonteCarloSimulation_V2/required_tests.txt', np_tests_needed)

print('Mean optimal_ks: ', statistics.mean(best_ks))
print('Mean minimum_tests: ', statistics.mean(tests_needed))









