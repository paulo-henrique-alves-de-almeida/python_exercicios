# o intuito desse projeto cômico é tentar recriar a experiência real de se utilizar um caixa eletrônico no Brasil, com as diversas falhas que podem ocorrer (baseado em experiência própria).

import os
from datetime import datetime, time
from random import randint
from time import sleep

# saque máximo que pode ser definido pelo banco dependendo do horário
agora = datetime.now().time()
limite_noite = time(22, 0)
limite_manha = time(6, 0)
saque_maximo = 0

if (agora < limite_noite) or (agora >= limite_manha):
    saque_maximo = randint(300, 4998)
else:
    saque_maximo = randint(300, 1000)

chance_10 = randint(1, 10) # chance do caixa eletrônico ter notas de 10 reais: 10%
chance_5 = randint(1, 20) # chance do caixa eletrônico ter notas de 5 reais: 5%
chance_2 = randint(1, 50) # chance do caixa eletrônico ter notas de 2 reais: 2%
chance_20_50_100 = randint(1, 5) # chance do caixa eletrônico ter notas de 20, 50 ou 100 reais: 80%
chance_200 = randint(1, 2) #chance do caixa eletrônico ter notas de 200 reais: 50%
chance_quebrado = randint(1, 5) # chance do caixa eletrônico estar quebrado: 20%

dinheiro = 0

def imprimir_titulo():
    os.system('cls')
    print('=' * 20, 'Saque Caixa Eletrônico 24/7', '=' * 20)
    print()


chance_cartao = 5 # chance do cartão não ser reconhecido: 20%
while chance_cartao == 5:
    imprimir_titulo()
    input('''Insira seu cartão
    
    ''')

    sleep(1)
    print()

    chance_cartao = randint(1, 5)

    if chance_cartao == 5:
        print('Cartão não reconhecido. Retire seu cartão.')
        input(' ')

if chance_quebrado == 5:
    input(' ' * 20, 'Fora de funcionamento.')
    print()
else:
    while (dinheiro < 20) or (dinheiro > saque_maximo):
        imprimir_titulo()

        try:
            dinheiro = int(input('Digite a quantidade a ser sacada: R$'))
            print()

            if dinheiro < 20: # valor menor que 20 reais
                print('''O menor valor a ser sacado é 20 reais.
                    ''')
                depositar = input('Digite 1 para depositar ao invés de sacar: ')
                print()

                if depositar == '1':
                    break
                else:
                    sleep(1)
            elif dinheiro >= 5000: # valor a partir de 5000 reais
                agendado = ''
                while (agendado != 'S') and (agendado != 'N'):
                    imprimir_titulo()
                    agendado = input('Você agendou este saque? (S/N) ')
                    agendado = agendado.strip().upper()
                    print()

                    if (agendado != 'S') and (agendado != 'N'):
                        print('Digite apenas S ou N.')
                        sleep(1)
                if agendado == 'S':
                    print('Se dirija ao balcão para sacar seu dinheiro agendado.')
                else:
                    print('Se dirija ao balcão para agendar o seu saque.')
                print()

            elif dinheiro > saque_maximo:
                print(f'O saque máximo permitido é R${saque_maximo}.')
                sleep(2)

            else: # valor (supostamente) possível de ser sacado
                if (chance_10 != 10) and (chance_5 != 20) and (chance_2 != 50) and (chance_200 == 1) and (chance_20_50_100 == 5):
                    print('Não possuímos dinheiro, no momento. Se dirija ao balcão.')
                    print()
                else:
                    notas_200 = notas_100 = notas_50 = notas_20 = notas_10 = notas_5 = notas_2 = 0

                    # enquanto houver dinheiro a ser processado em notas, verifica se há notas e quantas serão precisas
                    while dinheiro > 0:
                        if (dinheiro >= 200) and (chance_200 == 2):
                            notas_200 = dinheiro // 200
                            dinheiro -= notas_200 * 200
                        if (dinheiro >= 100) and (chance_20_50_100 != 5):
                            notas_100 = dinheiro // 100
                            dinheiro -= notas_100 * 100
                        elif (dinheiro >= 50) and (chance_20_50_100 != 5):
                            notas_50 = dinheiro // 50
                            dinheiro -= notas_50 * 50
                        elif (dinheiro >= 20) and (chance_20_50_100 != 5):
                            notas_20 = dinheiro // 20
                            dinheiro -= notas_20 * 20
                        elif (dinheiro >= 10) and (chance_10 == 10):
                            notas_10 = dinheiro // 10
                            dinheiro -= notas_10 * 10
                        elif (dinheiro >= 5) and (chance_5 == 20):
                            notas_5 = dinheiro // 5
                            dinheiro -= notas_5 * 5
                        elif (dinheiro >= 2) and (chance_2 == 50):
                            notas_2 = dinheiro // 2
                            dinheiro -= notas_2 * 2
                        else:
                            break
                        
                    imprimir_titulo()
                    print(' ' * 20, 'PROCESSANDO CÉDULAS... AGUARDE')
                    sleep(3)

                    imprimir_titulo()
                    print('Emitindo cédulas:')
                    print()
                        
                    # imprime todas as notas, como um caixa eletrônico
                    for duzentos in range(0, notas_200):
                        print('R$200')
                    for cem in range(0, notas_100):
                        print('R$100')
                    for cinquenta in range(0, notas_50):
                        print('R$50')
                    for vinte in range(0, notas_20):
                        print('R$20')
                    for dez in range(0, notas_10):
                        print('R$10')
                    for cinco in range(0, notas_5):
                        print('R$5')
                    for dois in range(0, notas_2):
                        print('R$2')
                        
                    if dinheiro > 0:
                        print(f'Se dirija ao balcão para receber os outros R${dinheiro}.')
                    else:
                        print('Saque realizado com sucesso. Volte sempre! :)')
                    print()
        except:
            print()
            print('Digite apenas valores possíveis de serem sacados.')
            sleep(2)
