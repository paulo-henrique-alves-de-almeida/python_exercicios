import os
from time import sleep
from random import randint

jogador = 0
computador = 0
tentativas = -1

escolhas = ['Pedra', 'Papel', 'Tesoura']

def imprimir_titulo():
    os.system('cls')
    if (tentativas < 0) or (tentativas % 2 == 0):
        print('=' * 20, 'JOKENPÔ', '=' * 20)
    else:
        print('=' * 20, f'JOKENPÔ MELHOR DE {tentativas}', '=' * 20)
        print()
        print(f'{nome}: {jogador} | Computador: {computador}')
    print()

imprimir_titulo()
nome = input('Digite seu nome: ')

while (tentativas < 0) or (tentativas % 2 == 0):
    imprimir_titulo()
    try:
        tentativas = int(input('O jogo terá quantas rodadas? '))

        if (tentativas < 0) or (tentativas % 2 == 0):
            print('Digite apenas números ímpares positivos.')
            sleep(2)
    except:
        print('Digite apenas números.')
        sleep(1)

for t in range(0, tentativas + 1):
    escolha = 0

    while (escolha != 1) and (escolha != 2) and (escolha != 3):
        imprimir_titulo()
        try:
            escolha = int(input('''Escolha:
[1] Pedra
[2] Papel
[3] Tesoura

'''))
            if (escolha != 1) and (escolha != 2) and (escolha != 3):
                print()
                print('Escolha apenas 1, 2 ou 3.')
                sleep(1)
        except:
            print()
            print('Escolha apenas 1, 2 ou 3.')
            sleep(1)

    escolha_computador = randint(1, 3)

    print()
    print('Jo')
    sleep(1)
    print('Ken')
    sleep(1)
    print('Pô')
    print()
    print(f'Você escolheu {escolhas[escolha - 1]} e o computador escolheu {escolhas[escolha_computador - 1]}.')
    print()

    if escolha == escolha_computador:
        print('Empate!')
    elif (escolha == 1 and escolha_computador == 3) or (escolha == 2 and escolha_computador == 1) or (escolha == 3 and escolha_computador == 2):
        print('Você ganhou!')
        jogador += 1
    else:
        print('O computador ganhou!')
        computador += 1
    
    sleep(3)
    
    if (jogador >= (tentativas // 2) + 1) or (computador >= (tentativas // 2) + 1):
        break

os.system('cls')
print('=' * 20, 'FIM DE JOGO', '=' * 20)
print()
print(f'Placar: Jogador {jogador} X {computador} Computador')
print()
if jogador > computador:
    print('Você venceu. Parabéns!!!')
else:
    print('Vitória do computador.')
print()
