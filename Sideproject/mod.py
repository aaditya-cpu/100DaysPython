import requests

from bs4 import BeautifulSoup as bs 

inf = open('file.html', 'r')

soup=bs(markup=inf,features='html.parser')
print(soup.prettify)



