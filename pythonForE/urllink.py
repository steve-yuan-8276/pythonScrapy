# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Function to retrieve name at specified position
def get_name_at_position(url, position):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    return tags[position - 1].contents[0], tags[position - 1].get('href', None)

# Parameters for the assignment
start_url = 'http://py4e-data.dr-chuck.net/known_by_Aileigh.html'
position = 18
repeat = 7

# Loop through the specified number of times
current_url = start_url
for _ in range(repeat):
    name, current_url = get_name_at_position(current_url, position)
    print('Current name:', name)

# Print the last name retrieved
print('Last name in sequence:', name)