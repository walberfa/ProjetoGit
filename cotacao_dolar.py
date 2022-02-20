import requests
import json

#Busca o dicionário de cotações na Awesome API
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid']

print(f'A cotação atual do dolar é: R$', cotacao_dolar)