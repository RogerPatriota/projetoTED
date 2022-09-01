from webscraping import get_tabel_content, get_content
from create_files import crate_table


print('Bem vindo ao gerador de arquivos traduzidos')

confluence_page = input('Informe o link do Confulence: ')

conteudo = get_tabel_content('http://127.0.0.1:5500/index.html', confluence_page)

#crate_table(conteudo, confluence_page)
print(get_content())
