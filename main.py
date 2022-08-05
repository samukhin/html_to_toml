import html_to_json
import json
import toml
from bs4 import BeautifulSoup

with open("index.html", 'r') as file:
    html_string = file.read()
soup = BeautifulSoup(html_string, 'html.parser')
for s in soup.select('script'):
    s.clear()
for s in soup.select('style'):
    s.clear()
print(soup)

output_json = json.dumps(html_to_json.convert(soup.prettify()))

with open("index.json", 'w') as file:
    file.write(output_json)

with open("index.json", 'r') as file:
    input_json = json.load(file)
output_toml = toml.dumps(input_json)

with open("index.toml", 'w') as file:
    file.write(output_toml)
