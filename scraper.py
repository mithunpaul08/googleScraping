import requests, bs4, sys, webbrowser
res = requests.get('https://www.google.com/search?q=water+availability+tamil+nadu+agriculture')
res.raise_for_status()
#print(res.text[:250])
#code to write the html to a file if you want to
#playFile = open('RomeoAndJuliet.txt', 'wb')
#for chunk in res.iter_content(100000):
#    playFile.write(chunk)
#playFile.close()
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')
numOpen = min(1, len(linkElems))
for i in range(numOpen):
    print(linkElems[i].get('href'))
    #webbrowser.open('http://google.com' + linkElems[i].get('href'))
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
