# Imports
import html_to_json
import json
import toml
from bs4 import BeautifulSoup

# Read html
with open("index.html", 'r') as file:
    html_string = file.read()

# Prepare html, delete extra tags
soup = BeautifulSoup(html_string, 'html.parser')
for s in soup.select('script'):
    s.clear()
for s in soup.select('style'):
    s.clear()

# Convert prepared html -> json -> toml
output_toml = toml.dumps(html_to_json.convert(soup.prettify()))

# Save toml to file
with open("index.toml", 'w') as file:
    file.write(output_toml)
