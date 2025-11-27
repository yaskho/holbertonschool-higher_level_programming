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
    app.run(debug=True, port=5000)
