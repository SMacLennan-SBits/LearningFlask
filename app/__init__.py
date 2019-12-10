from flask import Flask

App = Flask(__name__)

from app import routes

#NOTES

# A subdirectory that includes __init__.py is considered a package, Thus it can be imported
# Importing the package executed the __init__.py and defines symbols exposed.

# The above code creates an an object as an instance of class flask
# The routes module does not exist yet
# __name__ is a predefined python variable that represents the name of the module. Typically, instatiating a flask object with __name__ will be correct configuration.

# Routes is imported at the bottom to avoid circular imports 
# Routes are different URL's that the application implements. Handler for application routes are written as functions (View Functions).
# View functions are mapped to 1 or more route urls so Flask knows how to handle requests for those URLS

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world