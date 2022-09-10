import mysql.connector
conn= mysql.connector.Connect(
    host="localhost",
    username="TRAIN",
    password="train",
    database="tolu"

)
dcursor=conn.cursor()
sql="SELECT charter.name,home_port,start_date,date_of_arrival,duration_of_stay FROM charter,charter2,charter3 WHERE charter.id = charter2.user_id AND charter.id=charter3.user_id ORDER by rand()"
dcursor.execute(sql)
data=dcursor.fetchall()
for x in data:
    print(x)
