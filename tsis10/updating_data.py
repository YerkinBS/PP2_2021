import psycopg2

DB_NAME = "tsis"
DB_USER = "postgres"
DB_PASS = "erkin426"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, port = DB_PORT)

print("Database Connected Succesfully")

cur = conn.cursor()

cur.execute("UPDATE Employe set EMAIL = 'e_baizhanov@kbtu.kz' WHERE ID  = 1")
conn.commit()

print('Data Updated Succesfully')
print('Total row affected ' + str(cur.rowcount))