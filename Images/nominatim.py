import requests

def gps_coordinate(city):
    """
    Retrieve the latitude and longitude coordinates for a given city using the LocationIQ geocoding API.

    Args:
        city (str): Name of the city.

    Returns:
        dict or None: Dictionary containing 'latitude' and 'longitude' keys with float values,
                      or None if coordinates are not found or if there's an error.
    """
    #static
    if city.lower() == 'queensland':
        return {'latitude': -16.92, 'longitude': 145.777}
    
    base_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an HTTPError for bad status codes (e.g., 404, 500)
        data = response.json()

        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return {'latitude': latitude, 'longitude': longitude}
        else:
            print(f"No coordinates found for {city}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching coordinates for {city}: {e}")
        return None

# Test the gps_coordinate function
if __name__ == "__main__":
    # Test with different cities
    cities = ["Cairns", "Brisbane", "Sydney","Queensland"]

    for city in cities:
        coordinates = gps_coordinate(city)
        if coordinates:
            print(f"Coordinates for {city}: {coordinates}")
        else:
            print(f"No coordinates found for {city}")
