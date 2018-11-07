import pandas as pd
import numpy as np
import random
from matplotlib import style
import matplotlib.pyplot as plt
style.use('ggplot')

pt1 = [3, 4]
pt2 = [12, 14]

np.random.seed(13)

array1x = [np.random.randint(1,10)*0.1*pt1[0] for x in range(20)]
array1y = [np.random.randint(1,10)*0.1*pt1[1] for x in range(20)]
array2x = [np.random.randint(1,10)*0.1*pt2[0] for x in range(20)]
array2y = [np.random.randint(1,10)*0.1*pt2[1] for x in range(20)]

# df = pd.DataFrame(data = {'X':array1x+array2x, 'Y':array1y+array2y, 'class0':[1 for x in range(20)]+ [0 for x in range(20)], 'class1':[0 for x in range(20)]+ [1 for x in range(20)]})
#
# df0 = df[df.class0 == 1].copy()
# df1 = df[df.class1 == 1].copy()
#
# print(df0.mean())
# print(df1.mean())
#
# print(df)
# print(df.cov())
# print(df.mean())
#
# plt.scatter(df.X, df.Y)

X = [[array1x[x], array1y[x], 0] for x in range(len(array1x))]
ARRAY1 = X.copy()

X2 = [[array2x[x], array2y[x], 1] for x in range(len(array1x))]
ARRAY2 = X2.copy()

for i in range(len(X2)):
    X.append(X2[i])

random.shuffle(X)

X_train = X[:33]
X_test = X[33:]


X_train0mean = np.array(X_train)[:,0].mean()
X_train1mean = np.array(X_train)[:,1].mean()


def disfunc(x, d, cov_mat, p_C):
    x0 = x[0]
    x1 =x[1]
    first = d/2*np.log(2*np.pi)
    second = 0.5*np.log(np.linalg.det(cov_mat))
    third = 0.5*(np.dot( np.array([x0-X_train0mean,x1-X_train1mean]).T, np.dot(np.linalg.inv(cov_mat), [x0-X_train0mean,x1-X_train1mean])))
    return np.log(p_C) - first -second - third

for x in ARRAY1:
    print(x)

p_C1 = sum(np.array(X_train)[:,2])/len(X_train)
p_C2 = 1-p_C1

print(p_C1)
print(p_C2)
class1 = []
class0 = []
for x in X:
    if disfunc(x, 2, np.cov(X_train), p_C1)>disfunc(x, 2, np.cov(X_train), p_C2):
        class1.append(x)
    else:
        class0.append(x)

print(class1)
print(class0)


plt.scatter(array1x, array1y, color = 'red')
plt.scatter(array2x, array2y, color = 'blue')
plt.show()