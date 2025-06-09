import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.educacao.sp.gov.br/noticias/'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

noticias = []

for item in soup.select('.bloco-noticia'):
    titulo_tag = item.select_one('h3')
    resumo_tag = item.select_one('p')
    link_tag = item.select_one('a')
    imagem_tag = item.select_one('img')

    if titulo_tag and link_tag:
        titulo = titulo_tag.get_text(strip=True)
        link = link_tag['href']
        resumo = resumo_tag.get_text(strip=True) if resumo_tag else ''
        imagem = imagem_tag['src'] if imagem_tag else ''

        # Verifica se imagem tem URL completa
        if imagem and not imagem.startswith('http'):
            imagem = 'https://www.educacao.sp.gov.br' + imagem

        noticias.append({
            'titulo': titulo,
            'resumo': resumo,
            'link': link,
            'imagem': imagem
        })

# Salva em JSON
with open('noticias.json', 'w', encoding='utf-8') as f:
    json.dump(noticias, f, ensure_ascii=False, indent=2)

print(f'{len(noticias)} notícias salvas com sucesso em noticias.json')
