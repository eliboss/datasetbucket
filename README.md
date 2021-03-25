# datasetbucket

## Python and Flask installation via VSCode

### Prior to install our project in your local environment, follow these steps to make sure all the requirements are in place and working

1. Install python in your machine

    https://www.python.org

    If on a Mac, you can use home-brew with 

    `brew install python3`

    This command will install python3 and pip3

2. Open a new VSCode workspace (as you usually do) and install the Python extension

    https://marketplace.visualstudio.com/items?itemName=ms-python.python

3. Test a “Hello Python” print statement to see if python is working

    create file: hello.py

    and enter this:

    `msg = “Hello World!`

    `print(msg)`

    Check the terminal for the print.

4. Create a virtual environment

    On the terminal:

    `Python3 -m venv venv`

    The folders will be automatically set up on your workspace

5. Accept vscode tip to use this folder as your workspace

6. Before installing Linter pylint

    On the terminal:

    ` source venv/bin/activate `

    And the accept or install pylint

7. Install Flask

    On the terminal:

    ` pip3 install flask `

8. Test a "Hello Flask" to see if Flask is working

    https://flask.palletsprojects.com/en/1.1.x/quickstart/

    create file: app.py

    enter this:

    `from flask import Flask`

    `app = Flask(__name__)`


    `@app.route(‘/‘)`

    `def hello_world():`

    `    return 'Hello, World!’`

    Check the Hello Flask by going to Play Debug menu on VSCode

    Click on Run and Debug

    and choose to run as Flask

    watch the command line for the local web server address to appear

    Click on it, and a new window will open with your Hello Flask

    NOTE: Delete this app.py before downloading the project folder with a new app.py containing the project routes.

9. Freeze your dependencies

    after you get the dependencies installed, make sure you freeze them for version control 
    on the terminal:

    `pip3 freeze > requirements.txt`

    a txt file will be created automatically with a list of dependencies
    keep updating this requirements every time before you git command push, with the same line of command above, the file updates itself with that
## Local Deployement via VSCode
### Download the project folders to your local environment and before you commit your changes to Github for the first time, follow these steps:

1. If you can't locate these folders in your workspace, make sure you create an env.py and .gitignore files to keep your sensitive data secret

    On the terminal

    `touch env.py`

    `touch .gitignore`

    Open the .gitignore and insert:

    `env.py`

    `__pycache__`

    Save and close .gitignore

2. Open env.py and enter the following:

    `import os`

    `os.environ.setdefault("IP", "0.0.0.0")`

    `os.environ.setdefault("PORT", "5000")`

    `os.environ.setdefault("SECRET_KEY", "secret_key_here")`

    `os.environ.setdefault("MONGO_URI", "value_from mongoDB_here")`

    `os.environ.setdefault("MONGO_DBNAME", "your_database_collection_name_here")`

    This information will help create the integration between mongoBD and python-flask and redirect debug to your main terminal via the command `python3 app.py` (this will give you a port at 5000 to open a new window and run the app on your browser).

## Heroku Deployment

1. Create a Procfile

2. Update your requirements.txt

3. Open your Heroku Dashboard and create a new app

4. Enter the Config Vars

5. Connect your github Repo

## Connect MongoDB with Flask via flask-pymongo

### Flask-PyMongo is a 3rd-party library that helps connect the MongoDB database and the datasetbucket application by using a database url

1. On the terminal:

    `pip3 install flask-pymongo`

    `pip3 install dnspython`

    `pipe freeze > requirements.txt`
