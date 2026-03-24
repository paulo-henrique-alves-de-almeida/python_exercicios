print()
print('=' * 20, 'PROGRESSÃO ARITMÉTICA', '=' * 20)
print()

# coleta o primeiro termo da PA
while True:
    try:
        p_termo = float(input('Digite o primeiro termo da PA: '))
        print()
    except:
        print('''Digite apenas números.
OBS: Utilize "." ao invés de ",". Exemplo: 5.50.
              ''')
    else:
        break

# coleta a razão da PA
while True:
    try:
        razao = int(input('Digite a razão da PA: '))
        print()
    except:
        print('''Digite apenas números.
OBS: Utilize "." ao invés de ",". Exemplo: 5.50.
              ''')
    else:
        break

# coleta a quantidade de termos
termos = -1
while termos < 0:
    try:
        termos = int(input('Digite a quantidade de termos: '))
        print()

        if termos < 0:
            print('Digite apenas números naturais.')
            print()
    except:
        print('Digite apenas números naturais.')
        print()

# mostra os termos da PA
contador = 0
while contador < termos:
    print(f'{contador + 1}° termo:', end = ' ')
    print(f'{p_termo:.0f}') if p_termo % 1 == 0 else print(f'{p_termo:.2f}')
    p_termo += razao
    contador += 1
print()
