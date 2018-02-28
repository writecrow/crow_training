#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This demonstrates retrieving text from a remote URL using the `urllib` library
In this case, we request the writecrow.org homepage.
'''

from urllib import request
from bs4 import BeautifulSoup

url = "http://purdue.edu"
response = request.urlopen(url)
html = response.read().decode('utf8')
print(html)
soup = BeautifulSoup(html, 'html.parser')
print(soup.get_text())
