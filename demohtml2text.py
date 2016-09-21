# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import html2text
#os.rename('waterResult1.txt','waterResult1.html')
myhtml = open("rename1.htm").read()
print html2text.html2text(myhtml)
