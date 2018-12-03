import pymongo
from bson.objectid import ObjectId
import os
import glob
import datetime
import numpy as np
import sys
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
                arrayoftext = [x.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('"', '').replace("'", '').replace(';', '').replace(':', '').replace('$', '') for x in text.split()]
                dicttext['{}_{}'.format(x,z.split('.')[0])] = arrayoftext
    return dicttext
def make_invertedindex(dictoftext):
    all_words = []
    for x in dictoftext.keys():
        for y in dictoftext[x]:
            all_words.append(y)
    allwords = set(all_words)
    # for each word, count how many documents it is in and add it to a list
    invertedindexdict = {t: {'inverted index':[str(x) for x in dictoftext.keys() if t in dictoftext[x]]} for t in allwords}
    for i in invertedindexdict:
        # count number of documents that the word appears in
        invertedindexdict[i]['freq'] = len(invertedindexdict[i]['inverted index'])
    return invertedindexdict
def make_tfscores(a, listoftext):
    kk = {x:{'hits':a.count(x),'tf':a.count(x)/len(a), 'idf': np.log(totalnumberofdocuments/len([y for y in listoftext if x in dictofalltext[y]])), 'tf-idf': (a.count(x)/len(a)) * (np.log(totalnumberofdocuments/len([y for y in listoftext if x in dictofalltext[y]])))} for x in a}
    return kk
def queryfunction():
    #query function that asks for an input query and a number of how many documents to return
    # outputs the query, number of documents, results in a list, time for execution and then each of the document's
    # list of words is returned
    try:
        query = input('\nplease input a query\n\n')
        if query == 'exit':
            sys.exit()
        numofdocs = int(input('\nHow many documents?\n\n'))
        timee1 = datetime.datetime.now()
        yyy=[]
        for x in query.split():
            try:
                yyy.append(invertedindexdict[str(x)]['inverted index'])
            except Exception as e:
                pass
        #flatten the list of lists of documents to a single, flat list
        queryresults = [item for sublist in yyy for item in sublist]
        if len(queryresults) == 0:
            return
        querysplit = [x for x in query.split()]
        results = []
        for y in queryresults:
            tfidfscore = [alldoctfidfscores[y][x]['tf-idf'] for x in querysplit if y in invertedindexdict[x]['inverted index']]
            zz = len(tfidfscore) / len(querysplit)
            results.append((y,sum(tfidfscore)*zz))

        newlist = sorted(set(results), key = lambda x:x[1], reverse =True)[:numofdocs]
        print('\nQuery: ', query)
        print('\nNumber of Documents: ',numofdocs)
        print('\n{}'.format(newlist))
        print('\ntime: {} seconds'.format(datetime.datetime.now()-timee1))

        for x in newlist:
            print(' ')
            print(x[0])
            print(dictofalltext[x[0]])
    except Exception as e:
        print(str(e))

timee = datetime.datetime.now()
print(timee)
path = 'C:/Users/Julien/PycharmProjects/ds8003final/bbcsport/'

# commented out as this is the set-up phase. It builds the 3 dictionaries that are used and saves them as objects
# in a mongodb database called 'test-database'. Additionally, a local copy of each dictionary is saved as a python pickle

# # DICTIONARY OF ALL ARTICLES AND A LIST OF WORDS FOR EACH ARTICLE
# dictofalltext = make_dictoftext()
#
# # TOTAL NUMBER OF DOCUMENTS IN THE COLLECTION
# totalnumberofdocuments = len(dictofalltext.keys())
#
# # TF-IDF TABLES FOR EACH DOC (AND EACH WORD IN EACH DOC)
# dd = list(dictofalltext.keys())
# alldoctfidfscores = {i: make_tfscores(dictofalltext[i], dd) for i in dd}
# print('time:', datetime.datetime.now() - timee)
#
# # INVERTED INDEX DOCUMENT RETRIEVAL DICTIONARY
# invertedindexdict = make_invertedindex(dictofalltext)
# print('time:', datetime.datetime.now() - timee)
#
# pickle_out = open("dictofalltext.pickle", "wb")
# pickle.dump(dictofalltext, pickle_out)
# pickle_out.close()
#
# pickle_out1 = open("alldoctfidfscores.pickle", "wb")
# pickle.dump(alldoctfidfscores, pickle_out1)
# pickle_out1.close()
#
# pickle_out2 = open("invertedindexdict.pickle", "wb")
# pickle.dump(invertedindexdict, pickle_out2)
# pickle_out2.close()

# pickle_in1 = open("dictofalltext.pickle","rb")
# dictofalltext = pickle.load(pickle_in1)
# pickle_in2 = open("alldoctfidfscores.pickle","rb")
# alldoctfidfscores = pickle.load(pickle_in2)
# pickle_in3 = open("invertedindexdict.pickle","rb")
# invertedindexdict = pickle.load(pickle_in3)


client = pymongo.MongoClient('mongodb+srv://Jay:lovesosa@king-qgrir.azure.mongodb.net/test-database')
db = client['test-database']
collection = db['bigdatafinal']

# collection.insert_one(alldoctfidfscores)
# collection.insert_one(invertedindexdict)
# collection.insert_one(dictofalltext)
#get an id for each of the collections in the mongodb test-database
ids = [x['_id'] for x in collection.find({})]
alldoctfidfscores = collection.find_one({'_id':ObjectId(ids[0])})
invertedindexdict = collection.find_one({'_id':ObjectId(ids[1])})
dictofalltext = collection.find_one({'_id':ObjectId(ids[2])})

#infinite loop, type exit to quit
while True:
    queryfunction()
