# coding:utf-8
import pymongo

# 创建连接
# 默认端口27017
conn = pymongo.Connection(host='192.168.100.55', port=27017)
# 或者
# conn = pymongo.Connection('192.168.100.55', 27017)
# 或者
# conn = pymongo.Connection('localhost', 27017)


# 连接数据库
db = conn.dbname
# 或者
# db = conn["dbname"]


# 连接集合
coll = db.collectionname
# 或者
# coll = db["collectionname"]


# 查看数据库下的所有集合名称
db.collection_names()
db.collection_names(include_system_collections=False)   #不包括collection,一般指system.index

# 查询
db.collectionname.find()
db.collectionname.find()[0]
# 条件查询
db.collectionname.find({"UserName": "keyword"})
# 指定比较条件查询：$lt（小于），$gt（大于），$lte（小于等于），$gte（大于等于），$ne（不等于）
db.collectionname.find({"age": {"$lt": 30}})
# 查看集合中的一条记录
db.collectionname.find_one()
db.collectionname.find_one({"UserName": "keyword"})

# 查看集合中的多条记录
for item in db.collectionname.find():
    item

for item in db.collectionname.find({"UserName": "keyword"}):
    item

# 查看集合中记录的总数
db.collectionname.find().count()


# 集合查询结果排序
db.collectionname.find().sort("UserName")   # 默认升序
db.collectionname.find().sort("UserName", pymongo.ASCENDING)    # 升序
db.collectionname.find().sort("UserName", pymongo.DESCENDING)   # 降序

# 多列排序
db.collectionname.find().sort([("UserName", pymongo.ASCENDING), ("Email", pymongo.DESCENDING)])


# 增加记录
mydict = {"UserName": "password"}
dict_list = [
    mydict,
    mydict,
]
db.collectionname.insert(mydict)
# 增加一条记录
db.collectionname.insert_one(mydict)
# 增加多条记录
db.collectionname.insert_many(dict_list)


# 删除记录
db.collectionname.remove()  # 全部删除
db.collectionname.remove({"UserName": "keyword"})   # 如果不存在也不会报错


# 更新记录
db.collectionname.update({"UserName": "libing"}, {"$set": {"Email": "libing@126.com", "Password":"1223"}})