import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["school"]
mycollection=mydb['student']
#
# my_many_records_1=[{"name":"yash","rollno":1,"subject":"maths","marks":88}]
# x=mycollection.insert_many(my_many_records_1)
# my_many_records_2=[{"name":"jay","rollno":2,"subject":"science","marks":89}]
# x=mycollection.insert_many(my_many_records_2)
# my_many_records_3=[{"name":"aman","rollno":3,"subject":"hindi","marks":78}]

# x=mycollection.insert_many(my_many_records_3)

myquery = { "marks": "88" }
newvalues = { "$set": { "marks": "79" } }

mycollection.update_one(myquery, newvalues)

for x in mycollection.find():
  print(x)