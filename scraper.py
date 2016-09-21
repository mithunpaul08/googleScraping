import requests, bs4
res = requests.get('https://www.extension.iastate.edu/agdm/articles/edwards/EdwMay10.html')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text,"lxml")
type(noStarchSoup)
elems = noStarchSoup.select('div')
type(elems)
len(elems)
