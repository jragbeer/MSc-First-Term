import pymongo

client = pymongo.MongoClient()

db = client['test-database']
collection = db['test-collection']

nosql = {'love':[1,2,3],
         'same':{'1':[9,8], '2':[7,6]}}

collection.insert_one(nosql)

print(collection.find_one())