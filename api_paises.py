"""
API de Países
By Carlos Henrique Barros Silva Campos
"""
import json

import requests

url_all = "https://restcountries.eu/rest/v2/all"
url_nome = "https://restcountries.eu/rest/v2/name"


def req_web(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
    except Exception as err:
        print(f'Erro de requisição em: {url}')


def parsing(json_text):
    try:
        j_paises = json.loads(json_text)
        return j_paises
    except Exception as err:
        print('Erro ao fazer o parsing')


def listar(lst_pais):
    for pais in lst_pais:
        print(pais['name'])


def populacao(nome_pais):
    resp = req_web(f'{url_nome}/{nome_pais}')
    if resp:
        lstp = parsing(resp)
        if lstp:
            for pais in lstp:
                print(f"{pais['name']}: {pais['population']}")


def paises_moedas(nome_pais):
    resp = req_web(f'{url_nome}/{nome_pais}')
    if resp:
        lstp = parsing(resp)
        if lstp:
            for pais in lstp:
                print('Medas do', pais['name'])
                moedas = pais['currencies']
                for moeda in moedas:
                    print(f"{moeda['name']} - {moeda['code']}")


print('Informações de Paises')
values = input('Pais:')
populacao(values)
paises_moedas(values)
