import re
import json
from urllib.request import urlopen

def consultar_ip(endereco_ip):
    url = f'https://ipinfo.io/{endereco_ip}/json'

    resposta = urlopen(url)

    dados = json.load(resposta)

    ip = dados['ip']
    org = dados['org']
    cid = dados['city']
    pais = dados['country']
    regiao = dados['region']
    loc = dados['loc']

    print('Detalhes do IP externo:')
    print(f'IP: {ip}\nRegião: {regiao}\nPaís: {pais}\nCidade: {cid}\nOrganização: {org}\nGeolocalização: {loc}')

endereco_ip = input('Digite o IP que deseja consultar: ')
consultar_ip(endereco_ip)