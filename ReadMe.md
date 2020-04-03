# Camino
This is a sample project which allows users to login and enter their weights measurements over a period of time.

# Tech stack
The front end uses Angular 9 and backend uses Django 3.0. The database is being handled by sql Lite.

# Setting the environment
To setup the front end run the following command
`npm install -g @angular/cli`
Move to the root directory and then execute the following commands
`npm install`

To setup the back end run the following command. The settings of virtual env is different for windows and linux, so please install accordingly
`sudo pip3 install virtualenv`

If pip is not installed install pip using the following command
`sudo apt-get install python3-pip`

Once virtual env is setup activate it using the following commands
`source project_env/bin/activate`
where source represent the root path and the project_env represents your virtual environment

Now install the requirements.txt file present in the Camino BE file
`pip install -r requirements.txt`

Now both front and back end servers are ready to go

# Deploying
To deploy the front end, run the following command from the root directory
`ng serve`

To deploy the back end, run the following command from the root directory
`python manage.py runserver`

# Testing
Once deployed successfully functionalities of both front and back end can be tested. Postman and CRUD commands has been used by me for testing purposes for backend. Consoles has been used to test whether data is coming correctly to the front end. Some dummy data has already been added for the purpose of testing. You may drop the database and create superuser in order to access from first.

The records present in the database can be seen in `http://localhost:8000/admin/login/`

# External Libraries
Ng2-charts has been used for the purpose of charting the weight measurements.
https://valor-software.com/ng2-charts/