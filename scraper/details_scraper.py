import requests
from config import API_KEY

def get_details(place_id):
    url = "https://maps.googleapis.com/maps/api/place/details/json"

    params = {
        "key": API_KEY,
        "place_id": place_id,
        "fields": "name,formatted_phone_number,website"
    }

    res = requests.get(url, params=params).json()
    result = res.get("result", {})

    return {
        "name": result.get("name"),
        "phone": result.get("formatted_phone_number"),
        "website": result.get("website")
    }
