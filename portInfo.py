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
    phoneNumber = input("phoneNumber:")
    emailAddress = input("emailAddress:")
    noOfDockingPlaces = input("noOfDockingPlaces:")
    sql = "INSERT INTO  portinfo (name,phoneNumber,emailAddress,noOfDockingPlaces) VALUES (%s,%s,%s,%s)"
    values=(name,phoneNumber,emailAddress,noOfDockingPlaces)
    dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")
dcursor.execute("SELECT * FROM portinfo")
data = dcursor.fetchall()
for x in data:
    print(x)