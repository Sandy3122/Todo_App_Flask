# Import the create_app function from the config module
from config import create_app

# Call the create_app function to create an instance of the Flask application
app = create_app()

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
