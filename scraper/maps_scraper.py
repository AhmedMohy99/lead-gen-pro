import requests
from config import API_KEY, LOCATION, BUSINESS_TYPE, RADIUS

def get_coordinates():
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={LOCATION}&key={API_KEY}"
    res = requests.get(url).json()
    loc = res["results"][0]["geometry"]["location"]
    return loc["lat"], loc["lng"]

def search_places(lat, lng):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "key": API_KEY,
        "location": f"{lat},{lng}",
        "radius": RADIUS,
        "keyword": BUSINESS_TYPE
    }

    res = requests.get(url, params=params).json()
    return res.get("results", [])
