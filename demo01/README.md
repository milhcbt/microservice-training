# Demo 01
## Description
This demo is a simple web application that uses Flask to display a web page with a greeting, the current time, and the name of the host(user). The application is composed of three files.
## Requirement
- Python 3, tested with Python 3.10.6 on ubuntu 22.04, please consult [this link](https://www.python.org/downloads/) for other OS.
## Run
- install virtualenv `sudo  apt install python3.10-venv` (only need once, don't need to repeat if you already have virtualenv, you may change python3.10-venv to any other version of python3-venv that match your python version)  
- create virtualenv `python -m venv .venv`
- activate virtualenv `source .venv/bin/activate`
- install requirements `pip install -r requirements.txt`
- run `python hello-world.py`
- deactivate virtualenv `deactivate`
```shell
$ python hello-world.py 
 * Serving Flask app 'hello-world'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 712-996-629
127.0.0.1 - - [17/May/2023 13:31:00] "GET /hello/ HTTP/1.1" 200 -
127.0.0.1 - - [17/May/2023 13:31:08] "GET /hello/iman HTTP/1.1" 200 -
```