from urllib import request

print(("This demonstrates retrieving text from a remote URL using the `urllib` library\n").upper())
print(("In this case, we request random text from the Lorem Gutenberg site.\n").upper())

url = "https://lorem-gutenberg.markfullmer.com/demo/api/"
response = request.urlopen(url)
raw = response.read().decode('utf8')
print(raw)

# f = open('remote_file.html', 'w')
# f.write(raw)
# f.close()