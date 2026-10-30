#!/usr/bin/python3
    # Iñigo Auza de la Mora - Student ID 2824537

import numpy as np

import random
#from random import randint

import statistics


# Sickness probability range
p_min = .0001
p_max = .1
# From text: p can take values between 10−1 and 10−4
# As there is no specification of the distribution, we will use random.uniform


# Number of patients
N = 1000000


# https://www.programiz.com/python-programming/examples/list-chunks
# https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks
def split_list(list_, chunk_size):
  for i in range(0, len(list_), chunk_size):
    yield list_[i:i + chunk_size]
#Example
"""
chunk_size = 2
my_list = [1,2,3,4,5,6,7,8,9]
container = list(split_list(my_list, chunk_size))
print(container)
"""


def build_patient_list(number_patients, sick_prob_min, sick_prob_max):
    # Build list of patients
    patients = []   # 0 will mean Healthy, 1 will mean sick

    for patient in range(number_patients):
        # From text: p can take values between 10−1 and 10−4
        # As there is no specification of the distribution, we will use random.uniform
        patient_prob = random.uniform(sick_prob_min, p_max)

        # Decide if patient is sick
        if random.uniform(sick_prob_min, 1) > sick_prob_max:
            patients.append(0)
        else:
            patients.append(1)

    # Count sick patienst
    counter = 0
    for i in patients:
        if i == 1:
            counter += 1

    #print("Total Sick People: ", counter)   #******

    return patients


def calculate_test(patient_list, k):
    # Test counter
    num_tests = 0

    # Monte Calo

    # It has only two stages
        # Test on k batches
        # Retest all possitives individually
    container = list(split_list(patients, k))
    num_tests += len(container)

    for list_ in container:
        if 1 in list_:
            #print(list_)   #*******
            #print(len(list_))  #****
            num_tests += len(list_)
    
    return num_tests







 

def try_all_k(N, patients):
    min_test = N
    k_optimal = 1
    # TRY ALL K sizes
    for i in range(N): #We try every k, as the tree are all two layers with a single line each
        k=i+1 
        num_tests = calculate_test(patients, k)
        if num_tests < min_test:
            min_test = num_tests
            k_optimal = k

    return k_optimal, min_test






optimal_ks = []
minimum_tests = []



percentage = 0
for i in range(10):    #do 100 tests
    patients = build_patient_list(N, p_min, p_max)
    k_optimal, num_test = try_all_k(N, patients)
    optimal_ks.append(k_optimal)
    minimum_tests.append(num_test)
    if  (i % 10 )== 0:
        percentage += 10
        print(str(percentage) + '%')

print('optimal_ks')
print(optimal_ks)

print('minimum_tests')
print(minimum_tests)

print('Mean optimal_ks: ', statistics.mean(optimal_ks))
print('Mean minimum_tests: ', statistics.mean(minimum_tests))


























#NOTES to self



#N = 100 #5,3,5

"""
In one occassion
N=100

optimal = 13            #in some other 21


Total Sick People:  4
k 1
num_tests 104
k 2
num_tests 58
k 3
num_tests 46
k 4
num_tests 41
k 5
num_tests 40
k 6
num_tests 41
k 7
num_tests 43
k 8
num_tests 45
k 9
num_tests 48
k 10
num_tests 40
k 11
num_tests 54
k 12
num_tests 57
k 13
num_tests 34
"""


#N = 1000000
"""
Total Sick People:  100057
k_optimal:  2
min_test:  690034
k_optimal:  3
min_test:  604540
k_optimal:  4
min_test:  594456
"""

#N = 100000000        
"""
Total Sick People:  9986213
k_optimal:  2
min_test:  68975280
k_optimal:  3
min_test:  60400411
k_optimal:  4
min_test:  59350432
"""






# Implementation with threshold **** NOT finished****
    # NOT USED
"""
def threshold_montecarlo(N, patients):
    
    #k_optimal = 1 #*******

    # initial k
    k = round(N/2)
    threshold = 1
    #adjustment = round(k/2) # half_n **** # Half way point
    adjustment = k-1
    adjustment_rate = .1    # Not greater than 1
    #adjustment_rate = .001 *****
    k_optimal = k
    min_test = N    #****Not needed when th line below min_test = calculate_test(patients, k) is present 
    adjustment_change = False

    #all k's
    ks = list(range(1,N))   #********

    # Get an initial k value and calculate results 
    min_test = calculate_test(patients, k)

    # hold on to tested k's
    tested_ks = [k]

    print("INITIAL K")
    print(k)
    print(min_test)

    while adjustment > threshold:
        adjustment_change = False

        # update adjustment*******
        #update k ***** with adjustment
        
        # going right ****
        # Going right (incresing k)
        k = k_optimal+adjustment
        if(k <= N)and(k >= 1)and(k not in tested_ks):  #If the k is valid (within the range) and not used already
            num_tests = calculate_test(patients, k)
            if num_tests < min_test:    # improvement
                print('going right')
                print('num_tests, min_test, k')
                print(num_tests, min_test, k)
                min_test = num_tests
                k_optimal = k
                adjustment_change = True
        
        #If no improvement, try going left
        # Going left (decresing k)
        if adjustment_change == False:
            k = k_optimal-adjustment
            if(k <= N)and(k >= 1)and(k not in tested_ks):  #If the k is valid (within the range) and not used already
                num_tests = calculate_test(patients, k)
                if num_tests < min_test:    # improvement
                    print('going left')
                    print('num_tests, min_test, k')
                    print(num_tests, min_test, k)
                    min_test = num_tests
                    k_optimal = k
                    adjustment_change = True

        #If no improvement, try decreeasing adjustment
        if adjustment_change == False:  #*+*+*+*+*+**
            adjustment = round( adjustment*(1-adjustment_rate) )   #*****
            print('HEREEEEEEE: adjustment', adjustment)
        
        print('adjustment: ', adjustment)
        print('k: ', k_optimal)
        print('min_test: ', min_test)

    return k_optimal, min_test
        
"""
