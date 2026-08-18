import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="mentorai",
    user="postgres",
    password="123456"
)

cursor = connection.cursor()