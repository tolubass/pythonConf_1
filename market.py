import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tolu"
)
dcursor = conn.cursor()
for i in range (1,3):
    name=input("name:")
    quantity= input("quantity:")
    price = input("price:")
    sql = "INSERT INTO  market (name,quantity,price) VALUES (%s,%s,%s)"
    values =(name,quantity,price)
    dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")
dcursor.execute("SELECT name FROM market")
data = dcursor.fetchall()
for x in data:
    print(x)



