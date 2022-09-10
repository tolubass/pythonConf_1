import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tolu"
)
dcursor=conn.cursor()
for i in range (1,2):
    name = input("name:")
    nationality = input("nationality:")
    email = input("email:")
    phone = input("phone:")
    sql = "INSERT INTO  charter (name,nationality,email,phone) VALUES (%s,%s,%s,%s)"
    values=(name,nationality,email,phone)
    dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")
dcursor.execute("SELECT * FROM charter")
data = dcursor.fetchall()
for x in data:
    print(x)