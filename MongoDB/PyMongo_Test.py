from pymongo import MongoClient
#client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://admin:a123456!@192.168.0.109:27017')
database = client.MongoDB_Test
collection = database.test1

#data = {'id':4418,'name':'SawyerWang','age':28,'salary':23000}
#collection.insert_one(data)

more_data = [
    {'id':4419,'name':'ZhenXin','age':21,'salary':99999},
    {'id':4410,'name':'Zhangshan','age':22,'salary':12123},
    {'id':4411,'name':'ZhengSang','age':24,'salary':93199}
]
collection.insert_many(more_data)
'''try:
    client = MongoClient('mongodb://sawyerwang:a123456!@192.168.0.109:27017')
    database = client.MongoDB_Test
    collection = database.test1
    print("Connected to MongoDB successfully!")

except Exception as e:
    print(f"Error: {e}")'''

