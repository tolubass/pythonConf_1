import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tolu"
)
dcursor = conn.cursor()
for i in range (1,8):
    Doctor_Name = input("Doctor_Name:")
    Hospital_id = input("Hospital_id:")
    Joining_Date = input("Joining_Date:")
    Speciality =input("Speciality")
    Salary = input("Salary:")
    Experience = input("Experience")
    sql = "INSERT INTO  hospital (Doctor_Name,Hospital_id,Joining_Date,Speciality,Salary,Experience) VALUES (%s,%s,%s,%s,%s,%s)"
    values=(Doctor_Name,Hospital_id,Joining_Date,Speciality,Salary, Experience)
    dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")
dcursor.execute("SELECT * FROM hospital")
data = dcursor.fetchall()
for x in data:
    print(x)

