import random

rand_num = random.random()

if rand_num < 0.25:
    print('try to go right')
elif rand_num > 0.25 and rand_num < 0.5:
    print('try to go left')
elif rand_num > 0.5 and rand_num < 0.75:
    print('try to go up')
elif rand_num > 0.75 and rand_num < 1:
    print('try to go down')
