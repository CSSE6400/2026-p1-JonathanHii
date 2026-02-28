from flask import Flask 

"""
Commands:
    - `poetry run` to run commands
    - `flask --app todo run`  
        - Flask automatically looks inside __init__.py and start the server
        - `-p 6400` to run it on port 6400

    - `curl -X GET http://localhost:6400/api/v1/health` to test apis 
"""

def create_app():
    app = Flask(__name__)
    
    from .views.routes import api
    app.register_blueprint(api)

    return app 


