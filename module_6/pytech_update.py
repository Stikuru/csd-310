# Anthony Milton
# 02/07/2022
#Module 6 Pytech Assignment

#import module
from pymongo import MongoClient

#Assign URL, client, database, and collection variables
url ="mongodb+srv://admin:admin@cluster0.bgehd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

collection = db.students

col_query = collection.find()

#do the first query to show all documents in collection
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

#update the 1007 document, params below
og_search = {"student_id":1007}
update_values = {"$set": {"last_name":"CantSeeMe"}}

collection.update_one(og_search,update_values)

#print after finding new 1007 value

result = collection.find_one({"student_id":1007})

print("\n------DISPLAYING RESULTS FROM FIND QUERY ON THE STUDENTS DATABASE FOR ID 1007------")
print(f"""
student_id = {result["student_id"]}
first_name = {result["first_name"]}
last_name = {result["last_name"]}
""")

print("------------------------------------------------------------")