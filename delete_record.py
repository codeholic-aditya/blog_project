import sqlite3
from dependencies import DATABASE_URL

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('blog_project.db')

# Check if the connection was successful
print("Connection successful")

# Correct SQL DELETE command
command = """
    DELETE FROM frontend_user where username='aditya';
"""

# DROP TABLE IF EXISTS frontend_user_token;

# Execute the command to delete the record
try:
    conn.execute(command)
    conn.commit()  # Commit the transaction
    print("Record deleted successfully")
except sqlite3.Error as e:
    print(f"Error occurred: {e}")
finally:
    # Close the database connection
    conn.close()
