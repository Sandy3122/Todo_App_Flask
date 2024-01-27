# Import necessary modules and classes
from app import app
from flask import render_template

# Define a route for the home page
@app.route('/')
def index():
    # Render the 'index.html' template
    return render_template('index.html')

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
