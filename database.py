import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("students.db")

# Create a cursor
cursor = conn.cursor()

# Create the students table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    study_hours REAL,
    attendance REAL,
    previous_score REAL,
    result TEXT
)
""")

# Save changes
conn.commit()

# Check whether the table is empty
count = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]

if count == 0:
    df = pd.read_csv("students.csv")
    df.to_sql("students", conn, if_exists="append", index=False)
    conn.commit()
    print("CSV data imported successfully!")
else:
    print("Database already contains data. Skipping CSV import.")


# Close the connection
conn.close()