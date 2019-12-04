# Neighboring Water Systems data

## Summary

This is data used to calculate each public water system's nearest weather station.

## Collection Date

??

## Source

This data was collected from running the first few cells in a file called `code/python/notebooks/Neighboring_Water_Systems.ipynb`, which scrapes the EPA's EnviroFacts API.

## Description

#### water_systems.csv

List of all public water systems in the EPA data.

- **PWSID**: The Public Water System Identification (UID).
- **LAT** and **LON**: Latitude and longitude coordinates of the public water system.

#### water_systems_and_nearest_weather_stations.csv

Each water system's mapping to the nearest weather station; this is a one-to-many merge, where each row corresponds to a public water system.

- **PWSID**: The Public Water System Identification (UID).
- **LAT** and **LON**: Latitude and longitude coordinates of the public water system.
- **weather_station**: Name of the weather station
- **LAT_weather** and **LON_weather**: Latitude and longitude coordinates of the weather station.
- **distance**: Distance in miles between the public water system and the weather station.

#### weather_stations.csv

- **Station**: Name of the weather station, which can be used as a UID.
- **Lat** and **Lon**: Latitude and longitude coordinates of the weather station.

#### zipcodes.csv

Each zip code in the U.S.

- **zip_code**: Zip code (UID).
- **latitude** and **longitude**: Latitude and longitude coordinates of the center of the zip code's geograph.
- **city**, **state**, and **county**: City, state, and county corresponding with the zip code.

## Use

When you want to include rainfall as a feature for a model that can be linked to each public water system, the `water_systems_and_nearest_weather_stations.csv` provides a convenient way to link the water system to a weather station, which then allows for rainfall data to be incorporated.

