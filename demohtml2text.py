#just a sandbox/testbed file

import PyPDF2

pdfFileObj = open('test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
extractedText=pageObj.extractText()
print extractedText


# stubFilename='waterResults'
# for i in range(11):
#     combinedFileName=stubFilename +`i` + '.txt'
#     print combinedFileName
#
#stubFilename='waterResults'
#for i in range(11):
#    stubFilename +=`i`
#print stubFilename

#combinedFileName=stubFilename +=2
#print combinedFileName

# # encoding=utf8
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf8')
# import html2text
# #os.rename('waterResult1.txt','waterResult1.html')
# myhtml = open("rename1.htm").read()
# print html2text.html2text(myhtml)
