# Dormitory_Noise_Control_System
<div style="text-align: center;">
  <img style="width: 40%; display: inline-block;" src="https://github.com/LouiIII3/Dormitory_Noise_Control_System/assets/119919129/ef5703b4-c228-4374-872d-f1eee4bdfdec"/>
</div>

<br>
<br>

1. Reason for Creation:
  - There are individuals in the dormitory who make noise until dawn.
  - Provide accurate criteria data regarding noise.
  - Provide information on a systematic management system to identify the source of the noise.
  - Simplify the reporting process to enhance convenience in managing noise within the dormitory.

<br>

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
- Library imports: The code makes use of necessary libraries such as express and body-parser, where body-parser is used to parse JSON data from the request body.
- GET Handler: The server handles incoming GET requests to the root URL ('/') and responds with "The server responds according to the GET request."

4. sound_measurement.py
- This code is a simple example that reads sound sensor values and sends them to a web server. Depending on how the web server utilizes this data, it opens up possibilities for more functionalities and applications.
- Library imports: The code imports the libraries it uses, including spidev, time, requests, and the json library.
- The web server address is set in the url variable.
- The data variable is defined as a dictionary containing the data to be sent to the web server.
- The headers variable is used to set the HTTP request headers.
- Initializing SPI Interface: The SPI interface is initialized to establish communication between the MCP3008 and the Raspberry Pi.
- The read_adc function reads analog values from MCP3008. It uses SPI communication to request analog-to-digital conversion from MCP3008 and returns the digital value.
- Exception Handling: The code handles the KeyboardInterrupt exception (when the user presses Ctrl+C) and closes the SPI interface.
