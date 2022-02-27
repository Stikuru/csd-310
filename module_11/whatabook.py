# Anthony Milton
# 02/26/2022
#Module 11/12 Whatabook

#Code queries the PySports mysql database after connecting to it, prints query

#import module
import mysql.connector
from mysql.connector import errorcode
import sys

#Config settings to connect to MYSQL
config = {
    "user":"whatabook_user",
    "password":"MySQL8IsGreat!",
    "host":"127.0.0.1",
    "database":"whatabook",
    "raise_on_warnings":True
}

#Try to connect, or print error message if it doesn't
try:
    db = mysql.connector.connect(**config)
    print(f"\n Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password doesn't exist")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

#Establish cursor object
cursor = db.cursor()

#Show Menu Function, called a bunch elsewhere
def show_menu():
    print("\n---------------Main Menu---------------")
    chooser = input("""Please choose from the following options:
    1. View Books
    2. View Store Locations
    3. My Account
    4. Exit

Your Input: """)
    if chooser=="1":
        show_books(cursor)

    elif chooser=="2":
        show_locations(cursor)
    elif chooser=="3":
        validate_user(cursor)
    elif chooser=="4":
        sys.exit(0)
    else:
        print("Invalid entry, please try again. \n-------------------------------------------")
        show_menu()

#Show Books Function, called based on main menu selection
def show_books(cursor):
    cursor.execute("""SELECT book_id, book_name, details, author FROM book""")
    print("\n---------------Book List---------------")
    books = cursor.fetchall()
    for book in books:
        print(f"""{book[0]}: {book[1]} by {book[3]} : {book[2]}""")
    print("\n---------------End of Book List-------------")
    input("Press any key to return to the main menu:")
    show_menu()

#Show Locations Function, called based on main menu selection
def show_locations(cursor):
    cursor.execute("""SELECT store_id, locale FROM store""")
    print("\n--------------Store List---------------")
    stores = cursor.fetchall()
    for store in stores:
        print(f"""{store[0]}: Store located at - {store[1]}""")
    print("\n---------------End of Store List--------------")
    input("Press any key to return to main menu:")
    show_menu()

#Validates the user based on users in the table, called from main menu selection
def validate_user(cursor):
    cursor.execute("""SELECT user_id FROM user""")
    print("\n---------------Validate User-------------")
    users =  [x[0] for x in cursor.fetchall()] #Have to create a new list from the tuple to remove the trailing "," in each item
    var = input("Please enter your user id: ")
    try:
        if int(var) in users:
            cursor.execute("""SELECT user_id, first_name, last_name FROM user WHERE user_id = %s""",([int(var)])) #Param needs to be list to work
            vuser = cursor.fetchone() #Should only have one value anyway
            print("\n------------Validation Complete------------")
            print(f"Welcome back, {vuser[1]} {vuser[2]}!")
            show_account_menu(vuser)
        else:
            print("Invalid user, please try again. \n-------------------------------------------")
            show_menu()
    except ValueError:
        print("User ID does not follow proper formatting. Closing program for security reasons.")
        sys.exit(0)

#Account menu, called after user is validated
def show_account_menu(vuser):
    my_id = vuser[0]
    print("\n---------------Account Menu---------------")
    chooser = input("""Please choose from the following options:
    1. View Your Wishlist
    2. Add A Book To Wishlist
    3. Return To Main Menu
    4. Exit

Your Input: """)
    if chooser=="1":
        show_wishlist(cursor, vuser)
    elif chooser=="2":
        show_books_to_add(cursor,vuser)
        add_book_to_wishlist(cursor,vuser,)
    elif chooser=="3":
        show_menu()
    elif chooser=="4":
        sys.exit(0)
    else:
        print("Invalid entry, please try again. \n-------------------------------------------")
        show_menu()

#View the Wishlist, called by the account menu
def show_wishlist(cursor,vuser):
    my_id = vuser[0]
    cursor.execute("""SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author FROM wishlist 
    INNER JOIN user ON wishlist.user_id = user.user_id 
    INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = %s""",([int(my_id)]))
    wishlist = cursor.fetchall()
    print(f"--------------{vuser[1]} {vuser[2]}'s Wishlist-------------")
    for book in wishlist:
        print(f"""{book[3]}: {book[4]} by {book[5]}""")
    print("\n-------------End of Wishlist------------")
    input("Press any key to return to your account menu: ")
    show_account_menu(vuser)

#Show books to add to wishlist, called when trying to add books to wishlist
def show_books_to_add(cursor,vuser):
    my_id = vuser[0]
    cursor.execute("""SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN 
    (SELECT book_id FROM wishlist WHERE user_id = %s)""",([my_id]))
    book_list = cursor.fetchall()
    print(f"--------------Available Books-------------")
    for book in book_list:
        print(f"""{book[0]}: {book[1]} by {book[2]}: {book[3]}""")
    print("-------------End of Available Books------------")

#Add books to wishlist, called from account menu
def add_book_to_wishlist(cursor,vuser):
    my_id = vuser[0]
    cursor.execute("""SELECT book_id FROM book""")
    book_list =  [x[0] for x in cursor.fetchall()] #Have to create a new list from the tuple to remove the trailing "," in each item
    var = input("\nEnter the ID of the book you would like to add: ")
    try:
        if int(var) in book_list:
            cursor.execute("""INSERT INTO wishlist(user_id, book_id) VALUES(%s, %s)""",(my_id,int(var))) #Inserts the book to wishlist
            db.commit()
            cursor.execute("""SELECT book_name, author FROM book WHERE book_id = %s""",([int(var)]))
            book_facts = cursor.fetchone()
            print(f"""{book_facts[0]} by {book_facts[1]} has been added to your wishlist!""")
            input("Press any key to return to your account: ")
            print("------------Book Added-------------")
            show_account_menu(vuser)
        else:
            print("Invalid ID, book does not exist. Please try again. \n-------------------------------------------")
            show_account_menu(vuser)
    except ValueError: #Not the fanciest way to do this, but by typing x or any other non-int, will cancel the book add thanks to the error
        print("------------Cancelled Adding Book-------------")
        show_account_menu(vuser)


#Starts showing the menu, basically begins the whole program
show_menu()

#Clean-up
cursor.close()
db.close()