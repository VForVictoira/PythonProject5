from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['MongoDB_Test2']
collection = database['test']

# 插入数据

data = {'id':4418,'name':'SawyerWang','age':28,'salary':23000}
#collection.insert_one(data)

# 插入多个数据，是字典的列表
more_data = [
    {'id': 2, 'name': '张三', 'age': 10, 'salary': 0},
{'id': 3, 'name': '李四', 'age': 30, 'salary': -100},
{'id': 4, 'name': '五', 'age': 40, 'salary': 1000},
{'id': 5, 'name': '外国人', 'age': 50, 'salary': '未知'},
]
#collection.insert_many(more_data)

content1= [x for x in (collection.find({'age':28}))]
# 限定只返回 id 和 name
# Value是0或者1,0表示不返回这个字段，1表示返回这个字段
# 其中_id比较特殊，必须人工指定它的值为0，这样才不会返回
# 而对于其他数据，应该统一使用返回，或者统一使用不返回
content2 = [x for x in collection.find({'age':28},{'_id':0,'id':4418,'name':1})]

print(content1)
print(content2)
