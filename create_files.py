import pandas as pd

def crate_table(content_list, lang):
    title = content_list[0]
    body = content_list[1]

    print(title)
    molde_tabela = pd.DataFrame(body, columns=title)

    molde_tabela.to_excel(f'tabela teste - {lang}.xlsx', index=False)
