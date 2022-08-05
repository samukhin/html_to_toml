import html_to_json
import json

with open("index.html", 'r') as file:
    html_string = file.read()
output_json = json.dumps(html_to_json.convert(html_string))

print(output_json)
