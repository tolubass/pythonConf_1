import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="TRAIN",
    password="train",
    database="yacht"
)
dcursor=conn.cursor()
sql="SELECT durationOfStay FROM charter WHERE startDate= %s OR startDate= %s LIMIT 2"
para=("23-04-2022","03-03-2022")
dcursor.execute(sql,para)
data=dcursor.fetchall()
for x in data:
    print(x)
