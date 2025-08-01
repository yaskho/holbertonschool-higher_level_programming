#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to the specified file.

    Parameters:
    - data (dict): The dictionary to serialize.
    - filename (str): The name of the JSON file to write to.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from the specified file.

    Parameters:
    - filename (str): The name of the JSON file to read from.

    Returns:
    - dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as f:
        return json.load(f)
