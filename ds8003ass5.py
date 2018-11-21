import pandas as pd
df = pd.read_csv('integer_list.txt', header = None, names= ['nums'])
odds= [x for x in df.values if x%2 != 0]
evens=[x for x in df.values if x%2 == 0]
print(len(odds), 'len odds', '\n{}'.format(len(evens)), 'len evens ')
print('_'*15)
df = pd.read_csv('dept_salary.txt', header = None, names= ['Department', 'Salary'], delimiter=' ')
print(df.groupby(['Department'])['Salary'].sum())
print('_'*15)
with open('shakespeare_100.txt', 'r') as e:
    allwords = [x.replace(',', '').replace('.', '').replace(':', '').replace(' ', '').replace('/', '').replace('!', '').replace('?', '') for x in e.read().split()]
    df = pd.Series(allwords)
    print(df.value_counts()[:10])
    print(df.value_counts()[-10:])
#########################################################
print('/'*65)
import pandas as pd
print(len([x for x in pd.read_csv('integer_list.txt', header = None, names= ['nums']).values if x%2 != 0]), 'len odds', '\n{}'.format(len([x for x in pd.read_csv('integer_list.txt', header = None, names= ['nums']).values if x%2 == 0])), 'len evens\n', '_'*15)
print(pd.read_csv('dept_salary.txt', header = None, names= ['Department', 'Salary'], delimiter=' ').groupby(['Department'])['Salary'].sum(), '\n', '_'*15)
print('TOP (descending): {}\nBOTTOM (descending):\n{}'.format(pd.Series([x.replace(',', '').replace('.', '').replace(':', '').replace(' ', '').replace('/', '').replace('!', '').replace('?', '') for x in open('shakespeare_100.txt', 'r').read().split()]).copy().value_counts()[:10], pd.Series([x.replace(',', '').replace('.', '').replace(':', '').replace(' ', '').replace('/', '').replace('!', '').replace('?', '') for x in open('shakespeare_100.txt', 'r').read().split()]).copy().value_counts()[-10:]))
