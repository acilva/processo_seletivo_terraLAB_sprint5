# SPRINT 5 (terraLAB)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Sobre o projeto

> Nessa sprint, foi utilizado a URL do site da Amazon, onde foi feito uma busca em uma página de Livros sobre os assuntos de Computação, Tecnologias e Mídias Digitais.

# Problema

 > Pensando em uma aplicação, onde um cliente necessita de uma automatização nas análises de dados fornecidas por determinado site. Desenvolva um web scraping em python onde será possível colher informações detalhadas de maneira automatizada e salvá-las em algum arquivo, para que o cliente possa realizar suas análises. O tema é livre e recomendamos a utilização das seguintes bibliotecas: Beautifulsoup e Pandas. E salvar os dados em um arquivo com a extensão ‘.csv’. Segue um exemplo de contexto.Um determinado cliente solicitou a um desenvolvedor que criasse uma aplicação que conseguisse dizer qual o melhor dia para comprar tênis específicos e com os preços mais baixos no site da Netshoes e Centauro, após ele ter observado que os mesmos mudavam de preço constantemente ao longo da semana. E pediu para que salvasse as análise em um arquivo.

# Funcionalidades

Função criada para extrair dados da url do site como: preços, nome dos títulos e imagens da capa.

> def extrair_dados(site_url):

Função criada para salvar os dados dos preços, nome dos tírulos e imagens da capa.

> def data_save(precos_amazon,titulo_amazon,capa_imagem):

Execução do código:

> site_url='https://www.amazon.com.br/gp/bestsellers/books/7842641011/ref=zg_bs_nav_books_1'

> preco,title,imagem=extrair_dados(site_url)

> title=title[::2]

> status_data=data_save(preco,title,imagem)

> print(preco,title)

> print(status_data)

# Autor
> Ana Cláudia da Silva

