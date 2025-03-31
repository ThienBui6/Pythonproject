import sqlite3
import pandas as pd
import numpy as np

# Connect to SQLite database
conn = sqlite3.connect('satellite_tracker.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS satellite_data (
        satellite_name TEXT,
        tle_line1 TEXT,
        tle_line2 TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS debris_data (
        debris_id TEXT,
        x_position REAL,
        y_position REAL,
        z_position REAL,
        velocity_km_s REAL
    )
''')

# Insert satellite TLE data
satellite_data = [
    ("ISS", "1 25544U 98067A   24077.49263194  .00016717  00000+0  30166-3 0  9991",
     "2 25544  51.6422 150.3531 0001986  39.3055 320.8278 15.50385503453460")
]
cursor.executemany("INSERT INTO satellite_data VALUES (?, ?, ?)", satellite_data)

# Generate debris data
debris_data = [
    (f"Debris_{i+1}", np.random.uniform(7000, 7100),
     np.random.uniform(5000, 5100),
     np.random.uniform(2000, 2100),
     np.random.uniform(7.5, 8.0))
    for i in range(10)
]
cursor.executemany("INSERT INTO debris_data VALUES (?, ?, ?, ?, ?)", debris_data)

# Commit changes
conn.commit()
conn.close()

print("Satellite and debris data loaded into satellite_tracker.db")
