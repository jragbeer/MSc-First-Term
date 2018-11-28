import os
import glob
import datetime

def make_dictoftext():
    all_files = glob.glob(os.path.join(path, "*"))
    folders = [x.split('\\\\')[0].split('\\')[1] for x in all_files]
    folders.remove('README.TXT')
    dicttext = {}
    for x in folders:
        files = list(glob.glob(os.path.join(path + '{}/'.format(x), "*.txt")))
        for y in files:
            z = y.split('\\\\')[0].split('\\')[1]
            with open('bbcsport/{}/{}'.format(x,z), 'r') as a:
                text = a.read()
                arrayoftext = [x.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('"', '').replace("'", '').replace(';', '').replace(':', '') for x in text.split()]
                dicttext['{}_{}'.format(x,z)] = arrayoftext
    return dicttext
def make_invertedindex(dictoftext):
    all_words = []
    for x in dictoftext.keys():
        for y in dictoftext[x]:
            all_words.append(y)
    allwords = set(all_words)
    invertedindexdict = {t: {'inverted index':[str(x) for x in dictoftext.keys() if t in dictoftext[x]]} for t in allwords}
    for i in invertedindexdict:
        invertedindexdict[i]['freq'] = len(invertedindexdict[i]['inverted index'])
    return invertedindexdict

timee = datetime.datetime.now()
path = 'C:/Users/Julien/PycharmProjects/ds8003final/bbcsport/'
dictofalltext = make_dictoftext()
invertedindexdict = make_invertedindex(dictofalltext)
totalnumberofdocuments = len(dictofalltext.keys())
query = 'Manchester sgsgs'
yyy=[]
for x in query.split():
    try:
        yyy.append(invertedindexdict[x]['inverted index'])
    except Exception as e:
        pass
queryresults = [item for sublist in yyy for item in sublist]
print(queryresults)
print('time:',datetime.datetime.now()-timee)
