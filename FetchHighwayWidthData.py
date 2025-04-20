import requests
import json

types = ['bridleway', 'busway', 'bus_guideway', 'corridor', 'cycleway', 'escape', 'footway', 'living_street', 'motorway', 'motorway_link', 'path', 'pedestrian', 'primary', 'primary_link', 'raceway', 'residential', 'road', 'secondary', 'secondary_link', 'service', 'steps', 'tertiary', 'tertiary_link', 'track', 'trunk', 'trunk_link', 'unclassified']

for type in types:
    querystring = f"""
    [out:json];
    way["highway"="{type}"]["width"];
    out tags;
    """

    print(f"Fetching {type} data...")
    url = "http://overpass-api.de/api/interpreter"
    response = requests.get(url, params={"data": querystring})
    if response.status_code==200:
        osm_data = response.json()
        print("Writing to file...")
        with open(f"HighwayWidthData/{type}.json", "w") as f:
            json.dump(osm_data, f, indent=2)
    else:
        print("Error:", response.status_code, response.text)