# Dormitory_Noise_Control_System
<div style="text-align: center;">
  <img style="width: 40%; display: inline-block;" src="https://github.com/LouiIII3/Dormitory_Noise_Control_System/assets/119919129/ef5703b4-c228-4374-872d-f1eee4bdfdec"/>
</div>

1. Reason for Creation:
  - There are individuals in the dormitory who make noise until dawn.
  - Provide accurate criteria data regarding noise.
  - Provide information on a systematic management system to identify the source of the noise.
  - Simplify the reporting process to enhance convenience in managing noise within the dormitory.

<br>

2. Scenario:
  - When noise occurs in Room 1, the resident of Room 2 reports the complaint to the dormitory supervisor. The dormitory supervisor then verifies the noise in Room 1 and issues a warning to the occupants of that room. This information is communicated back to the resident of Room 1, who reported the noise complaint, for confirmation.



<hr>
<br>
<br>
<h2>Hardware and materials used in the project</h2>
- Sound Sensor: For noise measurement purposes (to be installed on the walls between dormitory rooms).
- Display: For reporting and notifications (to be installed in dormitory rooms and the supervisor's office).
- Buzzer: Used to notify the arrival of signals on the display.
- Push Button: Intended for reporting purposes inside the dormitory rooms and for verifying warning signals sent from the supervisor's office.
- Other Materials: Filament (for use with a 3D printer).



<hr>
<br>
<br>
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

5. Dormitory supervisor.py
- This code is an example that sends a POST request to the server with a given IP address, receives the response, and displays it in a Tkinter-based GUI application.
- The sendWarning method opens a graph window and continuously updates the sound values in real-time to display them in the form of a graph.
- In the initUI method, the code receives responses from the server and displays sound values for each room. If there is a warning, it shows an alert message using a message box.
- The code operates in a blocking manner until it receives a response.

<hr>
<br>
<br>
<h2>Added part</h2>
1. added threads.

The reason for implementing threads in this code is as follows:

Background Task Processing: The response_background function performs periodic data retrieval from the web server and processing. Such tasks are usually better handled in the background. By using threads to create separate background tasks, it prevents the user interface from freezing or becoming unresponsive, thereby enhancing the user experience.

Concurrency and Parallel Processing: Threads allow for the simultaneous execution of multiple tasks. By using threads, it enables parallel processing of tasks, such as making data requests to the web server and generating buzzer sounds, concurrently.
