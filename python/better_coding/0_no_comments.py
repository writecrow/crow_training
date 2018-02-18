from urllib import request
import PyPDF2
from urllib.request import urlretrieve
url = "http://writecrow.org/wp-content/uploads/2017/03/final-aaal2017-poster.pdf"
filename = 'poster'
urlretrieve(url, filename + '.pdf')
pdfFileObj = open(filename + '.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
f = open(filename + '_plain.txt', 'w')
f.write(pageObj.extractText())
f.close()
pdfFileObj.close()