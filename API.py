import requests
import sys
import json
if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
# TO run it use the command line like this:
# python API.py "band name"
print(json.dumps(response.json(), indent=2)) 
# Here json.dumps is used to convert the json object into a string (formatted) 
#with indentation of 2 spaces for better readability result is down example taken is "the beatles"

# here we will do another thing 
import requests
import sys
import json
if len(sys.argv) <= 1:
    sys.exit()
term = " ".join(sys.argv[1:])# For multi word band names
response = requests.get("https://itunes.apple.com/search?entity=song&limit=89&country=in&term=" + term)
o=response.json()
for song in o["results"]:#Here we are accessing the results key in the json object
    print(song["trackName"])