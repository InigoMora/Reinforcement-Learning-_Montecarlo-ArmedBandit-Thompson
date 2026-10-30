#!/usr/bin/python3
    # Iñigo Auza de la Mora - Student ID 2824537

import numpy as np
import random, time

a =[-1]*21
b =[-1]*21
c =[-1]*21
d_partial = [-100]*19
d = [-1]+d_partial+[20]


reward_map = [a,b,c,d]

#Snake pit
reward_map[1][10] = -100
reward_map[2][10] = -100



"""
a =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b =[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]
c =[42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62]
d =[63,64,65,66,67,68,69,70,71,72,73,74,75,75,77,78,79,80,81,82,83]
"""
a=list(range(0,21)) # 1-21
b=list(range(21,42)) # 22-42
c=list(range(42,63)) # 43-63
d=list(range(63,84)) # 64-84
state_map = [a,b,c,d]   #unique numbers for every state


a =[False]*21
b =[False]*21
c =[False]*21
d_partial = [True]*19
d = [False]+d_partial+[True]

terminal_map = [a,b,c,d]
#Snake pit  #Not specified *****
terminal_map[1][10] = True
terminal_map[2][10] = True




def enviromnent(state, action):
    action_probability = 1  #Not implemented******

        # initializing values
    new_state = state
    reward = 0
    is_terminal = False

    # This is how we can tell where in space that state is
    row, column = divmod(state, 21)

    # Movements mapping
        # up    0
        # down  1
        # left  2
        # right 3
    
    #check for limits
        #move up
    if action == 0:
        if row == 0:    # in the up-most row
            new_state = state   # The agent can't go any higher
        else:
            new_state = state_map[row-1][column]
        #move down
    if action == 1:
        if row == 3:    # in the down-most row
            new_state = state   # The agent can't go any lower
        else:
            new_state = state_map[row+1][column]
        #move left
    if action == 2:
        if column == 0:    # in the left-most column
            new_state = state   # The agent can't go left
        else:
            new_state = state_map[row][column-1]
        #move right
    if action == 3:
        if column == 20:    # in the right-most column
            new_state = state   # The agent can't go right
        else:
            new_state = state_map[row][column+1]

    row, column = divmod(new_state, 21)
    reward = reward_map[row][column]
    is_terminal = terminal_map[row][column]

    return new_state, reward, is_terminal








def sarsa_policy(state, e=0):   # if no epsilon value (exploration value) is given, defaule to 0
    if random.uniform(0, 1) > e:    # if epsilon (exploration) does not happen
        action = np.argmax(q_values[state])
        return action
    else:
        action = random.randint(0, 3)    #There are 4 admissible moves: 0, 1, 2, 3
        return action
    
def q_learning_policy(state, e=0):  # In this case, choosing the next action is the same
    sarsa_policy(state, e)


def sarsa_new_q_value(q_values, curr_state, action , reward, next_state, next_action, alpha, gamma):
    new_q_value =  q_values[curr_state][action] + alpha * (reward + (gamma * q_values[next_state][next_action]) - q_values[curr_state][action])
    return new_q_value

def q_learning_new_q_value(q_values, curr_state, action , reward, next_state, next_action, alpha, gamma):
    new_q_value =  q_values[curr_state][action] + alpha * (reward + (gamma * q_values[next_state][np.argmax(q_values[next_state])]    ) - q_values[curr_state][action])
    return new_q_value









q_values= np.zeros(shape=(84,4))    #84 states, 4 actions each



epochs = 600    # number of episodes 


def play_episode(agent_policy, q_value_update_method, buffer=False):

        # Parameters / Values
    epsilon = .005   # Exploration probability    #NOTE: Keep between 0 and .1
    alpha = .3  # Learning rate
    gamma = .7  #Discount factor

    curr_state = 63 #This is the initial state, at 3,0
    action = agent_policy(curr_state, epsilon)

    total_reward = 0

    episode_lenght = 0

    replay_buffer = []

    terminal = False
    while not terminal:

        next_state, reward, terminal = enviromnent(curr_state, action)
        next_action = agent_policy(next_state, epsilon)

        total_reward += reward

        if buffer == True:
            replay_buffer.append([curr_state, action, reward, next_state])

        # update q value for state, action tuple
            #based on the equation
            #Now generalized
            #SARSA
        #q_values[curr_state][action] = sarsa_new_q_value(q_values, curr_state, action , reward, next_state, next_action, alpha, gamma)
            #Q-Learning
        #q_values[curr_state][action] = q_learning_new_q_value(q_values, curr_state, action , reward, next_state, next_action, alpha, gamma)
        q_values[curr_state][action] = q_value_update_method(q_values, curr_state, action , reward, next_state, next_action, alpha, gamma)

        curr_state = next_state
        action = next_action

        episode_lenght+=1

    if buffer == True:
        return total_reward, replay_buffer
    return total_reward






def play_out_game(q_values):
        # Movements mapping
            # up    0
            # down  1
            # left  2
            # right 3

    curr_state = 63 #This is the initial state, at 3,0
    action = np.argmax(q_values[curr_state])

    visited_states = [curr_state]

    print("Initial state: ", curr_state, divmod(curr_state, 21))
    print(['up', 'down', 'left', 'right'][action])

    terminal = False
    while not terminal:
        next_state, reward, terminal = enviromnent(curr_state, action)
        print(next_state)
        action = np.argmax(q_values[next_state])
        print(['up', 'down', 'left', 'right'][action])

        if next_state in visited_states:
            print('Error, agent stuck in a loop')
            break
        visited_states.append(next_state)
        curr_state = next_state

    view_map = np.zeros(shape=(4,21))
    view_map= view_map.tolist()
    for state in visited_states:
        row, column = divmod(state, 21)
        view_map[row][column]= 'X'
    
    for line in view_map:
        print(line)
    
        
def run_buffer(q_values, buffer):
    #buffer includes:
        #[[S,A,R,S']]
    new_q_values = q_values
    buffer_reversed = buffer
    buffer_reversed.reverse()

    #These are hardcoded for time constraint    #*****
    next_action = None
    alpha = .3  # Learning rate
    gamma = .7  #Discount factor 

    for i in range(len(buffer_reversed)):
        curr_state, action, reward, next_state = buffer_reversed[i]
        new_q_values[curr_state][action] = q_learning_new_q_value(q_values, curr_state, action , reward, next_state, next_action, alpha, gamma)

    return new_q_values








print()
    #TRAIN SARSA
random.seed(1)  # 1, 2          #3, epsilon = .05

for episode in range(epochs):
    episode_reward = play_episode(sarsa_policy, sarsa_new_q_value)
    #print(episode_reward)
    #print(q_values)
    #time.sleep(3)

print("SARSA")
play_out_game(q_values)



print()
q_values= np.zeros(shape=(84,4))    #84 states, 4 actions each (there are some exeptions****)

    #TRAIN Q-Learning
random.seed(1)

for episode in range(epochs):
    episode_reward = play_episode(sarsa_policy, q_learning_new_q_value)
    #print(episode_reward)
    #print(q_values)
    #time.sleep(3)

print("Q-Learning")
play_out_game(q_values)



print()
q_values= np.zeros(shape=(84,4))    #84 states, 4 actions each (there are some exeptions****)

    #TRAIN Q-Learning with buffer
random.seed(1)  #1-4+7-12, 5, 6, 11

for episode in range(epochs):
    episode_reward, buffer = play_episode(sarsa_policy, q_learning_new_q_value,buffer=True)
    q_values = run_buffer(q_values, buffer)

print("Q-Learning with buffer")
play_out_game(q_values)