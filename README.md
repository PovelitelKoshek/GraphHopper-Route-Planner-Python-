# GraphHopper Route Planner

## Description

This is a small educational Python project created as part of learning how to integrate REST API services into a Python application.

The application connects to the GraphHopper API, converts user-entered locations into geographic coordinates, builds a route between two locations, and displays route information in the terminal.

## Purpose of the Project

The main purpose of this project is to practice working with:

* REST API requests
* JSON responses
* HTTP status codes
* Python functions
* user input
* basic error handling
* external API services

## API Service Used

This project uses the GraphHopper API.

The application works with two GraphHopper API endpoints:

1. Geocoding API

Used to convert a location name into latitude and longitude.

Endpoint:

```text
https://graphhopper.com/api/1/geocode
```

2. Routing API

Used to build a route between two geographic points.

Endpoint:

```text
https://graphhopper.com/api/1/route
```

## Features

The application allows the user to:

* select a vehicle profile:

  * car
  * bike
  * foot
* enter a starting location
* enter a destination
* receive geographic coordinates for both locations
* build a route between the two points
* display:

  * routing API status
  * routing API URL
  * distance in kilometers and miles
  * trip duration
  * step-by-step route instructions

The program can be stopped by entering:

```text
q
```

or

```text
quit
```

## Project Structure

```text
graphhopper-route-planner/
│
├── graphhopper_route_planner.py
├── README.md
└── LICENSE
```

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/your-username/graphhopper-route-planner.git
cd graphhopper-route-planner
```

### 2. Install the required library

The project uses the `requests` library.

```bash
pip install requests
```

### 3. Add your GraphHopper API key

Open the file:

```text
graphhopper_route_planner.py
```

Find this line:

```python
key = "YOUR_GRAPHHOPPER_API_KEY"
```

Replace `YOUR_GRAPHHOPPER_API_KEY` with your own GraphHopper API key.

Example:

```python
key = "your_real_api_key_here"
```

### 4. Run the application

```bash
python graphhopper_route_planner.py
```

or, on Linux/macOS:

```bash
python3 graphhopper_route_planner.py
```

## Example

```text
Vehicle profiles available on GraphHopper:
car, bike, foot

Enter a vehicle profile from the list above: car
Starting Location: Washington, D.C.
Destination: Baltimore, Maryland

Distance Traveled: 38.6 miles / 62.1 km
Trip Duration: 00:51:29
```

## What I Learned

During this mini-project, I practiced how to:

* send GET requests to a REST API;
* work with JSON data in Python;
* parse API responses;
* process geographic coordinates;
* build a route using an external web service;
* display formatted results in the terminal;
* handle invalid user input and API errors.

## Project Status

The project is completed as an educational mini-project.
