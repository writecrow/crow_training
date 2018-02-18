import nltk
from urllib import request
from bs4 import BeautifulSoup

print(("This demonstrates retrieving text from a remote URL using the `urllib` library\n").upper())
print(("In this case, we request the writecrow.org homepage.\n").upper())

url = "http://purdue.edu"
response = request.urlopen(url)
html = response.read().decode('utf8')
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup.get_text())