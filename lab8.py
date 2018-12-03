import numpy as np

np.random.seed(14235)

var = 10

a = [(np.random.randint(-var,var)*0.1+1,np.random.randint(-var,var)*0.1+1,0) for x in range(20)]
b = [(np.random.randint(-var,var)*0.1+3,np.random.randint(-var,var)*0.1+3,1) for x in range(20)]

dataset = a+b
np.random.shuffle(dataset)

train = dataset[:32]
test = dataset[32:]

p_c0 = len([x for x in dataset if x[2] == 0])/len(dataset)
p_c1 = len([x for x in dataset if x[2] == 1])/len(dataset)

mean_c0 = [np.mean([x[0] for x in a]), np.mean([x[1] for x in a])]
mean_c1 = [np.mean([x[0] for x in b]), np.mean([x[1] for x in b])]

meanvec = np.array([mean_c0,
           mean_c1]).reshape((2,2))

def make_cov(m):
    u = [x[0] for x in m]
    i = [x[1] for x in m]
    xx = np.column_stack([u,i])
    xx -= xx.mean(axis = 0)
    cc = np.dot(xx.T, xx.conj())/len(u)
    return cc

class0covmatrix = make_cov(a)
class1covmatrix = make_cov(b)

def func(y, mvec,logpc, covmat, d):
    y = np.array([y[0],y[1]])
    first = d*np.log(2*np.pi)/2
    second = 0.5*np.log(np.linalg.det(covmat))
    third = 0.5*np.dot(np.array(y-mvec).T,np.linalg.inv(covmat))
    third2 = np.dot(third,np.array(y-mvec))
    return np.log(logpc)-first-second-third2

for x in dataset:
    class1 = func(x, mean_c0, p_c0, class0covmatrix, 2)
    class2 = func(x, mean_c1, p_c1, class1covmatrix, 2)
    if class1 > class2:
        print(x, '0')
    else:
        print(x, '1')
