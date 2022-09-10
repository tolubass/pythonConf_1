import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="TRAIN",
    password="train",
    database="yacht"
)
dcursor=conn.cursor()
sql="SELECT users.name, yachtmmt.user_id FROM users, WHERE users.id=yachtmmt.user_id ORDER BY DESC"
para = ("23-04-2022","03-03-2022")
dcursor.execute(sql,)
data=dcursor.fetchall()
for x in data:
    print(x)