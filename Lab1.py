import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

a = range(1,101)
b = [1.1*np.log(x)+np.sin(x/2) for x in a]

df = pd.DataFrame(b, index = a)

model = LinearRegression()
model2 = model.fit(np.array(df.index).reshape(-1, 1), df.values)
p = model2.coef_
k = model2.intercept_
print('SKLEARN W_0: ',p)
print('SKLEARN W_1: ',k)
t = np.array([p*x + k for x in a]).reshape(-1,1)
error = mean_squared_error(b, t)

def errorstuff(q,t, w1, w0):
    i = []
    for x in range(len(q)):
        i.append((q[x] - (w1*t[x] + w0))**2)
    return sum(i)/len(q)

wONEtop = sum([a[x]*b[x] - (np.mean([a[x]*b[x] for x in range(len(a))])*len(a)) for x in range(len(a))])
wONEbottom = sum([a[x]**2 - len(a)*np.mean(a)**2 for x in range(len(a))])

wONE = wONEtop/wONEbottom
wZERO = np.mean(b) - wONE*np.mean(a)

dd = [p*wONE+wZERO for p in a]

print('DIY WONE',wONE)
print('DIY WZERO', wZERO)

print('SKLEARN MSE: ',error)
print('DIY MSE: ', errorstuff(b,a, k, p))
plt.scatter(a, b)
plt.plot(a, t, c = 'orange')
plt.scatter(a, dd, c = 'red')
plt.show()