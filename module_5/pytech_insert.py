# Anthony Milton
# 02/02/2022
#Module 5 MongoDB Insertion Assignment

#import module
from pymongo import MongoClient

#Assign URL, client, database, and collection variables
url ="mongodb+srv://admin:admin@cluster0.bgehd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

collection = db.students

#Delete all previous entries (Since while testing this code just keeps creating duplicates, at least the way it is currently)
collection.delete_many({})

#Create student dictionary
students = [
    {"student_id":1007,"first_name":"John","last_name":"Cena"},
    {"student_id":1008,"first_name":"Bruno","last_name":"Madrigal"},
    {"student_id":1009,"first_name":"Emma","last_name":"Watson"}
]

#Create student entry for each student, prints result
for x in students:
    x_id = collection.insert_one(x).inserted_id
    sid = str(x["student_id"])
    
    print("Student with ID of "+sid+", named "+x["first_name"]+" "+x["last_name"]+", was inserted with the document id of "+str(x_id))
