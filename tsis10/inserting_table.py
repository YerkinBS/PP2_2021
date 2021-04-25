import psycopg2

DB_NAME = "hjsgjzrg"
DB_USER = "hjsgjzrg"
DB_PASS = "OmiISPdv2U7Jtq4kkmm7V6QVJbfSw7IY"
DB_HOST = "queenie.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)

print("Database Connected Succesfully")

cur = conn.cursor()
cur.execute("""

CREATE TABLE Employe
(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
EMAIL TEXT NOT NULL
)

""")

conn.commit()
print("Table created succesfully")