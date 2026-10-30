#!/usr/bin/python3
    # Iñigo Auza de la Mora - Student ID 2824537

import random

from matplotlib import pyplot as plt


# The Bandit

bandit = [.3, .7, .4]



def sample_bandit_arm(arm):
    p = bandit[arm] # Uknown probability  0 ≤ p ≤ 1

    if random.uniform(0, 1) < p:
        return 1
    else:
        return 0


def mean_beta_distribution(a,b):
    return ( 1/ (1+(b/a)) )

def variance_beta_distribution(a,b):
    return ( (a+b)/(pow((a+b),2)*(a+b+1)) )







def thomson(bandit):
    # Thomson

    a = []  #Initialize a and b as empty lists to hold a,b for every arm
    for arm in bandit:
        a.append(1)
        #b.append(1)    #You can, or just copy them at the end
    b = a.copy()


    max_arm = 0
    #max_mean = mean_beta_distribution(a,b)

    epochs = 300
    for i in range (epochs-1):

        max_mean = 0    #Reset mean to compare again
        for arm in range(0,len(bandit)):
            mean = mean_beta_distribution(a[arm], b[arm])
            #print('mean: ', mean)
            if mean > max_mean:
                max_arm = arm
                max_mean = mean

        sample = sample_bandit_arm(max_arm)
        if sample == 1:
            a[max_arm] += 1
        else:   # sample == 0
            b[max_arm] += 1
        # or 
        """
        a[max_arm] += sample
        b[max_arm] += (1-sample)
        """


    print('THOMPSON')
    print('a: ', a)
    print('b: ', b)

    print("Max arm: ", max_arm)
    print("Max arm mean: ", max_mean)


    return a, b, max_arm





def UCB(bandit, c_):
    #Clean a, b data
    a = []  #Initialize a and b as empty lists to hold a,b for every arm
    for arm in bandit:
        a.append(1)
        #b.append(1)    #You can, or just copy them at the end
    b = a.copy()


        # UCB
    max_arm = 0
    c = c_

    epochs = 300
    for i in range (epochs-1):

        max_ucb = 0    #Reset mean to compare again
        for arm in range(0,len(bandit)):
            ucb = mean_beta_distribution(a[arm], b[arm]) + (c * variance_beta_distribution(a[arm], b[arm]))
            #print('ucb: ', ucb)
            if ucb > max_ucb:
                max_arm = arm
                max_ucb = ucb

        sample = sample_bandit_arm(max_arm)
        if sample == 1:
            a[max_arm] += 1
        else:   # sample == 0
            b[max_arm] += 1
        # or 
        """
        a[max_arm] += sample
        b[max_arm] += (1-sample)
        """

    print('UCB')
    print('a: ', a)
    print('b: ', b)

    print("Max arm: ", max_arm)
    print("Max UCB: ", max_ucb)

    max_mean = mean_beta_distribution(a[max_arm], b[max_arm]) 

    print("Max mean: ", max_mean)

    return a, b, max_arm


"""
for c in range(1, 11):   # 1 ≤ c ≤ 5
    print("UCB: ", c)
    UCB(bandit, c)
"""




# Thumpson 10 run calculation
thompson_as = []
thompson_bs = []
thompson_arms = []

for i in range(10):
    print(i)
    a, b, max_arm = thomson(bandit)
    thompson_as.append(a)
    thompson_bs.append(b)
    thompson_arms.append(max_arm)








# UCB c = 1 10 run calculation
ucb_1_as = []
ucb_1_bs = []
ucb_1_arms = []
c_1 = 1

for i in range(10):
    print(i)
    a, b, max_arm = UCB(bandit, c_1)
    ucb_1_as.append(a)
    ucb_1_bs.append(b)
    ucb_1_arms.append(max_arm)


# UCB c = 3 10 run calculation
ucb_3_as = []
ucb_3_bs = []
ucb_3_arms = []
c_3 = 3

for i in range(10):
    print(i)
    a, b, max_arm = UCB(bandit, c_3)
    ucb_3_as.append(a)
    ucb_3_bs.append(b)
    ucb_3_arms.append(max_arm)


# UCB c = 5 10 run calculation
ucb_5_as = []
ucb_5_bs = []
ucb_5_arms = []
c_5 = 5

for i in range(10):
    print(i)
    a, b, max_arm = UCB(bandit, c_5)
    ucb_5_as.append(a)
    ucb_5_bs.append(b)
    ucb_5_arms.append(max_arm)



# UCB c = 10 10 run calculation
ucb_10_as = []
ucb_10_bs = []
ucb_10_arms = []
c_10 = 10

for i in range(10):
    print(i)
    a, b, max_arm = UCB(bandit, c_10)
    ucb_10_as.append(a)
    ucb_10_bs.append(b)
    ucb_10_arms.append(max_arm)
















# Thumpson 10 run print
print()
print("Thumpson 10 run")
print('thompson_as', thompson_as)
print('thompson_bs', thompson_bs)
print('thompson_arms', thompson_arms)

print("Averages")
#https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
average_a = [sum(x) for x in zip(*thompson_as)]
average_b = [sum(x) for x in zip(*thompson_bs)]
"""
for arm in bandit:
    for a in a_s:
        a[arm]
"""
print('average_a', average_a)
print('average_b', average_b)

mean_beta = []

for arm in range(0,len(bandit)):
    mean_arm = mean_beta_distribution(average_a[arm], average_b[arm])
    mean_beta.append(mean_arm)
print('mean_beta')
print(mean_beta)








# c = 1
# UCB 10 run print
print()
print('UCB, c: ', c_1)
print("UCB 10 run")
print('UCB_as', ucb_1_as)
print('UCB_bs', ucb_1_bs)
print('UCB_arms', ucb_1_arms)

print("Averages")
#https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
average_a = [sum(x) for x in zip(*ucb_1_as)]
average_b = [sum(x) for x in zip(*ucb_1_bs)]
"""
for arm in bandit:
    for a in a_s:
        a[arm]
"""
print('average_a', average_a)
print('average_b', average_b)

mean_beta = []

for arm in range(0,len(bandit)):
    mean_arm = mean_beta_distribution(average_a[arm], average_b[arm])
    mean_beta.append(mean_arm)
print('mean_beta')
print(mean_beta)




# c = 3
# UCB 10 run print
print()
print('UCB, c: ', c_3)
print("UCB 10 run")
print('UCB_as', ucb_3_as)
print('UCB_bs', ucb_3_bs)
print('UCB_arms', ucb_3_arms)

print("Averages")
#https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
average_a = [sum(x) for x in zip(*ucb_3_as)]
average_b = [sum(x) for x in zip(*ucb_3_bs)]
"""
for arm in bandit:
    for a in a_s:
        a[arm]
"""
print('average_a', average_a)
print('average_b', average_b)

mean_beta = []

for arm in range(0,len(bandit)):
    mean_arm = mean_beta_distribution(average_a[arm], average_b[arm])
    mean_beta.append(mean_arm)
print('mean_beta')
print(mean_beta)




# c = 5
# UCB 10 run print
print()
print('UCB, c: ', c_5)
print("UCB 10 run")
print('UCB_as', ucb_5_as)
print('UCB_bs', ucb_5_bs)
print('UCB_arms', ucb_5_arms)

print("Averages")
#https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
average_a = [sum(x) for x in zip(*ucb_5_as)]
average_b = [sum(x) for x in zip(*ucb_5_bs)]
"""
for arm in bandit:
    for a in a_s:
        a[arm]
"""
print('average_a', average_a)
print('average_b', average_b)

mean_beta = []

for arm in range(0,len(bandit)):
    mean_arm = mean_beta_distribution(average_a[arm], average_b[arm])
    mean_beta.append(mean_arm)
print('mean_beta')
print(mean_beta)




# c = 1
# UCB 10 run print
print()
print('UCB, c: ', c_10)
print("UCB 10 run")
print('UCB_as', ucb_10_as)
print('UCB_bs', ucb_10_bs)
print('UCB_arms', ucb_10_arms)

print("Averages")
#https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
average_a = [sum(x) for x in zip(*ucb_10_as)]
average_b = [sum(x) for x in zip(*ucb_10_bs)]
"""
for arm in bandit:
    for a in a_s:
        a[arm]
"""
print('average_a', average_a)
print('average_b', average_b)

mean_beta = []

for arm in range(0,len(bandit)):
    mean_arm = mean_beta_distribution(average_a[arm], average_b[arm])
    mean_beta.append(mean_arm)
print('mean_beta')
print(mean_beta)