import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tolu"
)
dcursor = conn.cursor()
for i in range (1):
    name=input("name:")
    classes= input("classes:")
    scores = input("scores:")
    sql = "INSERT INTO  prop (name,classes,scores) VALUES (%s,%s,%s)"
    values=(name,classes,scores)
    dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")
dcursor.execute("SELECT * FROM prop")
data = dcursor.fetchall()
for x in data:
    print(x)




