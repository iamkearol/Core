import requests , json
import lxml.etree as etree

r = requests.get('http://www.aastocks.com/tc/stocks/quote/quick-quote.aspx?symbol=00001&S=Y')
r2 = r.content.decode("utf-8")
tree = etree.HTML(r2)


name = '//label[@id="SQ_Name"]/text()'

name_list = tree.xpath(name)
print(name_list)
