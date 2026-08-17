# Week 7: Weather Data ETL Pipeline

## Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using real-time weather data. Weather information was collected from the OpenWeather API for Lagos, Abuja, and London, cleaned and structured using Python and Pandas, and then saved as a CSV file for analysis.
## Data Source

The weather data was collected in real time from the OpenWeather API.

The data was collected for three cities:
- Lagos
- Abuja
- London

The fields collected include City Name, Temperature, Humidity, Weather Condition, Wind Speed, and Date and Time.
## ETL Process

### Extract
Weather data was extracted from the OpenWeather API using Python and the Requests library.

### Transform
The extracted JSON data was converted into a structured Pandas DataFrame. The required weather fields were selected, and the date and time were converted from Unix timestamps into a readable format.

### Load
The transformed data was saved as `weather_data.csv` for storage and further analysis.
## Tools Used

- Python
- Pandas
- Requests
- python-dotenv
- OpenWeather API
- Visual Studio Code
## Steps Taken

1. Connected to the OpenWeather API using an API key.
2. Extracted real-time weather data for Lagos, Abuja, and London.
3. Selected the required weather fields from the API response.
4. Converted the extracted data into a Pandas DataFrame.
5. Converted the date and time from Unix timestamps into a readable format.
6. Saved the processed data as a CSV file.
7. Compared temperatures, humidity levels, and weather conditions across the three cities.
## Key Findings

- Lagos recorded the highest temperature at 26.30°C.
- Lagos recorded the highest humidity at 80%.
- Lagos had broken clouds.
- Abuja had scattered clouds.
- London had overcast clouds.