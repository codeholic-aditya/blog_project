import sqlite3
from dependencies import DATABASE_URL

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('blog_project.db')

# Check if the connection was successful
print("Connection successful")

# Create table with "IF NOT EXISTS" to prevent errors if the table already exists
command = """
CREATE TABLE IF NOT EXISTS frontend_user_token (
    id INTEGER PRIMARY KEY,
    userid INTEGER NOT NULL UNIQUE,
    token TEXT,
    createdat TEXT,
    updatedat TEXT,
    FOREIGN KEY (userid) REFERENCES frontend_user(id) ON DELETE CASCADE
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
