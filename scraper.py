import requests, bs4, sys, webbrowser, html2text, os
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
res = requests.get('https://www.google.com/search?q=water+availability+tamil+nadu+agriculture')
res.raise_for_status()
#print(res.text[:250])
#code to write the html to a file if you want to
#playFile = open('RomeoAndJuliet.txt', 'wb')
#for chunk in res.iter_content(100000):
#    playFile.write(chunk)
#playFile.close()
soup = bs4.BeautifulSoup(res.text,"lxml")
linkElems = soup.select('.r a')
numOpen = min(1, len(linkElems))
#1. download and save html files from the first one results
#1.2 download and save html files from the first ten results

for i in range(numOpen):
    #print(linkElems[i].get('href'))
    #webbrowser.open('http://google.com' + linkElems[i].get('href'))
    res = requests.get('http://google.com' + linkElems[i].get('href'))
    waterResultFile = open('waterResultInHtmlFormat.txt', 'wb')
    for chunk in res.iter_content(100000):
        waterResultFile.write(chunk)
    waterResultFile.close()
os.rename('waterResultInHtmlFormat.txt','waterResultInHtmlFormat.html')
myhtml = open("waterResultInHtmlFormat.html").read()
#write to a file
target = open('waterResultInTxtFormat.txt', 'w')
target.write(html2text.html2text(myhtml))
target.close()
#print html2text.html2text(myhtml)
#todo
#1. download html files from the first ten results
#2. convert html to text, using BeautifulSoup
#3. download pdf files from the first ten results
#4. download html files from the first ten results


# noStarchSoup = bs4.BeautifulSoup(res.text,"lxml")
# type(noStarchSoup)
# elems = noStarchSoup.select('div')
# type(elems[0])
# len(elems)
