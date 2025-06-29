import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (adjust host, user, and password as needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''  # Add your MySQL password if set
    )

    if connection.is_connected():
        cursor = connection.cursor()
        
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
