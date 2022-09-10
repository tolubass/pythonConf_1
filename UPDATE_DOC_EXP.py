import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="TRAIN",
    password="train",
    database="tolu"
)
dcursor = conn.cursor()
sql = "UPDATE hospital SET Experience = '2_years' WHERE Experience = 'null' "
dcursor.execute(sql)
conn.commit()
data = dcursor.fetchall()
for x in data:
    print(x)