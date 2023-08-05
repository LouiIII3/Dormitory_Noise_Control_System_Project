# Dormitory_Noise_Control_System

<img width="40%" src="https://github.com/LouiIII3/Dormitory_Noise_Control_System/assets/119919129/ef5703b4-c228-4374-872d-f1eee4bdfdec"/>

<br>
<br>

1. Reason for Creation:
  - There are individuals in the dormitory who make noise until dawn.
  - Provide accurate criteria data regarding noise.
  - Provide information on a systematic management system to identify the source of the noise.
  - Simplify the reporting process to enhance convenience in managing noise within the dormitory.


2. Scenario:

  - When noise occurs in Room 1, the resident of Room 2 reports the complaint to the dormitory supervisor. The dormitory supervisor then verifies the noise in Room 1 and issues a warning to the occupants of that room. This information is communicated back to the resident of Room 1, who reported the noise complaint, for confirmation.


<hr>
<h2>code description</h2>

1. Client.py
- code is a Python script that uses the Tkinter library to create graphical user interface (GUI) applications.
- tkinter: The main library for creating GUI applications in Python.
- json: A module for working with JSON data.
- requests: A module for making HTTP requests.

2. temp.py
- Define the getWeather() function.
- Print the weather ID and temperature from the wethaerRes response variable.
- Store the weather ID and temperature in the weatherId and temp variables, respectively.
- Return the temp and weatherId.

3. sever.py
- This code is used to handle various types of POST requests, process data, and provide responses accordingly. The overall logic of the code is related to monitoring and   controlling rooms and alarm systems.
- Required library: The code makes use of necessary libraries such as express and body-parser, where body-parser is used to parse JSON data from the request body.
- GET Handler: The server handles incoming GET requests to the root URL ('/') and responds with "The server responds according to the GET request."


