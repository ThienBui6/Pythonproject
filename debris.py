import numpy as np
import pandas as pd

# Generate synthetic debris growth dataset
years = np.arange(2000, 2031)
debris_count = np.round(5000 + np.random.normal(0, 100, len(years)) + (years - 2000) * 200)

# Simulate space weather intensity
solar_activity = np.random.uniform(0, 100, len(years))

debris_growth_data = pd.DataFrame({
    "Year": years,
    "Debris Count": debris_count,
    "Solar Activity": solar_activity
})

debris_growth_data.to_csv('data/debris_growth_data.csv', index=False)

print("✅ Debris growth dataset generated: debris_growth_data.csv")