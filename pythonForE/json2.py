import urllib.request
import json

# Requesting a JSON file URL
url = input("Enter the URL: ")
# Load JSON file as list - info
info = json.loads(urllib.request.urlopen(url).read())

total = 0
# Loop through each item in the list comments
for item in info['comments']:
    # Loop through the value of the key count in the list and add
    total = total + int(item['count'])
print('Total number is:', total)