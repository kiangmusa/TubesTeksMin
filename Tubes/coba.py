myname = "Angky-Makan_Nasi"
from bs4 import BeautifulSoup as BS
from xml.etree import cElementTree as ET
import xml.dom.minidom
file = 'B:/Kul/Teksmin/dataset/Training101/6146.xml'
xmlObject = xml.dom.minidom.parse(file)
xmlstr = xmlObject.toprettyxml()
xmlstr = str(xmlstr)
soup = BS(xmlstr, 'html.parser')
a = soup.find_all('text')
for link in a:
    b = (link.get_text())
print(b.casefold())



