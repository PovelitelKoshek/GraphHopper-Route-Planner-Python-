port urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = ""  # upload your key


def geocoding(location, key):
    while location == "":
        location = input("Enter location again: ")

    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({
        "q": location,
        "limit": "1",
        "key": key
    })

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]

        country = json_data["hits"][0].get("country", "")
        state = json_data["hits"][0].get("state", "")

        if state and country:
            new_loc = name + ", " + state + ", " + country
        elif country:
            new_loc = name + ", " + country
        else:
            new_loc = name

        print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")")
        print(url)

    else:
        lat = "null"
        lng = "null"
        new_loc = location

        if json_status != 200:
            print("Geocode API status: " + str(json_status))
            print("Error message: " + json_data.get("message", "Unknown error"))
        else:
            print("No results found for location: " + location)

    return json_status, lat, lng, new_loc


def convert_time(milliseconds):
    seconds = int(milliseconds / 1000)
    minutes = int(seconds / 60)
    hours = int(minutes / 60)

    seconds = seconds % 60
    minutes = minutes % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


while True:
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print("Vehicle profiles available on GraphHopper:")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("car, bike, foot")
    print("+++++++++++++++++++++++++++++++++++++++++++++")

    profile = ["car", "bike", "foot"]
    vehicle = input("Enter a vehicle profile from the list above: ")

    if vehicle == "quit" or vehicle == "q":
        break
    elif vehicle not in profile:
        vehicle = "car"
        print("No valid vehicle profile was entered. Using the car profile.")

    loc1 = input("Starting Location: ")
    if loc1 == "quit" or loc1 == "q":
        break

    orig = geocoding(loc1, key)

    loc2 = input("Destination: ")
    if loc2 == "quit" or loc2 == "q":
        break

    dest = geocoding(loc2, key)

    print("=================================================")

    if orig[0] == 200 and dest[0] == 200 and orig[1] != "null" and dest[1] != "null":
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])

        paths_url = (
            route_url
            + urllib.parse.urlencode({"key": key, "vehicle": vehicle})
            + op
            + dp
        )

        paths_reply = requests.get(paths_url)
        paths_status = paths_reply.status_code
        paths_data = paths_reply.json()

        print("Routing API Status: " + str(paths_status))
        print("Routing API URL:")
        print(paths_url)
        print("=================================================")

        print(
            "Directions from "
            + orig[3]
            + " to "
            + dest[3]
            + " by "
            + vehicle
        )
        print("=================================================")

        if paths_status == 200:
            distance_km = paths_data["paths"][0]["distance"] / 1000
            distance_miles = distance_km / 1.61
            time = paths_data["paths"][0]["time"]

            print("Distance Traveled: {0:.1f} miles / {1:.1f} km".format(
                distance_miles, distance_km
            ))
            print("Trip Duration: " + convert_time(time))
            print("=================================================")

            instructions = paths_data["paths"][0]["instructions"]

            for item in instructions:
                text = item["text"]
                distance = item["distance"]

                print("{0} ( {1:.1f} km / {2:.1f} miles )".format(
                    text,
                    distance / 1000,
                    distance / 1000 / 1.61
                ))

            print("=================================================")

        else:
            print("Error message: " + paths_data.get("message", "Unknown routing error"))
            print("*************************************************")
