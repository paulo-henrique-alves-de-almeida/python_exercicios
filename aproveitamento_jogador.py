import os
from time import sleep

jogador = {'nome': ''}

def imprimir_titulo():
    os.system('cls')
    if jogador['nome']:
        print('=' * 20, f'APROVEITAMENTO DE {jogador['nome'].upper()}', '=' * 20)
    else:
        print('=' * 20, 'APROVEITAMENTO DO JOGADOR', '=' * 20)
    print()

imprimir_titulo()

jogador['nome'] = input('Digite o nome do jogador: ').capitalize().strip()
print()

jogador['partidas'] = -1
while jogador['partidas'] < 0:
    imprimir_titulo()
    print(f'''Nome: {jogador['nome']}
''')
    try:
        jogador['partidas'] = int(input(f'Digite quantas partidas {jogador['nome']} jogou: '))
        
        if jogador['partidas'] < 0:
            print('Digite apenas números naturais')
            sleep(1)
    except:
        print('Digite apenas números naturais')
        sleep(1)
print()

jogador['gols'] = list()
jogador['assist'] = list()
for j in range(1, jogador['partidas'] + 1):
    gols = -1
    assist = -1
    while (gols < 0) or (assist < 0):
        try:
            gols = int(input(f'Digite a quantidade de gols no {j}° jogo: '))
            assist = int(input(f'Digite a quantidade de assistências no {j}° jogo:  '))

            if (gols < 0) or (assist < 0):
                print('Gols contra não contam. Digite apenas números positivos.')
                print()
        except:
            print('Digite apenas números naturais.')
            print()
            
    jogador['gols'].append(gols)
    jogador['assist'].append(assist)
    print()

jogador['gols_totais'] = sum(jogador['gols'])
jogador['assist_totais'] = sum(jogador['assist'])

jogador['g+a'] = jogador['gols_totais'] + jogador['assist_totais']

jogador['aproveit'] = (jogador['g+a'] / jogador['partidas']) * 100

imprimir_titulo()

print(f'''O jogador {jogador['nome']} jogou {jogador['partidas']} partidas:
''')

for j in range(0, jogador['partidas']):
    print(f' => Na {j + 1}° partida fez {jogador["gols"][j]} gols e {jogador['assist'][j]} assitências.')
print()
print(f'Fez {jogador['gols_totais']} gols e {jogador['assist_totais']} assistências no campeonato.')
print(f'Teve {jogador['g+a']} participações em gols em {jogador['partidas']} jogos.')
print(f'Teve aproveitamento de {jogador['aproveit']:.2f}%')
print()