import requests
import sys

# Fetch live ISS TLE data from CelesTrak
url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT="
response = requests.get(url)

# Save the TLE data to a file
with open("data/STARLINK_tle.txt", "w") as file:
    file.write(response.text)

print("✅ STARLINK TLE data saved!")
