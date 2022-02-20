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

#Establish the variables and cursor objects, also insert item
cursor = db.cursor()
cursor.execute("""INSERT INTO player (first_name, last_name, team_id)
VALUES ('Smeagol', 'Shire Folk', 1)""")
cursor.execute("""SELECT player_id, first_name, last_name, team_name FROM player
INNER JOIN team ON player.team_id = team.team_id;""")
query = cursor.fetchall()

#Print Query with Joined Records, including new Record
print("\n-- Displaying Players After Insert --\n")
for x in query:
    print(f"""Player ID: {x[0]}
First Name: {x[1]}
Last Name: {x[2]}
Team Name: {x[3]}\n
-----------------------------""")

#Update the newly inserted item
cursor.execute("""UPDATE player 
SET team_id=2, first_name='Gollum',last_name='Ring Stealer'
WHERE first_name = 'Smeagol';""")

#Query again to show update
cursor.execute("""SELECT player_id, first_name, last_name, team_name FROM player
INNER JOIN team ON player.team_id = team.team_id;""")
query = cursor.fetchall()

#Print Query with Updated Record
print("\n-- Displaying Players After Update --\n")
for x in query:
    print(f"""Player ID: {x[0]}
First Name: {x[1]}
Last Name: {x[2]}
Team Name: {x[3]}\n
-----------------------------""")

#Delete the updated record
cursor.execute("""DELETE FROM player WHERE first_name='Gollum';""")

#Query again to show deletion
cursor.execute("""SELECT player_id, first_name, last_name, team_name FROM player
INNER JOIN team ON player.team_id = team.team_id;""")
query = cursor.fetchall()

#Print Query with deleted record
print("\n-- Displaying Players After Deletion --\n")
for x in query:
    print(f"""Player ID: {x[0]}
First Name: {x[1]}
Last Name: {x[2]}
Team Name: {x[3]}\n
-----------------------------""")

#Cleanup of cursor and db
cursor.close()
db.close()