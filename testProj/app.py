import os
import sys

from flask import Flask, request, jsonify, render_template
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Dummy database to store user information
# Update the username and password here
users = {
    'admin': 'password123',
    'tarique': 'admin1',
    'may': 'admin2'
}

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    print(f"Received username: {username}")
    print(f"Received password: {password}")

    if username in users and users[username] == password:
        print("Authentication successful")
        return jsonify({'message': 'Login successful'})
    else:
        print("Authentication failed")
        return jsonify({'message': 'Invalid credentials'}), 401

# Root URL - Serve HTML login page
@app.route('/')
def root():
    return render_template('index.html')

# Swagger UI
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Login API Documentation"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Shutdown mechanism
def shutdown_server():
    print("Server shutting down...")
    sys.stdout.flush()
    os._exit(0)

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    # Ask for the port number from the user
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = input("Enter the port number to run the server on: ")

    # Run the Flask application
    app.run(debug=True, port=port)
