#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named 'data.json'.

    Parameters:
    - csv_filename (str): Path to the input CSV file.

    Returns:
    - bool: True if conversion is successful, False if an error occurs.
    """
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, IOError, csv.Error, json.JSONDecodeError):
        return False
