
# Import the necessary libraries.
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

# Create a Flask application.
app = Flask(__name__)
Bootstrap(app)

# Define the main route.
@app.route('/')
def index():
    # Return the index.html template.
    return render_template('index.html')


# Run the application.
if __name__ == '__main__':
    app.run(debug=True)
