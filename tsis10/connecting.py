import psycopg2

DB_NAME = "tsis"
DB_USER = "postgres"
DB_PASS = "erkin426"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, port = DB_PORT)
    
    print("Database Connected Succesfully")

except:
    print("Database Not Connected")