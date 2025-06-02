from bs4 import BeautifulSoup
import requests

url="https://www.upv.es/titulaciones/GII/menu_1013007c.html"

pagina=requests.get(url)

print(pagina)
html = BeautifulSoup(pagina.text, 'html.parser')

print(html)
