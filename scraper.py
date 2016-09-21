import requests, bs4, sys, webbrowser, html2text, os , PyPDF2
# encoding=utf8
# the html file written by beautifulsoup4 wasnt getting parsed by html2text.
#So converted it to default utf8 encoding
import sys
reload(sys)
sys.setdefaultencoding('utf8')
res = requests.get('https://www.google.com/search?q=pests+diseases+tamil+nadu+agriculture')
res.raise_for_status()
#print(res.text[:250])
#code to write the html to a file if you want to
#playFile = open('RomeoAndJuliet.txt', 'wb')
#for chunk in res.iter_content(100000):
#    playFile.write(chunk)
#playFile.close()
soup = bs4.BeautifulSoup(res.text,"lxml")
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
#1. download and save html files from the first one results---done
#1.2 download and save html files from the first ten results----done

for i in range(numOpen):
    #print(linkElems[i].get('href'))
    #webbrowser.open('http://google.com' + linkElems[i].get('href'))
    #find if href has .pdf in it
    res = requests.get('http://google.com' + linkElems[i].get('href'))
    res.raise_for_status()
    #soup = bs4.BeautifulSoup(res.text,"lxml")
    #print soup

    #create a unique file name to store each of the results
    stubFilename='waterResults'
    combinedFileName=stubFilename +`i`
    waterResultFile = open(combinedFileName, 'wb')
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


        #print extractedText

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
        #os.rename('waterResultInHtmlFormat.txt','waterResultInHtmlFormat.html')
        os.rename(combinedFileName,combinedFileName+'.html')

        #read into an html handle
        myhtml = open(combinedFileName+".html").read()

        # #write the text from html page to a txt file
        target = open(combinedFileName+'InTxtFormat.txt', 'w')
        target.write(html2text.html2text(myhtml))
        target.close()






#todo
#1.2 download html files from the first ten results---done
#2. convert first 10 html results to text and save them---done
#3. download pdf files from the first ten results
#4. convert the pdf files into txt and save them
#5. create a folder structure
