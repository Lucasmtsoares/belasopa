import requests
from bs4 import BeautifulSoup

def myscraping():
  print('Iniciando raspagem...')
  url = 'https://www.in.gov.br/web/dou/-/portaria-n-1.933/ifal-de-24-de-maio-de-2024-562373946'
  corpo = requests.get(url)
  soup = BeautifulSoup(corpo.text, 'html.parser')
  titulo = soup.find('div', class_='texto-dou')
  
  return titulo.text
  
  
