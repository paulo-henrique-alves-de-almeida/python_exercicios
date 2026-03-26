import os
from time import sleep

def imprimir_titulo():
    os.system('cls')
    print('=' * 20, 'TRIÂNGULO RETÂNGULO', '=' * 20)
    print()

base = -1

while base < 0:
    imprimir_titulo()
    try:
        base = int(input('Digite o tamanho da base do triângulo retângulo: '))
        print()

        if base < 0:
            print('Número inválido.')
            sleep(1)
    except: 
        print('Digite um número natural.')
        sleep(1)

caracter = input('Digite o caracter que será usado para formar o triângulo retângulo: ')
print()

# define o máximo para 160 para melhor impressão no terminal
if base > 160:
    base = 160

if base > 0:
    for i in range(1, base + 1):
        print(caracter[0].strip() * i)
print()
