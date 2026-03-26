from random import randint
from time import sleep

numero_computador = randint(1, 10)
numero = 0
tentativas = 0

print()
print('=' * 15, 'JOGO DA ADIVINHAÇÃO', '=' * 15)
print('''
Vou pensar em um número inteiro, aguarde...
''')
sleep(3)

while numero != numero_computador:
    try:
        numero = int(input('Em que número eu estou pensando? '))
        tentativas += 1
    except:
        print('''Esse nem é um número inteiro rsrs
              ''')
    else:
        sleep(1)
        if numero < numero_computador:
            print('O número é maior... Tente novamente')
        elif numero > numero_computador:
            print('O número é menor... Tente novamente')
        print()

print(f'''Parabéns!!! Você acertou, o número era {numero_computador}!
Você acertou em {tentativas} tentativas.
''')
