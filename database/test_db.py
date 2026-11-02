import mysql.connector

cnx = mysql.connector.connect(option_files="db.cnf")

query = "SELECT * FROM trip LIMIT 1000"

cursor = cnx.cursor()
cursor.execute(query)

for row in cursor:
    print(row)

cursor.close()
cnx.close()

