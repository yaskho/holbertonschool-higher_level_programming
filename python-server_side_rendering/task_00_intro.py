import os


def generate_invitations(template, attendees):
# Input type checks
if not isinstance(template, str):
print(f"Error: template must be a string, got {type(template).**name**}")
return
if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
print(f"Error: attendees must be a list of dictionaries, got {type(attendees).**name**}")
return

```
# Empty template check
if template.strip() == "":
    print("Template is empty, no output files generated.")
    return

# Empty attendees list check
if len(attendees) == 0:
    print("No data provided, no output files generated.")
    return

# Process each attendee
for index, attendee in enumerate(attendees, start=1):
    # Replace placeholders with actual values or "N/A"
    output_content = template
    for placeholder in ["name", "event_title", "event_date", "event_location"]:
        value = attendee.get(placeholder)
        if value is None:
            value = "N/A"
        output_content = output_content.replace(f"{{{placeholder}}}", str(value))

    # Write to output file
    filename = f"output_{index}.txt"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(output_content)
    except Exception as e:
        print(f"Error writing file {filename}: {e}")
```
