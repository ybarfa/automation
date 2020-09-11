import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["school"]
mycollection=mydb['student']
myquery = { "name": "aaditya" }
newvalues = { "$set": { "name": "Yash" } }

mycollection.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycollection.find():
  print(x)

