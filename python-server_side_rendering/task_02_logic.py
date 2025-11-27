from flask import Flask, render_template
import json
import os

# Initialize the Flask application
app = Flask(__name__)

# --- Re-use routes from previous task (optional, but good practice) ---

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html')

# --- New Route for Task 2 ---

@app.route('/items')
def items():
    """Reads items from items.json and renders them using a dynamic template."""
    items_list = []
    
    # Path to the JSON file
    json_file_path = os.path.join(os.path.dirname(__file__), 'items.json')

    try:
        # 1. Read and parse JSON data
        with open(json_file_path, 'r') as f:
            data = json.load(f)
            # Safely get the list, defaulting to an empty list if 'items' key is missing
            items_list = data.get('items', [])
            
    except FileNotFoundError:
        print(f"Error: {json_file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {json_file_path}.")

    # 2. Pass the dynamic list to the template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    # Run the application on debug mode and port 5000
    app.run(debug=True, port=5000)