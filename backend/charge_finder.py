import requests

def get_nearest_fast_chargers(lat=36.9741, lon=-122.0308, radius_miles=15, limit=5):
    """
    Fetches the nearest EV DC Fast Chargers using the NREL API.
    Returns a list of dictionaries containing station data.
    """
    url = "https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json"
    
    params = {
        "api_key": "DEMO_KEY",  # Replace with your real API key later
        "latitude": lat,
        "longitude": lon,
        "radius": radius_miles,
        "fuel_type": "ELEC",
        "ev_charging_level": "dc_fast",
        "limit": limit
    }
    
    try:
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            return {"error": f"API Error {response.status_code}: {response.text}"}

        data = response.json()
        raw_stations = data.get('fuel_stations', [])
        
        # Format the data into a clean list to send to the frontend
        formatted_stations = []
        for station in raw_stations:
            formatted_stations.append({
                "name": station.get('station_name'),
                "network": station.get('ev_network'),
                "distance_miles": round(station.get('distance', 0), 2),
                "address": f"{station.get('street_address')}, {station.get('city')}",
                "connectors": station.get('ev_connector_types', [])
            })
            
        return formatted_stations

    except Exception as e:
        return {"error": f"Request Failed: {str(e)}"}

# If you run this file directly, it will test the function
if __name__ == "__main__":
    print("Testing backend function...")
    results = get_nearest_fast_chargers()
    print(results)