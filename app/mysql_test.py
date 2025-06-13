import socket
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Novell911"
)

mycursor = db.cursor()
mycursor.execute("USE mydb")