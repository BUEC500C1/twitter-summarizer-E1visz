# WeatherAPI-E1visz
WeatherAPI-E1visz created by GitHub Classroom

#### Contents

* [Product Mission](#product-mission)
* [User Stores](#user-stories)
* [Architecture Needed](#architecture-needed)
* [Run Program](#run-program)
* [Code Flowchart](#code-flowchart)
* [Test Cases](#test-cases)
* [Lessons Learned](#lessons-learned)

<a name="product-mission"/>

## Project Mission

Provide the realtime weather of the airport, which contains the temperature, feels like, humidity, pressure, etc.

<a name="user-stories"/>

## User Stories

I, as a traveler, would like to use this API to get the weather information of the airport to make sure the journey goes well.   

I, as a ground crew, would like to use this API to get the weather imformation of the airport in case of the negative influence of the bad weather.  

<a name="architecture-needed"/>

## Architecture Needed

* Python code running on computer.    

* OpenweatherMap API.  

* Requests(python module).

<a name="run-program"/>

## Run Program

*Assumes __Requests__ packages already installed.*

*Assumes __OpenweatherMap Keys__ available.*

*Requires __Python 3.x__ to run!*

1. Copy code locally
2. Ensure the following Python packages are installed: Requests
  ```Python
  $ pip install requests
  ```
3. Add API key to local "weather.py" file and save:  
  ```Python
  API_KEY = 'Your API key'
  ```
4. Open terminal/command window and navigate to folder where code was downloaded
5. Run "python weather.py"
7. Enter the airport name

<a name="test-cases"/>

## Test Case

1. I, as a ground crew in Cass Field, I want to know whether today's weather is good for airplane to take off.
            <img src="img/result.png">         
2. I, as a traver, will fly from Colberg Airport to Keller Airfield today and I want to know the weather in these two airports is good for taking off or landing.   
            <img src="img/first.png">
            <img src="img/second.png">

<a name="lessons-learned"/>

## Lessons Learned

This project was interesting. In this project, I learned to use OpenweatherMap API to get the realtime weather conditon of the airport. Besides, I also learned to use json file in a python format.
