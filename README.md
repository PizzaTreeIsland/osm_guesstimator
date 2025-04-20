Guesstimate properties like street width in incomplete openstreetmap (osm) data. 

osm_guesstimator uses tag combinations to figure out a best guess for missing values. In the example of street width, the width=* value is used, interpreting a wide range of non-standard notations for this key. If the width value is either missing or cannot be parsed as a valid value, a combination of highway type and, if available, lane count, is used to get a best guess. 

# installation

```
pip install osm-guesstimator 
```

Requires Python 3.6 or higher. 
# usage

So far, the only function implemented is estimatewaywidth. It takes the highway as a geojson object, for example: 

```
highway = {
  "type": "way",
  "id": 1351793418,
  "nodes": [
    65295447,
    12246845964,
    65356292,
    12246845963,
    3978836027,
    5431134833
  ],
  "tags": {
    "cycleway:both": "no",
    "highway": "residential",
    "lit": "yes",
    "name": "11th Avenue",
    "parking:lane:both": "parallel",
    "parking:lane:both:parallel": "on_street",
    "sidewalk": "both",
    "surface": "asphalt",
    "tiger:cfcc": "A41",
    "tiger:county": "San Francisco, CA",
    "tiger:name_base": "11th",
    "tiger:name_type": "Ave"
  }
}
```

You can call it like this: 

```
import osm_guesstimator

estimated_width = osm_guesstimator.estimatewaywidth(highway)

print(estimated_width)

```

The estimated width is a float value in meters, rounded to two decimal places to allow for centimeter precision. 

Currently, these highway=* values are supported: 'bridleway', 'busway', 'bus_guideway', 'corridor', 'cycleway', 'escape', 'footway', 'living_street', 'motorway', 'motorway_link', 'path', 'pedestrian', 'primary', 'primary_link', 'raceway', 'residential', 'road', 'secondary', 'secondary_link', 'service', 'steps', 'tertiary', 'tertiary_link', 'track', 'trunk', 'trunk_link', 'unclassified'. 
Any other highway tag value, including missing highway tags, will result in an exception. 
# statistics
The value estimation is based on existing data on osm. The following graph shows the width distribution of highway objects with (parseable) width data, by highway type and lane count. The lane coun was differenciated into values between 1 and 8 and anything else, where anything else includes missing lane number info as well as any values other than numbers between 1 and 8. 

![Width distribution by highway type](https://github.com/user-attachments/assets/a8b2d127-6039-4647-b45a-e78542a39481)

Sorting any lane values that are not numbers between 1 and 8 as unspecified excludes both highways with lane numbers higher than 8 and highways with lane numbers in non standard notation. However, this is deemed good enough, as 99.94% of lane values are accounted for. 

For each combination of highway type and lane count, including unspecified, a median width is determined that is applied to highways that don't have a (parseable) width value themselves as a best guess. 

A third dimension to differenciate highway width in, aside from highway type and lane count, is the subtype, especially in highway=service features. The following graph shows the service road width distribution by service road type. 
However, this consideration in the width estimation is not yet implemented. 

![Service Road width distribution by type](https://github.com/user-attachments/assets/a7e1f14b-c40a-4461-9a5d-323d5547d23f)

# contribute
For feature requests or bugfixes, github issues or pull requests are always welcome. 

You can also have a look at the [proposals](#proposals) section to find projects to work on. 

Finally, you can [go out and map](https://www.openstreetmap.org)! I will regularly download the newest osm data and update the median values accordingly. Therefore, measuring and mapping the world around you or fixing typos and other non standard tagging in the data set will increase the accuracy of the estimations. 

‼️ DO NOT USE THIS TOOL TO INPUT DATA INTO OSM ‼️

The estimation functions only produces rough estimates and the resulsts are therefore not reliable. They are good enough for most cases, especially when manually measuring on a large number of objects is not feasible, but it does not warrant the level of trust people have in the data on osm. 
It would also lead to an effect where inaccuracies and biases of this method would procreate and intensify as the function would feed itself the map data created by itself. 

# proposals

Some proposals for futre extensions include: 

- Supporting ranges in data (for example, a width of "2m ~ 3m"). 
- Supporting other object types
	- Building height based on the building type and number of floors
	- Height and crown diameter of trees based on species and other factors
	- Waterway widths based on waterway type
- Take regional differences into account: Adjust the data to include rough locations, form lists of typical values for each region as an additional dimension for the estimations
- Take service road type into account
