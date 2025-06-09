import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.educacao.sp.gov.br/noticias/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

noticias = []
for item in soup.select('.bloco-noticia')[:10]:
    titulo = item.select_one('h3').get_text(strip=True)
    link = item.select_one('a')['href']
    resumo = item.select_one('p').get_text(strip=True) if item.select_one('p') else ''
    
    noticias.append({
        'titulo': titulo,
        'resumo': resumo,
        'link': link
    })

with open('noticias.json', 'w', encoding='utf-8') as f:
    json.dump(noticias, f, ensure_ascii=False, indent=2)

print("Arquivo noticias.json atualizado com sucesso!")
