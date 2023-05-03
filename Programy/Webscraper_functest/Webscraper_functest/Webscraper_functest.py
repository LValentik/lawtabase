import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.kurzy.cz/zakony/89-2012-obcansky-zakonik/paragraf-1/')
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.findAll('p.odst')
print(links)


