import os
from datetime import date
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def imprimir_titulo(ano):
    os.system('cls')
    if ano:
        print('=' * 20, f'TABELA DO BRASILEIRÃO {ano}', '=' * 20)
    else:
        print('=' * 20, f'TABELA DO BRASILEIRÃO', '=' * 20)
    print()

imprimir_titulo(None)
print('''Vamos ver a tabela do Brasileirão! Aguarde alguns segundos...
''')

try:
    # inicia o navegador e entra no site ge
    options = Options()
    options.add_argument("--headless=new")
    navegador = webdriver.Chrome(options = options)

    url = 'https://ge.globo.com/futebol/brasileirao-serie-a/'
    navegador.get(url)

    # define as faixas de classificação
    faixa_classificacao_element = navegador.find_elements('css selector', '.classificacao__icone.faixa-classificacao__label--icone')    

    faixa_classificacao = [faixa_classificacao_element[0].value_of_css_property('background-color'),
        faixa_classificacao_element[1].value_of_css_property('background-color'),
        faixa_classificacao_element[2].value_of_css_property('background-color'),
        faixa_classificacao_element[3].value_of_css_property('background-color')]

    # encontra os times
    times_element = navegador.find_elements('css selector', '.classificacao__equipes.classificacao__equipes--nome')
    times = list()

    for t in range(0, len(times_element)):
        times.append(times_element[t].text)

    # encontra a posição dos times
    posicao_element = navegador.find_elements('css selector', '.classificacao__equipes.classificacao__equipes--posicao')
    posicoes = list()

    for p in range(0, len(posicao_element)):
        posicoes.append(posicao_element[p].value_of_css_property('color'))
        
    # pergunta ao usuário qual seu time do coração para mostrar sua posição ao fim do programa
    ano_atual = date.today().year

    time_coracao = 0
    while (time_coracao < 1) or (time_coracao > 20):
        imprimir_titulo(ano_atual)
        for p, t in enumerate(sorted(times)):
                print(f'[0{p + 1}] {t}' if p < 9 else f'[{p + 1}] {t}')

        print()
        try:
            time_coracao = int(input('Para qual time você torce? '))
            print()

            if (time_coracao < 0) or (time_coracao > 20):
                print('Digte apenas números entre 1 e 20.')
                sleep(1)
        except:
            print('Digite apenas números.')
            sleep(1)
            
    # exibe a solução do ano atual
    imprimir_titulo(ano_atual)

    for p, t in enumerate(times):
        if posicoes[p] == faixa_classificacao[0]:
            print(f'\033[34m{p + 1}\033[m', end = ' ')
        elif posicoes[p] == faixa_classificacao[1]:
            print(f'\033[36m{p + 1}\033[m', end = ' ')
        elif posicoes[p] == faixa_classificacao[2]:
            print(f'\033[32m{p + 1}\033[m', end = ' ')
        elif posicoes[p] == faixa_classificacao[3]:
            print(f'\033[31m{p + 1}\033[m', end = ' ')
        else:
            print(f'\033[37m{p + 1}\033[m', end = ' ')
                    
        print(t)

    print()
    print('=' * 60)
    print()
    print(f'O G5 está assim: {times[0:5]}')
    print()
    print('=' * 60)
    print()
    print('Times na zona de rebaixamento:', end = ' ')
    for p, t in enumerate(times):
        if posicoes[p] == faixa_classificacao[3]:
            print(t, end = ' ')
    print('''
    ''')
    print('=' * 60)
    print()
    print(f'{sorted(times)[time_coracao - 1]} está na {times.index(sorted(times)[time_coracao - 1]) + 1}° posição.')
    print()
except:
    print('Não consegui encontrar a tabela do Brasileirão... Verfique sua internet.')
    print()
