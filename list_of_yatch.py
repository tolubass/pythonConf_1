import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="TRAIN",
    password="train",
    database="yacht"
)
dcursor=conn.cursor()
sql="SELECT yachtdata.name,charter.expectyedDateOfArrival,charter.durationOfStay FROM yachtdata, charter WHERE  yachtdata.id = charter.yacht_id LIMIT 2"
para = ("23-04-2022","03-03-2022")
dcursor.execute(sql,)
data=dcursor.fetchall()
for x in data:
    print(x)

