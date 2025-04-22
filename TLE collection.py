import requests
import os
from config import TLE_URL  # Import the URL from the config file

try:
    response = requests.get(TLE_URL)
    response.raise_for_status()  # Raise an error for bad responses

    # Ensure the directory exists
    os.makedirs("data", exist_ok=True)

    # Save the TLE data to a file
    with open("data/STARLINK_tle.txt", "w") as file:
        file.write(response.text)

    print("✅ STARLINK TLE data saved!")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # e.g., 404 Not Found
except Exception as err:
    print(f"An error occurred: {err}")  # Other errors