import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tolu"
)
print("   NAME-----------NATIONALITY--------EMAIL---------PHONE----TYPE--MODEL----LOCATION--NO/D/P----COST---NO/D/P--ST/DATE---DURATION-----ARRIVAL----STAY")
dcursor = conn.cursor()
sql = "SELECT charter.name,charter.nationality,charter.email,charter.phone,charter2.type,charter2.model,charter2.home_port,charter2.number_of_berths,charter2.cost,charter3.no_of_docking_places,charter3.start_date,charter3.duration,charter3.date_of_arrival,charter3.duration_of_stay FROM charter,charter2,charter3 WHERE charter.id = charter2.user_id AND charter.id=charter3.user_id ORDER BY rand()"
dcursor.execute(sql)
data = dcursor.fetchall()
for x in data:
    print(x)
