import psycopg2

DB_NAME = "hjsgjzrg"
DB_USER = "hjsgjzrg"
DB_PASS = "OmiISPdv2U7Jtq4kkmm7V6QVJbfSw7IY"
DB_HOST = "queenie.db.elephantsql.com"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    
    print("Database Connected Succesfully")

except:
    print("Database Not Connected")