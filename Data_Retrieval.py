import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('satellite_tracker.db')

# Query satellite data
satellite_query = "SELECT * FROM satellite_data"
satellite_df = pd.read_sql(satellite_query, conn)
print(satellite_df)

# Query debris data
debris_query = "SELECT * FROM debris_data"
debris_df = pd.read_sql(debris_query, conn)
print(debris_df)

conn.close()
