import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tolu"
)
dcursor = conn.cursor()
sql = "DELETE FROM prop ORDER BY id DESC LIMIT 4"
para = ('%080',)
dcursor.execute(sql)
conn.commit()
