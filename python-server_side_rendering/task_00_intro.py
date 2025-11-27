import os
import logging
from typing import List, Dict, Any

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template: str, attendees: List[Dict[str, Any]]):
    """
    Generates personalized invitation files from a template and a list of attendees.
    Handles various edge cases and errors gracefully.

    Args:
        template (str): The string template with placeholders.
        attendees (List[Dict[str, Any]]): A list of dictionaries, where each dict
                                          contains data for an attendee.
    """
    # 1. Check Input Types
    if not isinstance(template, str):
        logging.error("Invalid input type: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input type: Attendees must be a list of dictionaries.")
        return

    # 2. Handle Empty Template
    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    # 3. Handle Empty List of Objects
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # Define the required placeholders
    placeholders = ["{name}", "{event_title}", "{event_date}", "{event_location}"]
    
    # 4. Process Each Attendee and Generate Output Files
    for index, attendee in enumerate(attendees):
        output_filename = f"output_{index + 1}.txt"
        
        # Start with a fresh copy of the template
        personalized_invitation = template
        
        # Substitute placeholders
        for placeholder in placeholders:
            key = placeholder.strip("{}")  # e.g., converts "{name}" to "name"
            
            # Check for missing data (including None values)
            # Use 'N/A' if the key is missing or the value is None
            value = attendee.get(key)
            if value is None or (isinstance(value, str) and not value.strip()):
                replacement = "N/A"
            else:
                replacement = str(value)
            
            # Replace the placeholder in the invitation
            personalized_invitation = personalized_invitation.replace(placeholder, replacement)
        
        # Write the personalized invitation to the output file
        try:
            with open(output_filename, 'w') as f:
                f.write(personalized_invitation)
            logging.info(f"Successfully generated file: {output_filename}")
        except IOError as e:
            logging.error(f"Error writing to file {output_filename}: {e}")

if __name__ == '__main__':
    # This block is for demonstrating the main file logic
    
    # Example template (Ideally read from template.txt)
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Error: template.txt not found. Create it with the provided content.")
        template_content = "" # Use empty string for error testing

    # Example Data for Testing:
    test_attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        # Charlie has 'event_date' set to None (Missing Data Case)
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"},
        # Missing 'event_title' (Missing Data Case)
        {"name": "Dana", "event_date": "2024-01-01", "event_location": "Online", "name": "Dana"}
    ]

    print("\n--- Running valid case ---")
    generate_invitations(template_content, test_attendees)
    
    print("\n--- Running Empty Template case ---")
    generate_invitations("", test_attendees)
    
    print("\n--- Running Empty List case ---")
    generate_invitations(template_content, [])
    
    print("\n--- Running Invalid Template Type case (Expected Error) ---")
    generate_invitations(12345, test_attendees)
    
    print("\n--- Running Invalid Attendees Type case (Expected Error) ---")
    generate_invitations(template_content, "not a list")
    