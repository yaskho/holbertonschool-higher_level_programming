from flask import Flask, render_template, request, jsonify
import json
import csv
import os

app = Flask(__name__)

# --- Helper Functions for Data Handling ---

def read_json_data(file_path):
    """Reads and parses data from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return []

def read_csv_data(file_path):
    """Reads and parses data from a CSV file."""
    data = []
    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id and price to appropriate types for easier filtering/display
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except ValueError:
                    # Skip rows with invalid number formats
                    continue
                data.append(row)
        return data
    except FileNotFoundError as e:
        print(f"Error reading CSV file: {e}")
        return []

# --- Main Route for Task 3 ---

@app.route('/products')
def products():
    # 1. Get query parameters
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products_data = []
    error_message = None

    # 2. Determine data source and read data
    if source == 'json':
        file_path = os.path.join(os.path.dirname(__file__), 'products.json')
        products_data = read_json_data(file_path)
    elif source == 'csv':
        file_path = os.path.join(os.path.dirname(__file__), 'products.csv')
        products_data = read_csv_data(file_path)
    else:
        # 3. Handle Invalid Source Edge Case
        error_message = "Wrong source. Please use 'json' or 'csv'."
    
    # 4. Filter data by ID if provided
    if product_id and products_data:
        try:
            target_id = int(product_id)
            # Filter the list down to products that match the ID
            filtered_data = [p for p in products_data if p.get('id') == target_id]

            if not filtered_data:
                # 5. Handle Product Not Found Edge Case
                error_message = f"Product with id {product_id} not found."
            
            products_data = filtered_data
            
        except ValueError:
            error_message = "Invalid product ID format."
            products_data = [] # Clear data if ID is invalid
    
    # 6. Render the template with data and/or error message
    return render_template('product_display.html', 
                           products=products_data, 
                           error=error_message,
                           source=source)

# Add home route for testing convenience
@app.route('/')
def home():
    return "Welcome! Try accessing <a href='/products?source=json'>/products?source=json</a>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)