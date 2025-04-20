import re

def estimatewaywidth(feature):
    if feature.get("tags").get("highway") in ['bridleway', 'busway', 'bus_guideway', 'corridor', 'cycleway', 'escape', 'footway', 'living_street', 'motorway', 'motorway_link', 'path', 'pedestrian', 'primary', 'primary_link', 'raceway', 'residential', 'road', 'secondary', 'secondary_link', 'service', 'steps', 'tertiary', 'tertiary_link', 'track', 'trunk', 'trunk_link', 'unclassified']:
        median_widths = {'bridleway': {'unspecified': 1.95, '1': 1.0, '2': 6.0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}, 'busway': {'unspecified': 5.0, '1': 3.0, '2': 5.5, '3': 9.0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}, 'bus_guideway': {'unspecified': 3.8, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}, 'corridor': {'unspecified': 3.0, '1': 0, '2': 3.5, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}, 'cycleway': {'unspecified': 2.4, '1': 2.0, '2': 2.5, '3': 4.5, '4': 4.4, '5': 0, '6': 0, '7': 0, '8': 0}, 'escape': {'unspecified': 4.0, '1': 6.0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}, 'footway': {'unspecified': 1.52, '1': 1.5, '2': 2.0, '3': 3.0, '4': 3.0, '5': 0, '6': 6.5, '7': 0, '8': 8.0}, 'living_street': {'unspecified': 3.0, '1': 2.0, '2': 3.0, '3': 6.0, '4': 5.0, '5': 0, '6': 5.0, '7': 0, '8': 0}, 'motorway': {'unspecified': 12.0, '1': 6.0, '2': 7.5, '3': 11.5, '4': 15.0, '5': 19.0, '6': 21.9, '7': 22.0, '8': 35.0}, 'motorway_link': {'unspecified': 4.7, '1': 15.2, '2': 10.0, '3': 12.0, '4': 14.8, '5': 22.0, '6': 28.0, '7': 35.0, '8': 0}, 'path': {'unspecified': 1.0, '1': 2.0, '2': 3.0, '3': 0, '4': 4.0, '5': 0, '6': 0, '7': 0, '8': 10.0}, 'pedestrian': {'unspecified': 4.0, '1': 4.0, '2': 5.45, '3': 8.0, '4': 10.0, '5': 0, '6': 0, '7': 0, '8': 0}, 'primary': {'unspecified': 7.0, '1': 5.0, '2': 8.0, '3': 10.97, '4': 14.0, '5': 18.0, '6': 20.1, '7': 20.73, '8': 27.0}, 'primary_link': {'unspecified': 7.0, '1': 5.0, '2': 7.8, '3': 9.0, '4': 12.0, '5': 0, '6': 14.0, '7': 0, '8': 0}, 'raceway': {'unspecified': 7.92, '1': 8.0, '2': 6.0, '3': 20.0, '4': 20.0, '5': 5.0, '6': 0, '7': 0, '8': 400.0}, 'residential': {'unspecified': 5.0, '1': 4.0, '2': 9.1, '3': 9.5, '4': 9.0, '5': 15.2, '6': 20.0, '7': 0, '8': 0}, 'road': {'unspecified': 3.0, '1': 2.75, '2': 6.0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}, 'secondary': {'unspecified': 6.0, '1': 5.0, '2': 8.0, '3': 10.5, '4': 14.0, '5': 17.8, '6': 20.73, '7': 24.5, '8': 25.6}, 'secondary_link': {'unspecified': 9.0, '1': 5.0, '2': 8.5, '3': 9.0, '4': 8.0, '5': 4.0, '6': 12.0, '7': 0, '8': 0}, 'service': {'unspecified': 3.0, '1': 3.0, '2': 6.0, '3': 10.0, '4': 10.0, '5': 12.5, '6': 21.9, '7': 21.0, '8': 25.5}, 'steps': {'unspecified': 1.8, '1': 1.25, '2': 1.75, '3': 11.25, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}, 'tertiary': {'unspecified': 5.2, '1': 4.0, '2': 6.0, '3': 10.0, '4': 12.0, '5': 17.0, '6': 19.0, '7': 23.47, '8': 24.99}, 'tertiary_link': {'unspecified': 5.5, '1': 4.0, '2': 7.0, '3': 12.0, '4': 12.0, '5': 0, '6': 0, '7': 0, '8': 0}, 'track': {'unspecified': 2.5, '1': 3.0, '2': 4.0, '3': 5.75, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}, 'trunk': {'unspecified': 7.0, '1': 5.3, '2': 7.7, '3': 10.0, '4': 13.4, '5': 18.29, '6': 21.0, '7': 26.82, '8': 29.26}, 'trunk_link': {'unspecified': 7.0, '1': 6.0, '2': 7.9, '3': 10.0, '4': 10.0, '5': 0, '6': 0, '7': 0, '8': 0}, 'unclassified': {'unspecified': 4.0, '1': 3.5, '2': 5.0, '3': 10.0, '4': 12.2, '5': 17.84, '6': 21.95, '7': 27.5, '8': 0}}
        if feature.get("tags").get("width"):
            width = feature.get("tags").get("width")
            if re.match(r"^\d+(\.\d+)?$", width):  #expected format
                width = float(width)
            elif re.match(r"^\d+(,\d+)?$", width):  #comma instead of decimal point
                width = float(width.replace(",", "."))
            elif re.match(r"^\d+(\.\d+)?\s*[a-zA-Z][a-zA-Z\s]*$", width): #expected format with various unit specifications
                if re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["m",
                                                                                                                       "mete",
                                                                                                                       "meters",
                                                                                                                       "metros",
                                                                                                                       "metre",
                                                                                                                       "metres",
                                                                                                                       "mts",
                                                                                                                       "mt",
                                                                                                                       "metri",
                                                                                                                       "metro",
                                                                                                                       "mt"]:
                    width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1))
                elif re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["mi",
                                                                                                                         "mile",
                                                                                                                         "miles"]:
                    width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1)) * 1609.34
                elif re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["cm",
                                                                                                                         "centimete",
                                                                                                                         "centimeters",
                                                                                                                         "zentimete",
                                                                                                                         "cms",
                                                                                                                         "centi"]:
                    width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1)) * 0.01
                elif re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["ft",
                                                                                                                         "feet",
                                                                                                                         "foot"]:
                    width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1)) * 0.3048
                elif re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["in",
                                                                                                                         "inch",
                                                                                                                         "inches"]:
                    width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1)) * 0.0254
                elif re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["km",
                                                                                                                         "kms",
                                                                                                                         "kilomete",
                                                                                                                         "kilometers"]:
                    width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1)) * 1000
                else: #unit not recognizable
                    width = 0
            elif re.match(r"^\d+(,\d+)?\s*[a-zA-Z][a-zA-Z\s]*$", width): #comma instead of decimal point, with various unit specifications
                if re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["m",
                                                                                                                      "mete",
                                                                                                                      "meters",
                                                                                                                      "metros",
                                                                                                                      "metre",
                                                                                                                      "metres",
                                                                                                                      "mts",
                                                                                                                      "mt",
                                                                                                                      "metri",
                                                                                                                      "metro",
                                                                                                                      "mt"]:
                    width = float(re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", "."))
                elif re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["mi",
                                                                                                                        "mile",
                                                                                                                        "miles"]:
                    width = float(
                        re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", ".")) * 1609.34
                elif re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["cm",
                                                                                                                        "centimete",
                                                                                                                        "centimeters",
                                                                                                                        "zentimete",
                                                                                                                        "cms",
                                                                                                                        "centi"]:
                    width = float(re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", ".")) * 0.01
                elif re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["ft",
                                                                                                                        "feet",
                                                                                                                        "foot"]:
                    width = float(
                        re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", ".")) * 0.3048
                elif re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["in",
                                                                                                                        "inch",
                                                                                                                        "inches"]:
                    width = float(
                        re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", ".")) * 0.0254
                elif re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["km",
                                                                                                                        "kms",
                                                                                                                        "kilomete",
                                                                                                                        "kilometers"]:
                    width = float(re.match(r"^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", ".")) * 1000
                else: #unit not recognizable
                    width = 0
            elif re.match(r"^\.\d+$", width):  #decimal numbers without leading 0
                width = float(width)
            elif re.match(r"\d+\.\d+e[-+]?\d+", width):  #scinumber notation
                width = float(width)
            elif re.match(r"^(\d+(\.\d+)?)(?:\\)?'(\d{1,2}(\.\d+)?)?(?:\\)?(?:\")?", width):  # feet and inches with ...'..." notation
                match = re.match(r"^(\d+(\.\d+)?)(?:\\)?'(\d{1,2}(\.\d+)?)?(?:\\)?(?:\")?", width)
                if match.lastindex == 2:
                    width = float(match.group(1)) * 0.3048 + float(match.group(2)) * 0.0254
                else:
                    width = float(match.group(1)) * 0.3048
            else:  #width value not parseable
                width = 0
        else: #no width value
            width = 0

        if width == 0 and feature.get("tags").get("lanes") in map(str, range(1, 9)): #if no (valid) width value available: Determine approximate width based on highway type and lane count
            width = median_widths[feature.get("tags").get("highway")][feature.get("tags").get("lanes")]

        if width == 0: #if no (valid) lane count available: Determine width based on highway type alone
            width = median_widths[feature.get("tags").get("highway")]["unspecified"]

        return round(width, 2)

    else:
        raise Exception(f"{feature.get('tags').get('highway')} is not a valid highway type. Only supported highway types are: 'bridleway', 'busway', 'bus_guideway', 'corridor', 'cycleway', 'escape', 'footway', 'living_street', 'motorway', 'motorway_link', 'path', 'pedestrian', 'primary', 'primary_link', 'raceway', 'residential', 'road', 'secondary', 'secondary_link', 'service', 'steps', 'tertiary', 'tertiary_link', 'track', 'trunk', 'trunk_link', 'unclassified'")
