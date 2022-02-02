# Anthony Milton
# 02/02/2022
#Module 5 MongoDB Queries Assignment

#import module
from pymongo import MongoClient

#Assign URL, client, database, and collection variables
url ="mongodb+srv://admin:admin@cluster0.bgehd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

collection = db.students


col_query = collection.find()

print("------DISPLAYING RESULTS FROM FIND() QUERY ON THE STUDENTS DATABASE------")
for x in col_query:
    sid = x["student_id"]
    fname = x["first_name"]
    lname = x["last_name"]

    print(f"""
student_id = {sid}
first_name = {fname}
last_name = {lname}
""")

print("------------------------------------------------------------")
