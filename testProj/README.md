# Save the Code:

Save the provided code in a Python file, for example, `app.py`.

# Install Dependencies:

Ensure that you have Flask and Flask-Swagger-UI installed. You can install them using pip:

pip install Flask flask-swagger-ui


# Run the Flask Application:

1. Open a terminal or command prompt.
2. Navigate to the directory containing your `app.py` file.
3. Run the Flask application by executing the `app.py` file with Python 3 and providing the desired port number as a command-line argument. Use the following command:

python3 app.py <port_number>


Replace `<port_number>` with the port number you want the server to listen on.

# Access the Application:

1. Open a web browser.
2. Navigate to `http://localhost:<port_number>` to access the frontend login page served by the Flask application.
3. Replace `<port_number>` with the port number you specified when running the Flask application.
4. Use the following credentials to test positive login responses:
   - Username: admin
   - Password: password123

# Access Swagger UI:

To access Swagger UI for API documentation, navigate to `http://localhost:<port_number>/api/docs` in your web browser.
Replace `<port_number>` with the port number you specified when running the Flask application.
You should see the Swagger UI interface displaying the API documentation.

# Shutdown the Server:

To gracefully shutdown the server, you can access `http://localhost:<port_number>/shutdown` in your web browser. This will trigger the shutdown mechanism and print "Server shutting down..." in the terminal where Flask is running.
Again, replace `<port_number>` with the port number you specified when running the Flask application.
