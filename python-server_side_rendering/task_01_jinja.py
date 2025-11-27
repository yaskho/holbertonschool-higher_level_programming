This task guides you through setting up a basic Flask application and using Jinja's templating features—specifically the {% include %} statement—to create a modular and reusable website structure.

Here is the structured solution for your files:

1. Project Setup
First, ensure you have the required environment:

Bash

pip install Flask
Create the following file and folder structure:

your-project-directory/
├── task_01_jinja.py
└── templates/
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── header.html
    └── footer.html
2. Python Application (task_01_jinja.py)
This file sets up the Flask application and defines the routes to render your templates.

Python

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page using index.html."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about page using about.html."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Renders the contact page using contact.html."""
    return render_template('contact.html')

if __name__ == '__main__':
    # Run the application on debug mode and port 5000 as required
    print("Running Flask app on http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)
