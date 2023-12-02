import requests
from bs4 import BeautifulSoup
import pandas as pd

def extrair_dados(site_url):
    
    response = requests.get(site_url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    precos = soup.find_all('span',attrs={"class":"p13n-sc-price"})
    titulos = soup.find_all('div',attrs={"class":"_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"})
    imagens = soup.find_all('img',attrs={"class":"a-dynamic-image p13n-sc-dynamic-image p13n-product-image"})

    lista_precos = [preco.text.replace(u'\xa0',u'') for preco in precos]
    lista_nome = [titulo.text for titulo in titulos]
    lista_imagem = [imagem["src"] for imagem in imagens]

    return lista_precos,lista_nome,lista_imagem
           
def data_save(precos_amazon,titulo_amazon,capa_imagem):
        
    df = pd.DataFrame({
           'Price_amazon': precos_amazon,
           'Title_amazon': titulo_amazon,
           'Capa_amazon': capa_imagem
    })
        
    df.to_csv('analise_precos_livros.csv', index=False)

    print('Dados salvos com sucesso!')
    
site_url='https://www.amazon.com.br/gp/bestsellers/books/7842641011/ref=zg_bs_nav_books_1'

preco,title,imagem=extrair_dados(site_url)
title=title[::2]

status_data=data_save(preco,title,imagem)


print(preco,title)
print(status_data)