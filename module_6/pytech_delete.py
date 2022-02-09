# Anthony Milton
# 02/08/2022
#Module 6 Pytech delete Assignment

#import module
from pymongo import MongoClient

#Assign URL, client, database, and collection variables
url ="mongodb+srv://admin:admin@cluster0.bgehd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
collection = db.students

#function to call and display find query so i don't have to keep re-typing
def ez_find(search_data = "all"):
    if search_data == "all":
        col_query = collection.find()
        print("------DISPLAYING RESULTS FROM FIND( \""+search_data+"\" ) QUERY ON THE STUDENTS DATABASE------")
        for x in col_query:
            sid = x["student_id"]
            fname = x["first_name"]
            lname = x["last_name"]
            print(f"""
                student_id = {sid}
                first_name = {fname}
                last_name = {lname}
                """)
    else:
        col_query = collection.find_one(search_data)
        print("------DISPLAYING RESULTS FROM FIND( \""+str(search_data["student_id"])+" \") QUERY ON THE STUDENTS DATABASE------")
        sid = col_query["student_id"]
        fname = col_query["first_name"]
        lname = col_query["last_name"]
        print(f"""
            student_id = {sid}
            first_name = {fname}
            last_name = {lname}
            """)

    print("------------------------------------------------------------")


#call ez_find to do the first print
ez_find(search_data="all")

#insert new document
insert_data={"student_id":1010,"first_name":"Albert","last_name":"Einstein"}
collection.insert_one(insert_data)

#call ez_find to print only searched for ID, make sure it's there
ez_find(search_data={"student_id":1010})

#delete student with id 1010
collection.delete_one({"student_id":1010})
#collection.delete_many({"student_id":1010}) <---Used to correct an error where I made too many 1010's in the collection

#call ez_find to search for all students. 1010 should be missing from list
ez_find(search_data="all")
