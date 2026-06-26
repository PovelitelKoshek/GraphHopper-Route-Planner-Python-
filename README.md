# GraphHopper Route Planner (Python)

## Overview

This repository contains a small educational project developed as part of the Cisco Networking Academy DEVASC course.

The application demonstrates how to integrate a third-party REST API into a Python application. It uses the GraphHopper Geocoding API and Routing API to calculate routes between two locations and display detailed travel information.

The project focuses on practical usage of:

* REST API requests
* JSON parsing
* HTTP status code handling
* User input validation
* Error handling
* Python functions
* API authentication

---

## Features

* Geocoding of start and destination locations
* Route calculation using GraphHopper Routing API
* Vehicle profile selection:

  * car
  * bike
  * foot
* Trip distance in kilometers and miles
* Trip duration
* Step-by-step navigation instructions
* Validation of user input
* Error handling for:

  * invalid API key
  * unknown locations
  * empty input
  * API request failures
* Exit using `q` or `quit`

---

## Technologies

* Python 3
* requests
* urllib.parse
* GraphHopper REST API

---

## Project Structure

```
graphhopper-route-planner/
│
├── graphhopper.py
├── README.md
├── LICENSE
├── .gitignore
└── screenshots/
```

---

## Program Workflow

1. User selects a vehicle profile.
2. User enters the starting location.
3. The application sends a request to the GraphHopper Geocoding API.
4. Geographic coordinates are returned.
5. The destination is processed in the same way.
6. The application sends both coordinates to the Routing API.
7. The API returns:

   * total distance
   * travel time
   * navigation instructions
8. The information is displayed in the terminal.

---

## Example Output

```
Vehicle: car

Starting Location:
Washington, D.C.

Destination:
Baltimore, Maryland

Distance:
62.1 km

Travel Time:
00:51:29

Directions:
Continue onto...
Turn right...
Keep left...
...
```

---

## Possible Improvements

* Support for additional transportation profiles
* Interactive map visualization
* Export route to GPX format
* Save route history
* Graphical interface using Tkinter or PyQt
* Better exception handling
* Unit tests

---

## Educational Purpose

This project was created for learning purposes to practice working with REST APIs in Python and understand how external web services can be integrated into applications.
