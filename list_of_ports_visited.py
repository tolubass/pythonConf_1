import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="TRAIN",
    password="train",
    database="yacht"
)
dcursor=conn.cursor()
sql="SELECT portinfo.name,yachtdata.homePort,charter.expectyedDateOfArrival,charter.durationOfStay " \
    "FROM portinfo,yachtdata,charter WHERE portinfo.id = charter.portid AND portinfo.id = yachtdata.id ORDER BY yachtdata.id"
para = ("23-04-2022","03-03-2022")
dcursor.execute(sql,)
data=dcursor.fetchall()
for x in data:
    print(x)