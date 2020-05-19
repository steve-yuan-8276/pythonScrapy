import urllib.request
request_url = "http://helloworldbook2.com/data/message.txt"
with urllib.request.urlopen(request_url) as response:
    content_of_the_html = response.read()

print(content_of_the_html)
