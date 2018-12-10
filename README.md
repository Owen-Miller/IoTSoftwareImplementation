# IoTSoftwareImplementation
Django App for Curran Place Solar Panel Data

## Getting Started

This app can be ran on a local machine or through some server like a digital dropplet.

## Prerequisites
 Python 3.5+
 Matplotlib 3.0 +
 Django 2.1+
 
 ## Installing
 If using Ubuntu 16.04 or higher the necessary python version should already be satisfied. Otherwise install python3 using the instructions found at https://www.python.org/downloads/.
 
Install the necessary packages using pip commands. Reference https://pip.pypa.io/en/stable/installing/ for install instructions.
 
 ## Testing
 To test the app using the following command python3 manage.py runserver <local host or IP address>:<portnumber> from the directory containing manage.py, should be IoTSoftwareImplementation.
 
 Additionally, in the settings.py file change the ALLOWED_HOSTS variable to contain the IP address you are attempting to deploy the app from. if the value in ALLOWED_HOSTS is '*' all host will be accepted.
 
 Keep in mind if you are testing this on a server open the port that you are trying to use. The easiest way I found to do this was to add a security wall exception on the port I wanted to access.
 
## Deployment
To deploy into a production environment I recommend using Apache and mod_wsgi documentation can be found here: https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/modwsgi/.
 
 

