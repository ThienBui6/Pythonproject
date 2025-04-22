from sgp4.api import Satrec
from datetime import datetime
from datetime import datetime, timezone
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from astropy import units as u 

# Load satellite data
try:
    sat_data = pd.read_csv('data/satellite_tle.csv')
    tle_line1, tle_line2 = sat_data['TLE_Line1'][0], sat_data['TLE_Line2'][0]
except Exception as e:
    print(f"Error loading satellite data: {e}")
    exit()

# Parse the TLE and get satellite position
satellite = Satrec.twoline2rv(tle_line1, tle_line2)

# Convert current UTC time to Julian Date
now = datetime.now(timezone.utc)
jd = (now - datetime(2000, 1, 1, 12, tzinfo=timezone.utc)).days + 2451545
fr = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds() / 86400.0

e, position, velocity = satellite.sgp4(jd, fr)

# Convert position and velocity to NumPy arrays
position = np.array(position)
velocity = np.array(velocity)
# Convert to astropy Quantity
position = position * u.m  # Add units of meters
velocity = velocity * u.m / u.s  # Add units of meters per second

# Plot the satellite orbit
orbit = Orbit.from_vectors(Earth, position * 1e3, velocity * 1e3)
plt.figure(figsize=(10, 6))
#orbit.plot(label="Satellite Orbit")                                    # still having bug in here with plot
plt.title("Satellite Orbit Tracker")
plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.legend()
plt.grid()
plt.show()

# Monte Carlo collision simulation
try:
    debris = pd.read_csv('data/debris_data.csv')
except Exception as e:
    print(f"Error loading debris data: {e}")
    exit()

collision_count = 0

for i in range(1000):
    # Simulate debris positions with some noise
    debris_sim = debris[['X_Position', 'Y_Position', 'Z_Position']].values + np.random.normal(0, 0.1, size=(debris.shape[0], 3))
    distances = np.linalg.norm(position - debris_sim, axis=1)
    collision_count += np.sum(distances < 1)  # Assuming 1 meter as the collision threshold

collision_prob = (collision_count / 1000) * 100
print(f"Collision Probability: {collision_prob:.2f}%")