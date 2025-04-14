
import json
import re

def fix_malformed_json(raw_text):
    # Replace single quotes with double quotes
    fixed_text = raw_text.replace("'", '"')

    # Replace Python-style None, True, False with JSON null, true, false
    fixed_text = fixed_text.replace("None", "null").replace("True", "true").replace("False", "false")

    try:
        # Attempt to parse the corrected string to ensure it's valid JSON
        data = json.loads(fixed_text)
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
        return None

    # Return the pretty-formatted JSON string
    return json.dumps(data, indent=2)

if __name__ == "__main__":
    # Updated to use the correct filename "output.json"
    with open("/Users/tobiasnikolaisen/Documents/Github/HEL8048/bigfive_patterns/data/output.json", "r") as infile:
        raw_data = infile.read()

    corrected_json = fix_malformed_json(raw_data)

    if corrected_json:
        with open("corrected_output.json", "w") as outfile:
            outfile.write(corrected_json)
        print("Corrected JSON saved to corrected_output.json")
    else:
        print("Failed to correct the JSON.")
