import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

fig = plt.figure()
ax0 = fig.add_subplot(121)
ax1 = fig.add_subplot(122)

def ed(q,w):
    first = (q[0]-w[0])**2
    second = (q[1] - w[1]) ** 2
    return np.sqrt(first + second)

np.random.seed(3)
randomfactor = 10.3
a = [45, 39] # point 1 red
#dataset generated around point 1
d = [a[0]+np.random.randint(-5, 5)*randomfactor for x in range(20)]
e = [a[1]+np.random.randint(-5, 5)*randomfactor for x in range(20)]

b = [19, 27] #point 2 blue
#dataset generated around point 2
f = [b[0]+np.random.randint(-5, 5)*randomfactor for x in range(20)]
g = [b[1]+np.random.randint(-5, 5)*randomfactor for x in range(20)]

reds = [[f[x], g[x]] for x in range(len(f))]
blues = [[d[x], e[x]] for x in range(len(f))]
pp = reds+blues
print(pp)
shuffle(pp)
new = []
truelabel = []
points = []
#0 is blue
#1 is red
for x in pp:
    if x in reds:
        if ed(x, a) > ed(x, b):
            points.append(x)
            truelabel.append(1)
            new.append(1)
        else:
            points.append(x)
            truelabel.append(1)
            new.append(0)
    elif x in blues:
        if ed(x, a) > ed(x, b):
            points.append(x)
            truelabel.append(0)
            new.append(1)
        else:
            points.append(x)
            truelabel.append(0)
            new.append(0)

for x in range(len(new)):
    if new[x] != truelabel[x]:
        print('At point: ', points[x],", the prediction is wrong")
ax0.set_title('TRUTH')
ax0.scatter(a[0], a[1], s=100, color = 'red')
ax0.scatter(b[0], b[1], s=100, color = 'blue')
ax0.plot(f, g, 'bo', alpha = 0.5)
ax0.plot(d, e, 'ro', alpha = 0.5)
newred = []
newblue = []
for y, u in enumerate(new):
    if u == 0:
        newred.append(points[y])
    else:
        newblue.append(points[y])

ax1.scatter(a[0], a[1], s=100, color = 'red')
ax1.scatter(b[0], b[1], s=100, color='blue')
ax1.set_title('PREDICTIONS')
ax1.plot([x[0] for x in newred], [x[1] for x in newred], 'ro', alpha = 0.5)
ax1.plot([x[0] for x in newblue], [x[1] for x in newblue], 'bo', alpha = 0.5)

plt.show()