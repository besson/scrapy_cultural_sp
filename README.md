# scrapy_cultural_sp
Scrapy scripts para extrair programação da virada cultural paulista 2016.
Esse projeto é apresentado na vídeo [aula sobre Scrapy](https://www.youtube.com/watch?v=rj8Sqsgh5TM) do curso de [Introdução à Ciência da Computação com Python Parte 1](https://www.coursera.org/learn/ciencia-computacao-python-conceitos) criado pela CCSL IME-USP

## Requisitos para a instalação
Para rodar a versão atual do Scrapy cultural SP, é necessário:

- Python 3
- Scrapy 1.4.0

## Instalação usando virtualenv

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Instalação usando conda
Siga as instruções definidas em https://anaconda.org/conda-forge/scrapy

## Executando o projeto
```
scrapy crawl virada_cultural
```
