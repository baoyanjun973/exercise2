import sqlite3

# Establish a connection with SQLite database
conn = sqlite3.connect("stephen_king_adaptations.db")
cursor = conn.cursor()

# Execute a sample query to retrieve data from the database
cursor.execute("SELECT * FROM stephen_king_adaptations_table")
results = cursor.fetchall()

# Print the retrieved data
for row in results:
    print(row)

# Close the database connection
conn.close()