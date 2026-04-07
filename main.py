from scraper.maps_scraper import get_coordinates, search_places
from scraper.details_scraper import get_details
from scraper.email_finder import extract_email
from automation.email_sender import send_email
from utils.logger import log
from utils.helpers import score_lead, create_map

import pandas as pd

def main():
    log("🚀 Start System")

    lat, lng = get_coordinates()
    places = search_places(lat, lng)

    leads = []

    for place in places:
        try:
            details = get_details(place["place_id"])

            email = None
            if details["website"]:
                email = extract_email(details["website"])

            priority = score_lead(details, email)

            lead = {
                "name": details["name"],
                "phone": details["phone"],
                "website": details["website"],
                "email": email,
                "rating": details["rating"],
                "priority": priority,
                "lat": details["lat"],
                "lng": details["lng"]
            }

            leads.append(lead)

            if email:
                send_email(email, details["name"])

        except Exception as e:
            log(f"Error: {e}")

    df = pd.DataFrame(leads)
    df.to_csv("data/leads.csv", index=False)

    create_map(lat, lng, leads)

    log("✅ Finished Successfully")

if __name__ == "__main__":
    main()
