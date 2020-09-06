import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["school"]
mycollection=mydb['student']
my_many_records=[{"name":"yash","name":"aman","name":"nitin"}]
x=mycollection.insert_many(my_many_records)