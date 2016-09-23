import requests, bs4, sys, webbrowser, html2text, os , PyPDF2

# encoding=utf8
# the html file written by beautifulsoup4 wasnt getting parsed by html2text.
#So converted it to default utf8 encoding

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#print os.getcwd()
os.chdir('../../outputs/')
#print os.getcwd()
#exit()
#various typical requests
#todo: add into a string array and call ?
#res = requests.get('https://www.google.com/search?q=pests+diseases+tamil+nadu+agriculture')
#res = requests.get('https://www.google.com/search?q=soil+degradation+tamil+nadu+agriculture')
res = requests.get('https://www.google.com/search?q=farm+sizes+tamil+nadu+agriculture')

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"lxml")
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    #find if href has .pdf in it
    res = requests.get('http://google.com' + linkElems[i].get('href'))
    res.raise_for_status()

    #create a unique file name to store each of the results
    stubFilename='waterResults'
    combinedFileName=stubFilename +`i`
    waterResultFile = open(combinedFileName, 'wb+')
    for chunk in res.iter_content(100000):
        waterResultFile.write(chunk)
    waterResultFile.close()
    hrefValue=linkElems[i].get('href')

    if(hrefValue.find('.pdf')>0):
        print 'file number ' + `i`+  ' is a pdf file'
        os.rename(combinedFileName,combinedFileName+'.pdf')
        pdfFileObj = open(combinedFileName+'.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        extractedText=pageObj.extractText()

        for i in xrange(pdfReader.getNumPages()):
            pageObj = pdfReader.getPage(i)
            extractedText=extractedText+pageObj.extractText()

        #remove the file if it already exists
        try:
            os.remove(combinedFileName+'InTxtFormat.txt')
        except OSError:
            pass

        #write the extracted text from pdf document to a txt file
        target = open(combinedFileName+'InTxtFormat.txt', 'w')
        target.write(extractedText)
        target.close()
    else:
        #if file is html or txt
        print'file number ' + `i`+  ' is not a pdf file'

        #get the unicode converted file and rename it as html
        os.rename(combinedFileName,combinedFileName+'.html')

        #read into an html handle
        #myhtml = open(outputDirectory+combinedFileName+".html").read()
        myhtml = open(combinedFileName+".html").read()

        #remove the file if it already exists
        try:
            #os.remove(outputDirectory+combinedFileName+'InTxtFormat.txt')
            os.remove(combinedFileName+'InTxtFormat.txt')
        except OSError:
            pass

    	#ignore links
        h = html2text.HTML2Text()
    	# Ignore converting links from HTML
    	h.ignore_links = True
    	#convert html to text
    	convertedText=h.handle(myhtml)

        # #write the converted text to a txt file
        #target = open(outputDirectory+combinedFileName+'InTxtFormat.txt', 'w')
        target = open(combinedFileName+'InTxtFormat.txt', 'w')
        target.write(html2text.html2text(convertedText).encode('utf-8'))
        target.close()






#todo
#1.1 download and save html files from the first one results---done
#1.2 download and save html files from the first ten results----done
#1.3 download html files from the first ten results---done
#2. convert first 10 html results to text and save them---done
#3. download pdf files from the first ten results--done
#4. convert the pdf files into txt and save them---done
#5. create a folder structure
