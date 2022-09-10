import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="TRAIN",
    password="train",
    database="tolu"
)
dcursor = conn.cursor()
sql = "SELECT hospital.Doctor_Name, Hospital_id, Joining_Date, Speciality, Salary, Experience FROM hospital_2,hospital WHERE hospital_2.id = Hospital_id ORDER BY rand() LIMIT 2"
dcursor.execute(sql)
data = dcursor.fetchall()
for x in data:
    print(x)
