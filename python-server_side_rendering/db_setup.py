import sqlite3
import os

DB_NAME = 'products.db'

def create_database():
    """Creates the products.db file and populates the Products table."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # 1. Create the table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        
        # 2. Insert example data (using OR IGNORE to prevent duplicate inserts)
        data = [
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ]
        
        cursor.executemany('''
            INSERT OR REPLACE INTO Products (id, name, category, price)
            VALUES (?, ?, ?, ?)
        ''', data)
        
        conn.commit()
        print(f"Database '{DB_NAME}' created and populated successfully.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # You would typically run this file once: python db_setup.py
    create_database()