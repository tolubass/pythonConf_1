import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "yacht"
)
dcursor=conn.cursor()
for i in range (1,5):
    name = input("name:")
    nationality = input("nationality:")
    emailAddress = input("emailAddress:")
    phoneNumber = input("phoneNumber:")
    sql = "INSERT INTO  users (name,nationality,emailAddress,phoneNumber) VALUES (%s,%s,%s,%s)"
    values=(name,nationality,emailAddress,phoneNumber)
    dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")
dcursor.execute("SELECT * FROM users")
data = dcursor.fetchall()
for x in data:
    print(x)