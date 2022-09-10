import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="TRAIN",
    password="train",
    database="yacht"
)
dcursor=conn.cursor()
sql="SELECT * FROM charter durationOfStay WHERE expectyedDateOfArrival = %  "
para = ("27-02-2022",)
dcursor.execute(sql,)
data=dcursor.fetchall()
for Y in data:
    print(Y)