import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tutorial"
)
dcursor = conn.cursor()
sql = "SELECT tabclass.name,tabclass.phone,score.class,score.score,score.subject,attendance.attend FROM tabclass,score,attendance WHERE tabclass.id = score.user_id AND tabclass.id = attendance.user_id ORDER BY rand()"
dcursor.execute(sql)
data = dcursor.fetchall()
for x in data:
    print(x)
