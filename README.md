# VehicleCollisionDataVisualization

## About the Project:
This personal project includes a DataVisualization.html file which acts as the frontend in visualizing over 4000 unique vehicle collision records as toggleable colour coded markers using the Google Maps API that occurred in Toronto during March of 2024 which can be found [here](https://data.torontopolice.on.ca/datasets/bc4c72a793014a55a674984ef175a6f3_0/explore?location=22.500085%2C-67.638909%2C3.15)
Each collision marker when clicked displays information about that collision including date, Neighbourhood, number of fatalities, and presence of injuries. I also included a toggleable heat map so the user can conveniently tell apart which regions of Toronto have more or less collisions that other regions making it a useful tool in narrowing down regions that outline potential road safety concerns.

The App.py server performs the tasks associated with a REST API through the Flask library to serve collision data as a JSON structure which is called by the frontend. To do so the server first references the "DataRetrieval.py" module that processes the initial dataset contained in the "TorontoTrafficCollisions.csv.zip" file using the pandas library to narrow down the proper month and year that gets called by the Flask application.

## How to Run It:
To run this web application the user must first boot up the App.py server which will run locally allowing for the HTTP GET requests outgoing from the frontend to be served after the user locally boots up the html application.

#### Note: 
To ensure the API key's usage remains secure the html web app must be launched in correspondence to an http url under the form of "*/DataVisualization.html" where * is a wildcard character. Also, to best reduce the incurring costs associated with map load operations having to do with the api key the allowable total number of map loads per day/per minute/per user per minute has been set to a very small allowable number.