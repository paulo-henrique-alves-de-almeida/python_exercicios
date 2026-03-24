import os
from time import sleep

segundos = -1
pro_reg = 0

def imprimir_titulo(seg):
    os.system('cls')
    if seg == 0:
        print('=' * 20, 'CONTAGEM', '=' * 20)
    else:
        print('=' * 15, f'CONTAGEM DE {seg} SEGUNDOS', '=' * 15)
    print()

imprimir_titulo(0)

# coleta a quantidade de segundos que a contagem terá
while segundos < 0:
    try:
        segundos = int(input('Digite quantos segundos quer contar: '))
        print()

        if segundos < 0:
            print('Digite apenas números naturais.')
    except:
        print('Digite apenas números naturais.')
        print()

imprimir_titulo(segundos)

# coleta o tipo de contagem
while (pro_reg < 1) or (pro_reg > 2):
    try:
        pro_reg = int(input('''Escolha como será a contagem:
[1] Progressiva
[2] Regressiva
'''))
        print()

        if (pro_reg < 1) or (pro_reg > 2):
            print('Digite apenas 1 ou 2.')
            print()
    except:
        print('Digite apenas 1 ou 2.')
        print()

imprimir_titulo(segundos)

if pro_reg == 1:
    for i in range(1, segundos + 1):
        print(i)
        sleep(1)
else:
    for i in range(segundos, 0, -1):
        print(i)
        sleep(1)
print('''
FIM
''')
