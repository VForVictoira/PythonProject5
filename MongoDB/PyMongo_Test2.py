from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['MongoDB_Test2']
collection = database['test']

# 插入数据

data = {'id':4418,'name':'SawyerWang','age':28,'salary':23000}
collection.insert_one(data)

