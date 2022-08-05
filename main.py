import html_to_json
import json
import toml

with open("index.html", 'r') as file:
    html_string = file.read()
output_json = json.dumps(html_to_json.convert(html_string))

#print(output_json)

with open("index.json", 'r') as file:
    input_json = json.load(file)
output_toml = toml.dumps(input_json)

print(output_toml)
