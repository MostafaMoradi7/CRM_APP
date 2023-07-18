import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'iammostafa'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE mostafa_db")

print("DONE")