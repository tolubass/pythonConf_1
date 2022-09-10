import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tolu"
)
dcursor = conn.cursor()
sql="SELECT * FROM prop WHERE classes=%s AND scores=%s ORDER BY id ASC LIMIT 1,3"
para = ('ss1','23')
dcursor.execute(sql,para)
data = dcursor.fetchall()
for x in data:
    print(x)



