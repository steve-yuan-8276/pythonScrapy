import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Input the URL
url = input('Enter url: ')
print('Retrieving', url)

# Open the URL and read the data from it
uh = urllib.request.urlopen(url)
data = uh.read()
# Print the length of the data retrieved from the URL
print('Retrieved', len(data), 'characters')

# Parse the XML data using ElementTree library and find all the comment elements
tree = ET.fromstring(data)
items = tree.findall('comments/comment')

# Iterate through each comment element, find the count element and add the count value to the total
total = 0
count = 0
for item in items:
    count = count + 1
    t = item.find('count').text
    total = total + float(t)

# Print the total count and sum of all the count elements in the XML data
print('Count:', count)
print('Sum:', total)