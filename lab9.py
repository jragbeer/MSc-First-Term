import pandas as pd
import numpy as np
path = 'C:/Users/J_Ragbeer/Downloads/'
df = pd.read_csv(path+'pca_data.csv', header = None, names = ['1', '2'])
df['new1'] = df['1']-df['1'].mean()
df['new2'] = df['2']-df['2'].mean()
cov = np.cov( df['new2'],df['new1'])
qq= np.array([df['new1'].values, df['new2'].values])
eigvals, eigvec = np.linalg.eig(cov)
z = [np.matmul(eigvec, [qq[0][i], qq[1][i]]) for i in range(len(qq[0]))]
print(z)
