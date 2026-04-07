import folium

def score_lead(details, email):
    score = 0

    if not details.get("website"):
        score += 10

    if details.get("rating") and details["rating"] < 4:
        score += 5

    if not email:
        score += 3

    return "HIGH" if score >= 10 else "LOW"

def create_map(lat, lng, leads):
    m = folium.Map(location=[lat, lng], zoom_start=13)

    for lead in leads:
        color = "red" if lead["priority"] == "HIGH" else "blue"

        folium.Marker(
            [lead["lat"], lead["lng"]],
            popup=f"{lead['name']} | {lead['phone']}",
            icon=folium.Icon(color=color)
        ).add_to(m)

    m.save("data/map.html")
