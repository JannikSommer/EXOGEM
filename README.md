# EXOGEM
 This repository contains the code for the EXOGEM project which was the Bachelor's thesis for Software Engineering students at Aalborg University. The project was in late 2022 published at [The International Conference on Service Oriented computing (ICSOC 2022)](https://icsoc2022.spilab.es) in a revised format with the code being rewritten to JavaScript and with other use cases than originally presented. The paper can be found [here](https://link.springer.com/chapter/10.1007/978-3-031-26507-5_10) but is not free. 


## Purpose 
The idea behind the project was to introduce a new way to include monitoring of APIs created with the OpenAPI Generator. In short, server metrics would be broadcast back to the client in the response to a server request, and the client would then send the server metrics to the monitoring server. This would then enable the server to be monitored without a large overhead of sending requests to the monitoring server itself. 

## Overview 
The project is made up of several important components which are explained as follows. Overall the project was created with the purpose of facial recognition on the server based on image data sent from the client side when it locates a face from a webcam. The server will then recognize individuals from the image data. The idea is that one or more clients with lesser hardware are connected to the server which has the necessary hardware to run the ML model and recognize individuals. 

### Framework 
This includes the necessary template files which the OpenAPI Generator will use to create the EXOGEM framework.

### Client 
The client will take some input data from the webcam and send image data to the server for processing face recognition. 

### Server 
The server is a Python Flask server which serves the client requests for image processing. It also has a machine learning model which is trained to recognize individual based on facial attributes. It will also collect server metrics that is used to monitor it. 

### Monitoring server
The monitoring server also a Python Flask server that will receive requests from the client after it gets a response from the server. It contains a SQLite database which contains the metric data which is accessible from a homepage. 