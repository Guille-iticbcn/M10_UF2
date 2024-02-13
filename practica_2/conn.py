import psycopg2

#Arxiu per establir conexió amb la DB.

conn = psycopg2.connect(
    database = "postgres",
    user = "user_postgres",
    password = "pass_postgres",
    host = "localhost",
    port = "5432"
) 
connection = conn.cursor()