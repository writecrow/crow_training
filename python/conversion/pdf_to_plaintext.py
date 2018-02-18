from urllib import request
import PyPDF2
from urllib.request import urlretrieve

print(("This demonstrates extracting the text from a PDF using the PyPDF2 library").upper())
print(("We'll save the original file to poster.pdf and a plaintext version to poster_plain.txt").upper())

url = "http://writecrow.org/wp-content/uploads/2017/03/final-aaal2017-poster.pdf"
filename = 'poster'
urlretrieve(url, filename + '.pdf')

# creating a pdf file object
pdfFileObj = open(filename + '.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
print(pdfReader.numPages)
 
# creating a page object
pageObj = pdfReader.getPage(0)
 
# extracting text from page
# print(pageObj.extractText())
 
f = open(filename + '_plain.txt', 'w')
f.write(pageObj.extractText())
f.close()

# closing the pdf file object
pdfFileObj.close()