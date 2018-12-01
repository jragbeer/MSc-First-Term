import pymongo
import os
import glob
import datetime
import numpy as np
import pickle

def make_dictoftext():
    all_files = glob.glob(os.path.join(path, "*")) #list of all files/directories, absolute path
    folders = [x.split('\\\\')[0].split('\\')[1] for x in all_files] #names of all folders
    folders.remove('README.TXT') #remove readme
    #create a dictionary of the corpus. Each entry is represented 'x_y':z where x is the folder name, y is the document name inside that folder
    # and z is a string with the text inside the file
    dicttext = {}
    for x in folders:
        files = list(glob.glob(os.path.join(path + '{}/'.format(x), "*.txt")))
        for y in files:
            z = y.split('\\\\')[0].split('\\')[1]
            with open(path+'/{}/{}'.format(x,z), 'r') as a:
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
def make_tfscores(article, a):
    kk = {x:{'hits':a.count(x),'tf':a.count(x)/len(a), 'idf': np.log(totalnumberofdocuments/len([y for y in dictofalltext.keys() if x in dictofalltext[y]])), 'tf-idf': (a.count(x)/len(a)) * (np.log(totalnumberofdocuments/len([y for y in dictofalltext.keys() if x in dictofalltext[y]])))} for x in a}
    return kk

timee = datetime.datetime.now()
path = 'C:/Users/J_Ragbeer/PycharmProjects/final/bbcsport/'
# #DICTIONARY OF ALL ARTICLES AND A LIST OF WORDS FOR EACH ARTICLE
# dictofalltext = make_dictoftext()
#
# # TOTAL NUMBER OF DOCUMENTS IN THE COLLECTION
# totalnumberofdocuments = len(dictofalltext.keys())
#
# # TF-IDF TABLES FOR EACH DOC (AND EACH WORD IN EACH DOC)
# alldoctfidfscores = {i:make_tfscores(i,dictofalltext[i]) for i in dictofalltext.keys()}
# print(alldoctfidfscores)
# print('time:',datetime.datetime.now()-timee)
# # INVERTED INDEX DOCUMENT RETRIEVAL DICTIONARY
# invertedindexdict = make_invertedindex(dictofalltext)
# print('time:',datetime.datetime.now()-timee)
#
# pickle_out = open("dictofalltext.pickle","wb")
# pickle.dump(dictofalltext, pickle_out)
# pickle_out.close()
#
# pickle_out1 = open("alldoctfidfscores.pickle","wb")
# pickle.dump(alldoctfidfscores, pickle_out1)
# pickle_out1.close()
#
# pickle_out2= open("invertedindexdict.pickle","wb")
# pickle.dump(invertedindexdict, pickle_out2)
# pickle_out2.close()

pickle_in1 = open("dictofalltext.pickle","rb")
dictofalltext = pickle.load(pickle_in1)
pickle_in2 = open("alldoctfidfscores.pickle","rb")
alldoctfidfscores = pickle.load(pickle_in2)
pickle_in3 = open("invertedindexdict.pickle","rb")
invertedindexdict = pickle.load(pickle_in3)

print(alldoctfidfscores)

query = 'Manchester cross'

yyy=[]
for x in query.split():
    try:
        yyy.append(invertedindexdict[str(x)]['inverted index'])
    except Exception as e:
        pass
queryresults = [item for sublist in yyy for item in sublist]
sumoftfidf = 0
for x in query.split():
    for y in queryresults:
        if x in dictofalltext[y]:
            try:
                print(x,y,alldoctfidfscores[y][x]['tf-idf'])
                sumoftfidf += alldoctfidfscores[y][x]['tf-idf']
            except:
                pass
        else:
            print(x,y)
            pass
Q = len([x for x in query.split()])
print(sumoftfidf)
print('time:',datetime.datetime.now()-timee)



# client = pymongo.MongoClient()
# db = client['test-database']
# collection = db['test-collection']
# nosql = {'love':[1,2,3],
#          'same':{'1':[9,8], '2':[7,6]}}
# collection.insert_one(nosql)
# print(collection.find_one())