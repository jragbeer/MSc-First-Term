import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(1324)
try:
    k = int(input('Please pick K\n'))
except Exception as e:
    print('Must pick a number')
    k = int(input('Please pick K\n'))

def euclidean_distance(curpoint,othpoint):
    return np.sqrt((curpoint[0]-othpoint[0])**2 + (curpoint[1]-othpoint[1])**2)

a = [[5+0.1*np.random.randint(-10,10), 3+0.1*np.random.randint(-10,10), 0] for x in np.arange(20)]
b = [[8+0.1*np.random.randint(-10,10), 1+0.1*np.random.randint(-10,10), 1] for x in np.arange(20)]
c = a+b
np.random.shuffle(c)

new = [6.5+0.1*np.random.randint(-10,10), 2+0.1*np.random.randint(-10,10)]

distances = sorted([[euclidean_distance(new, x),x] for x in c], key = lambda x: x[0])

nums = [x[1][2] for x in distances[:k]]
if sum(nums)/len(nums)> 0.5:
    print('should be blue')
    z = 'blue'
else:
    print('should be red')
    z = 'red'

plt.scatter([x[0] for x in a],[x[1] for x in a], c = 'red') #red is 0
plt.scatter([x[0] for x in b],[x[1] for x in b], c = 'blue') #blue is 1
plt.scatter(new[0], new[1], c=z, marker = 'x', s = 30)
plt.show()