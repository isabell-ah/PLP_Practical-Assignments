import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

try:


 conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password
 )
 cursor = conn.cursor()
#question1- creating db
 cursor.execute("CREATE DATABASE salesDB;")
 print("Database 'salesDB' created successfully.")

#question2 - dropping db
 cursor.execute("DROP DATABASE IF EXISTS demo;")
 print("Database 'demo' dropped successfully.")

 cursor.close()
 conn.close()

except mysql.connector.Error as err:
    print(f" MySQL Error: {err}")
