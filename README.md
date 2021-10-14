# Country List Project

This project is a simple Web API server that accepts one of two HTTP Get 
requests and returns a corresponding list of country identifiers. The app
was built using the Flask framework in Python and deployed to an AWS EC2 
instance running Ubuntu 20.04 using [gevent](http://www.gevent.org/). 

The setup in AWS involves downloading and updating standard packages, creating
a Python virtual environment for our application, and installing necessary 
Python packages. All necessary Python packages can be found in the 
'requirements.txt' file. The following commands will perform these tasks, assuming
this repository has been cloned and exists as a directory named 'CountryListProject':

```
$ sudo apt update
$ sudo apt -y upgrade
$ sudo apt install -y python3-pip
$ sudo apt install -y python3-venv
$ python3 -m venv country_list
$ source country_list/bin/activate
$ cd CountryListProject
$ pip install -r requirements.txt
```

Once all the dependencies are installed, the app can be deployed using the 
following command in the terminal:

```
$ python server.py
```

The two URL endpoints are currently available at http://18.188.157.159:5000/BLZ
 and http://18.188.157.159:5000/PAN. 


