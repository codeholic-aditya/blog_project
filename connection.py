import sqlite3
from dependencies import DATABASE_URL

con=sqlite3.connect(DATABASE_URL)

try:
    if con:
        print("Connection success")
    else:
        print("Failed to connect")
except sqlite3.Error as e:
    print(f"Error Occurred : {e}")
    
finally:
    con.close()