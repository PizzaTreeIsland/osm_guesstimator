import os
import json
import re
import statistics

widths_by_type = {}
medians = {}


for type in os.listdir("HighwayWidthData")[::]:
    print(type.split('.')[0])

    with open(f"HighwayWidthdata/{type}", "r", encoding='utf-8') as f:
        data = json.load(f)
    widths = {"unspecified": [], "1": [], "2": [], "3": [], "4": [], "5":[], "6": [], "7": [], "8": []}
    for instance in data.get("elements"):
        width = instance.get("tags").get("width")
        if re.match(r"^\d+(\.\d+)?$", width): #expected format #TODO: Ignore spaces
            width = float(width)
        elif re.match(r"^\d+(,\d+)?$", width): #comma instead of decimal point #TODO: Ignore spaces
            width = float(width.replace(",", "."))
        elif re.match(r"^\d+(\.\d+)?\s*[a-zA-Z][a-zA-Z\s]*$", width):
            if re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["m", "meter", "meters", "metros", "metre", "metres", "mts", "mt", "metri", "metro", "mtr"]: #TODO: Consider taking out the ^ and $ to match in the middle of strings.
                width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1))
            elif re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["mi", "mile", "miles"]:
                width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1)) * 1609.34
            elif re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["cm", "centimeter", "centimeters", "zentimeter","cms", "centi"]:
                width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1)) * 100
            elif re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["ft", "feet", "foot"]:
                width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1)) * 0.3048
            elif re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["in", "inch", "inches"]:
                width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1)) * 0.0254
            elif re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["km", "kms", "kilometer", "kilometers"]:
                width = float(re.match(r"^(\d+(?:\.\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1)) * 1000
            else:
                width = None
        elif re.match("^\d+(,\d+)?\s*[a-zA-Z][a-zA-Z\s]*$", width):
            if re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["m", "meter", "meters", "metros", "metre", "metres", "mts", "mt", "metri", "metro", "mtr"]:
                width = float(re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", "."))
            elif re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["mi", "mile", "miles"]:
                width = float(re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", ".")) * 1609.34
            elif re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["cm", "centimeter", "centimeters", "zentimeter","cms", "centi"]:
                width = float(re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", ".")) * 100
            elif re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["ft", "feet", "foot"]:
                width = float(re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", ".")) * 0.3048
            elif re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["in", "inch", "inches"]:
                width = float(re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", ".")) * 0.0254
            elif re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z]*)(?:\s([a-zA-Z\s]+))?$", width).group(2).lower() in ["km", "kms", "kilometer", "kilometers"]:
                width = float(re.match("^(\d+(?:,\d+)?)\s*([a-zA-Z][a-zA-Z\s]*)$", width).group(1).replace(",", ".")) * 1000
            else:
                width = None
        elif re.match("^\.\d+$", width): #decimal numbers without leading 0
            width = float(width)
        elif re.match("\d+\.\d+e[-+]?\d+", width): #scinumber
            width = float(width)
        elif re.match(r"^(\d+(\.\d+)?)(?:\\)?'(\d{1,2}(\.\d+)?)?(?:\\)?(?:\")?", width): #feet and inches with ...'..." notation
            match = re.match(r"^(\d+(\.\d+)?)(?:\\)?'(\d{1,2}(\.\d+)?)?(?:\\)?(?:\")?", width)
            if match.lastindex == 2:
                width = float(match.group(1)) * 0.3048 + float(match.group(2)) * 0.0254
            else:
                width = float(match.group(1)) * 0.3048
        else: #all other
            width = None

        if width:
            if instance.get("tags").get("lanes") in ["1", "2", "3", "4", "5", "6", "7", "8"]: #covers 99.94% of lane values, can't be asked to make an effort to account for the very few remaining non standard, non NULL lane values.
                widths[instance.get("tags").get("lanes")].append(width)
            else:
                widths["unspecified"].append(width)


    widths_by_type[type.split('.')[0]] = widths

for type, lanecounts in widths_by_type.items():
    medians[type]={}
    for lanecount, values in lanecounts.items():
        if values == []:
            medians[type][lanecount] = 0
        else:
            medians[type][lanecount] = round(statistics.median(values),2)


#fallback incase no "unspecified" values are available
fallback_medians = {'bridleway': 1.95, 'busway': 5.0, 'bus_guideway': 3.8, 'corridor': 3.0, 'cycleway': 2.3,
                    'escape': 4.0, 'footway': 1.5, 'living_street': 3.0, 'motorway': 12.0, 'motorway_link': 4.0,
                    'path': 1.0, 'pedestrian': 4.0, 'primary': 7.0, 'primary_link': 7.0, 'raceway': 7.5,
                    'residential': 5.0, 'road': 3.0, 'secondary': 6.0, 'secondary_link': 9.0, 'service': 3.0,
                    'steps': 1.8, 'tertiary': 5.2, 'tertiary_link': 5.5, 'track': 2.5, 'trunk': 7.0,
                    'trunk_link': 7.0, 'unclassified': 4.0}

for type, values in medians.items():
    if values["unspecified"] == 0:
        values["unspecified"] = fallback_medians[type]

print(medians)
