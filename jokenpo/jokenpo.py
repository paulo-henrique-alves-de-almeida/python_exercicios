import os
from time import sleep
from random import randint
from datetime import datetime

def imprimir_titulo_jokenpo():
    os.system('cls')
    if (rodadas < 0) or (rodadas % 2 == 0):
        print('=' * 20, 'MENU JOKENPÔ', '=' * 20)
    elif rodadas == 1:
        print('=' * 20, 'JOKENPÔ - RODADA ÚNICA', '=' * 20)
    else:
        print('=' * 20, f'JOKENPÔ - MELHOR DE {rodadas}', '=' * 20)
    print()

    if (rodadas > 0) and (rodadas % 2 == 1):
        print(f'{nome}: {jogador} | Computador: {computador}')
        print()

def historico_existe():
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'historico.txt'), 'r') as historico:
            conteudo = historico.read()

            if not conteudo.strip():
                return False
    except FileNotFoundError:
        return False
    else:
        return True

def print_erro(msg):
    print()

# definições
contador = 0
nome = ''
escolhas = ['Pedra', 'Papel', 'Tesoura']
menu = 1

while (menu != 3):

    # reseta os dados de jogo
    jogador = 0
    computador = 0
    rodadas = -1

    # se o arquivo de histórico de jogos existe, mostra o menu
    # caso contrário, o programa vai direto para o jogo

    if historico_existe():
        menu = 0
        while (menu != 1) and (menu != 2) and (menu != 3):
            imprimir_titulo_jokenpo()
            try:
                menu = int(input('''[1] Jogar Jokenpô
[2] Mostrar Histórico de Jogos
[3] Sair do jogo
                                
'''))
                if (menu != 1) and (menu != 2) and (menu != 3):
                    print('Digite apenas 1, 2 ou 3.')
                    sleep(1)
            except:
                print('Digite apenas 1, 2 ou 3.')
                sleep(1)

    match menu:
        case 1: # opção 1: Jogar Jokenpô

            # coleta o nome do usuário na primeira iteração
            if contador == 0:
                while (len(nome) < 3) or (len(nome) > 50):
                    imprimir_titulo_jokenpo()
                    nome = input('Digite seu nome: ').strip().capitalize()

                    if (len(nome) < 3) or (len(nome) > 50):
                        print('Digite um nome entre 3 e 50 caracteres')
                        sleep(2)
            contador += 1

            # coleta a quantidade de rodadas
            while (rodadas < 0) or (rodadas % 2 == 0):
                imprimir_titulo_jokenpo()
                print(f'Nome: {nome}')
                print()
                try:
                    rodadas = int(input('O jogo terá quantas rodadas? '))

                    if (rodadas < 0) or (rodadas % 2 == 0):
                        print('Digite apenas números ímpares positivos.')
                        sleep(2)
                except:
                    print('Digite apenas números.')
                    sleep(1)

            # inicia o jogo

            for t in range(0, rodadas + 1):
                escolha = 0

                while (escolha != 1) and (escolha != 2) and (escolha != 3):
                    imprimir_titulo_jokenpo()
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

                imprimir_titulo_jokenpo()

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
                
                if (jogador >= (rodadas // 2) + 1) or (computador >= (rodadas // 2) + 1):
                    sleep(2)
                    break

                sleep(3)

            # salva o placar em um arquivo com o histórico de jogos
            placar = f'Placar: {nome} {jogador} X {computador} Computador'
            agora = datetime.now()
            mode = 'w+'
            if historico_existe():
                mode = 'a'

            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'historico.txt'), mode, encoding='utf-8') as historico:
                historico.write(f'{placar} | Data: {agora.day if agora.day >= 10 else '0' + str(agora.day)}/{agora.month if agora.month >= 10 else '0' + str(agora.month)}/{agora.year if agora.year >= 10 else '0' + str(agora.year)} | Hora: {agora.hour if agora.hour >= 10 else '0' + str(agora.hour)}:{agora.minute if agora.minute >= 10 else '0' + str(agora.minute)} \n\n')

            # mostra o resultado final
            os.system('cls')
            print('=' * 20, 'FIM DE JOGO', '=' * 20)
            print()
            print(placar)
            print()

            if jogador > computador:
                print('Você venceu. Parabéns!!!')
            else:
                print('Vitória do computador.')
            print()
            input('Digite enter para voltar')

        case 2: # opção 2: exibir histórico de jogos
            
            os.system('cls')
            print('=' * 20, 'HISTÓRICO DE JOGOS', '=' * 20)
            print()

            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'historico.txt'), 'r') as historico:
                print(historico.read().lstrip())

                if not historico_existe():
                    print('Histórico de jogos inexistente.')
                    print()
                else:
                    print()
                    historico.seek(0)
                    total_jogos = sum(1 for jogo in historico)
                    print(f'Total de jogos: {(total_jogos / 2):.0f}')
                    print()
            
            input('Digite enter para voltar ')
        
        case 3:
            imprimir_titulo_jokenpo()
            print('Obrigado por jogar! :)')
            print()
