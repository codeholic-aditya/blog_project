import sqlite3
from dependencies import DATABASE_URL

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('blog_project.db')

# Check if the connection was successful
print("Connection successful")

# Create table with "IF NOT EXISTS" to prevent errors if the table already exists
command = """
CREATE TABLE IF NOT EXISTS users_post (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    createdat TEXT,
    updatedat TEXT,
    po_id TEXT UNIQUE,
    status TEXT,
    FOREIGN KEY (user_id) REFERENCES frontend_user(id)
);
"""

# Execute the command to create the table
try:
    conn.execute(command)
    conn.commit()  # Commit the transaction
    print("Table created successfully")
except sqlite3.Error as e:
    print(f"Error occurred: {e}")
finally:
    # Close the database connection
    conn.close()




# CREATE TABLE IF NOT EXISTS frontend_user (
#     id INTEGER PRIMARY KEY,
#     username TEXT NOT NULL UNIQUE,
#     firstname TEXT,
#     lastname TEXT,
#     email TEXT NOT NULL,
#     password TEXT NOT NULL,
#     phone INTEGER,
#     address TEXT,
#     createdat TEXT,
#     updatedat TEXT,
#     fuid TEXT UNIQUE,
#     status TEXT