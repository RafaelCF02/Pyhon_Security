from bs4 import BeautifulSoup
import requests 

site = input('Escreva o site que deseja realizar o scraping: ')

scrap = requests.get(site).content

soup = BeautifulSoup(scrap, 'html.parser')

print(soup.prettify())


