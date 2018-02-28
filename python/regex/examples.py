import re
fh = open("test_text.txt", "r")
text = fh.read()

# Print the original text.
print(text)

# Find the tagged "Program" value.
program = re.findall('<Program: (.*\s*)>', text)
print(program)
# ['Engineering First Year']

# Find all available tags & values
tags = re.findall('<(.*\s*):(.*\s*)>', text)
print(tags)
# [('ID', ' 11127'), ('Country', ' BGD'), ('Assignment', ' 1'), ('Draft', ' A'), ('Semester in School', ' 3'), ('Gender', ' F'), ('Term writing', ' Spring 2016'), ('College', ' E'), ('Program', ' Engineering First Year'), ('TOEFL-total', ' NA'), ('TOEFL-reading', ' NA'), ('TOEFL-listening', ' NA'), ('TOEFL-speaking', ' NA'), ('TOEFL-writing', ' NA')]

# Strip out all of the tags from the text, so that you just have the text itself.
tags = re.findall('<[^>]+>', text)
for tag in tags:
    text = text.replace(tag, '')
print(text)
