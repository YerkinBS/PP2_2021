import psycopg2

DB_NAME = "tsis"
DB_USER = "postgres"
DB_PASS = "erkin426"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, port = DB_PORT)

print("Database Connected Succesfully")

cur = conn.cursor()

cur.execute("SELECT ID, NAME, EMAIL FROM Employe")

rows = cur.fetchall()

for data in rows:
    print("ID : " + str(data[0]))
    print("NAME : " + data[1])
    print("EMAIL : " + data[2])

print("Data Selected Succesfully")
conn.close()