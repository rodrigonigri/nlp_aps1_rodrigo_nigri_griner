from bs4 import BeautifulSoup
import requests
import csv

# Função para extrair título, artista e letra de uma URL
def extrair_dados(url):
    response = requests.get(url)
    response.raise_for_status()  # Levanta um erro se a requisição falhar
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extrair título
    title_div = soup.find('div', class_='title-content')
    if title_div:
        title = title_div.find('h1', class_='textStyle-primary').get_text(strip=True)
        artist = title_div.find('h2', class_='textStyle-secondary').get_text(strip=True)
        title_artist = f'{title}-{artist}'
    else:
        title_artist = 'Desconhecido'

    # Extrair letra
    lyrics_div = soup.find('div', class_='lyric-original font --lyrics --size18')
    if lyrics_div:
        lyrics = ' '.join(p.get_text(separator='\n', strip=True) for p in lyrics_div.find_all('p'))
    else:
        lyrics = 'Letra não encontrada'

    return title_artist, lyrics

# Ler URLs do arquivo txt
urls = []
with open('urls.txt', 'r') as file:
    urls = file.read().splitlines()

# Criar e escrever no arquivo CSV
with open('musicas.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Título-Artista', 'Letra']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')

    writer.writeheader()
    for url in urls:
        try:
            title_artist, lyrics = extrair_dados(url)
            writer.writerow({'Título-Artista': title_artist, 'Letra': lyrics})
            print(f'Dados salvos para {title_artist}')
        except Exception as e:
            print(f'Erro ao processar {url}: {e}')
