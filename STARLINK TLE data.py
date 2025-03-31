import numpy as np
import pandas as pd

# Generate satellite data (using TLE format simulation)
satellite_data = {
    "Satellite": ["STARLINK"],
    "TLE_Line1": ["1 25544U 98067A   24077.49263194  .00016717  00000+0  30166-3 0  9991"],
    "TLE_Line2": ["2 25544  51.6422 150.3531 0001986  39.3055 320.8278 15.50385503453460"]
}

# Create synthetic debris data (10 debris objects)
debris_data = {
    "Debris_ID": [f"Debris_{i+1}" for i in range(10)],
    "X_Position": np.random.uniform(7000, 7100, 10),
    "Y_Position": np.random.uniform(5000, 5100, 10),
    "Z_Position": np.random.uniform(2000, 2100, 10),
    "Velocity_km_s": np.random.uniform(7.5, 8.0, 10)
}

# Save datasets to CSV files
pd.DataFrame(satellite_data).to_csv('data/satellite_tle.csv', index=False)
pd.DataFrame(debris_data).to_csv('data/debris_data.csv', index=False)

print(" Datasets generated: satellite_tle.csv and debris_data.csv")
