import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

casa = 1

def get_tabel_content(link, lang):
    title_content =[]
    body_content = []
    body_content_translated = []

    start = 0
    cont = 0

    html_text = requests.get(link).text
    site = BeautifulSoup(html_text, 'html.parser')
    table = site.find_all('tr', attrs={'role': 'row'})

    # coleta os titles da table
    for row_title in table:
        row = row_title.find_all('th', attrs={'class': 'title'})

        for ct in row:
            translated = GoogleTranslator(source='auto', target=lang).translate(ct.text)
            title_content.append(translated)
    

    # coleta o conteudo da table
    for rows_corpo in table:
        row = rows_corpo.find_all('td', attrs={'class': 'ct'})

        num_row = len(row)
        
        for ct in row:
            if ct != None:
                translated = GoogleTranslator(source='auto', target=lang).translate(ct.text)
                body_content_translated.append(translated)

        if body_content_translated:
            body_content.append(body_content_translated[start:num_row + cont])

        cont = num_row
        start += num_row
 
    return [title_content, body_content]

def get_content():
    return casa