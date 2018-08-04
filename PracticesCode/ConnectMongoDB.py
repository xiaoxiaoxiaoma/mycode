import pymongo

# connect the database of mongodb
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# create a database
mydb = myclient["runoobdb"]

# create a collection
mycol = mydb["sites"]

# create a file
mydict = {"name": "RUNOOB", "alexa": "10001", "url": "https://www.runoob.com"}
# insert a file to database of mongodb
mycol.insert_one(mydict)

#create many files
mylist = [
    {"name": "Taobao", "alexa": "100", "url": "https：//www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]
mycol.insert_many(mylist)

#create many files with id
mylist1 = [
    {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
    {"_id": 2, "name": "Google", "address": "Google搜索"},
    {"_id": 3, "name": "Facebook", "address": "脸书"},
    {"_id": 4, "name": "Taobao", "address": "淘宝"},
    {"_id": 5, "name": "Zhihu", "address": "知乎"}
]
z = mycol.insert_many(mylist1)
print(z)

#find the first files from the "mycol" collection
f1 = mycol.find_one()
print(f1)

#find all the files from "mycol" collection
for x in mycol.find():
    print(x)

#find the specified files from collection.only display name and alexa
for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
    print(x)

myquery = {"name": "RUNOOB"}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# Advanced query
myquery1 = {"name": {"$gt": "H"}}
mydoc1 = mycol.find(myquery1)
for x in mydoc1:
    print(x)

# Regular expression
myquery2 = {"name": {"$regex": "^R"}}
mydoc2 = mycol.find(myquery2)
for x in mydoc2:
    print(x)

# reture the specified number of files
myresult = mycol.find().limit(3)
for x in myresult:
    print(x)

# modify the data,update_one modify the first file of that collection
myupdate = {"alexa": "10000"}
newvalues = {"$set": {"alexa": "12345"}}
mycol.update_one(myupdate, newvalues)

# modify the data,update_many modify all the file,which match the conditions
myupdate2 = {"name": {"$regex": "^F"}}
newvalues2 = {"$set": {"alexa": "123"}}
mycol.update_many(myupdate2, newvalues2)

# delete one file,which is the first file
myquery3 = {"name": "Taobao"}
mycol.delete_one(myquery3)

# delete all the files which match the conditions
myquery4 = {"name": {"$regex": "^F"}}
mycol.delete_many(myquery4)

# delete all the files from that collection
s = mycol.delete_many({})
print(s.deleted_count, "file deleted")

# delete the collection
mycol.drop()

# sort the files that we find (The order)
mydoc3 = mycol.find().sort("alexa")
for x in mydoc:
    print(x)

# sort the files that we find (Reverse order)
mydoc4 = mycol.find().sort("alexa", -1)
for x in mydoc:
    print(x)

# show all the database from mongodb
dblist = myclient.list_database_names()
if "runoobdb" in dblist:
    print("That database exist!")

# show all the collections from runoobdb
collectionlist = mydb.list_collection_names()
if "sites" in collectionlist:
    print("That collection exist!")

print(x)