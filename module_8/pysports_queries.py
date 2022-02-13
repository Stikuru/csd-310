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
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()

#Print Team Records
print("\n-- Displaying Team Records --\n")
for team in teams:
    print(f"""Team ID: {team[0]}
Team Name: {team[1]}
Team Mascot: {team[2]}""")

#Print Player Records
print("\n-- Displaying Player Records --\n")
for player in players:
    print(f"""Player ID: {player[0]}
First Name: {player[1]}
Last Name: {player[2]}
Team ID: {player[3]}\n""")

#Cleanup of cursor and db
cursor.close()
db.close()