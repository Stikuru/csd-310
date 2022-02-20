# Anthony Milton
# 02/12/2022
#Module 8 PySports Queries

#Code queries the PySports mysql database after connecting to it, prints query

#import module
import mysql.connector
from mysql.connector import errorcode

#Config settings to connect to MYSQL
config = {
    "user":"pysports_user",
    "password":"MySQL8IsGreat!",
    "host":"127.0.0.1",
    "database":"pysports",
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

#Establish the variables and cursor objects
cursor = db.cursor()
cursor.execute("""SELECT player_id, first_name, last_name, team_name FROM player
INNER JOIN team ON player.team_id = team.team_id;""")
query = cursor.fetchall()

print(query)

#Print Query with Joined Records
print("\n-- Displaying Query Data --\n")
for x in query:
    print(f"""Player ID: {x[0]}
First Name: {x[1]}
Last Name: {x[2]}
Team Name: {x[3]}\n
-----------------------------""")

#Cleanup of cursor and db
cursor.close()
db.close()