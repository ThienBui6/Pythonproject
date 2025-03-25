import pandas as pd
import matplotlib.pyplot as plt

# Load debris growth data
data = pd.read_csv('data/debris_growth_data.csv')

# Plot debris growth
plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Debris Count'], label="Debris Count")
plt.plot(data['Year'], data['Solar Activity'], label="Solar Activity")
plt.xlabel('Year')
plt.ylabel('Debris Count / Solar Activity')
plt.legend()
plt.title('Space Debris Growth and Solar Activity')
plt.grid(True)
plt.show()
