# Open the file and read its contents
with open("output.json", "r") as file:
    data = file.read()

import ast  # Module to safely evaluate Python expressions

# Convert the string (with single quotes) into a Python list of dictionaries
data = ast.literal_eval(data)

import json  # Module to work with JSON

# Convert to JSON format with indentation
json_data = json.dumps(data, indent=4)

# Save to a new JSON file
with open("output.json", "w") as json_file:
    json_file.write(json_data)

print("Conversion complete! File saved as 'symanto_output_1.json'")