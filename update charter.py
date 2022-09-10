import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="TRAIN",
    password="train",
    database="tolu"
)
dcursor=conn.cursor()
sql ="UPDATE charter3 SET name="