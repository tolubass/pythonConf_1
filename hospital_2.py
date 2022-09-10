import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tolu"
)
dcursor = conn.cursor()
for i in range (1,5):
    Hospital_Name=input("Hospital_Name:")
    Bed_count= input("Bed_count:")
    sql = "INSERT INTO  hospital_2 (Hospital_Name,Bed_count) VALUES (%s,%s)"
    values=(Hospital_Name,Bed_count)
    dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")
dcursor.execute("SELECT * FROM hospital_2")
data = dcursor.fetchall()
for x in data:
    print(x)

