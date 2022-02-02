# Anthony Milton
# 01/31/2022
#Module 5 MongoDB Assignment

#import module
from pymongo import MongoClient

#Assign URL, client, and database variables
url ="mongodb+srv://admin:admin@cluster0.bgehd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

#Print a list of the names of all collections in the database (only one right now)
print(db.list_collection_names())
