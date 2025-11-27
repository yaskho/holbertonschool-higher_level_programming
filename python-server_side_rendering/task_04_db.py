from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# Define file paths
BASE_DIR = os.path.dirname(__file__)
DB_NAME = 'products.db'
DB_PATH = os.path.join(BASE_DIR, DB_NAME)
JSON_PATH = os.path.join(BASE_DIR, 'products.json')
CSV_PATH = os.path.join(BASE_DIR, 'products.csv')

# --- Helper Functions (Re-used/Modified from Task 3) ---

def read_json_data(file_path):
    """Reads and parses data from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            # Ensure the ID is integer for consistent filtering
            data = json.load(f)
            for item in data:
                if 'id' in item:
                    item['id'] = int(item['id'])
            return data
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
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    data.append(row)
                except ValueError:
                    continue
        return data
    except FileNotFoundError as e:
        print(f"Error reading CSV file: {e}")
        return []

def read_sql_data(db_path):
    """Fetches all product data from the SQLite database."""
    products_data = []
    try:
        conn = sqlite3.connect(db_path)
        # Set row factory to sqlite3.Row to access columns by name/key
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Fetch all columns
        cursor.execute("SELECT id, name, category, price FROM Products")
        
        # Convert sqlite3.Row objects to standard dictionaries
        products_data = [dict(row) for row in cursor.fetchall()]

    except sqlite3.Error as e:
        print(f"SQLite database error: {e}")
        # Return an error tuple to be handled by the main route
        return ([], f"Database error occurred: {e}")
    
    finally:
        if conn:
            conn.close()
            
    return (products_data, None)


# --- Main Route for Task 4 ---

@app.route('/products')
def products():
    # 1. Get query parameters
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    
    products_data = []
    error_message = None

    # 2. Determine data source and read data
    if source == 'json':
        products_data = read_json_data(JSON_PATH)
    elif source == 'csv':
        products_data = read_csv_data(CSV_PATH)
    elif source == 'sql':
        # New SQL path
        products_data, db_error = read_sql_data(DB_PATH)
        if db_error:
            error_message = db_error
            products_data = [] # Clear data on DB error
    else:
        # 3. Handle Invalid Source Edge Case
        error_message = "Wrong source. Please use 'json', 'csv', or 'sql'."
    
    # Check if an invalid source error has already been set
    if not error_message:
        # 4. Filter data by ID if provided (works for all sources)
        if product_id_str and products_data:
            try:
                target_id = int(product_id_str)
                filtered_data = [p for p in products_data if p.get('id') == target_id]

                if not filtered_data:
                    # 5. Handle Product Not Found Edge Case
                    error_message = f"Product with id {product_id_str} not found in the {source.upper()} data."
                
                products_data = filtered_data
                
            except ValueError:
                error_message = "Invalid product ID format. ID must be an integer."
                products_data = []
    
    # 6. Render the template
    return render_template('product_display.html', 
                           products=products_data, 
                           error=error_message,
                           source=source)

# Add home route for testing convenience
@app.route('/')
def home():
    return "Welcome! Try accessing <a href='/products?source=sql'>/products?source=sql</a>"

if __name__ == '__main__':
    # Ensure the database file exists before running the server (optional, but good practice)
    if not os.path.exists(DB_PATH):
        print(f"Warning: Database file '{DB_NAME}' not found. Please run the setup script.")
    
    app.run(debug=True, port=5000)