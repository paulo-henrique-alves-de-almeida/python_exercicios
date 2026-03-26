print()
print('=' * 15, 'DETECTOR DE NÚMEROS PRIMOS', '=' * 20)
print()

numero = 0
while numero <= 1:
    try:
        numero = int(input('Digite um número: '))
        print()

        if numero <= 1:
            print('Digite apenas números naturais maiores que 1.')
            print()
    except:
        print('Digite apenas números naturais maiores que 1.')
        print()

# contador de números que dividem o número digitado
cont = 0

for i in range (1, numero + 1):
    if numero % i == 0:
        if numero <= 1000:
            print(f'\033[33m{i}\033[m', end = ' ')
        cont += 1
    else:
        if numero <= 1000:
            print(f'{i}', end = ' ')

print('''
''')
if cont == 2:
    print(f'O número {numero} é divisível apenas por 1 e por ele mesmo. Portanto, é primo')
    if numero > 1000:
        print('Incrível!')
else:
    print(f'O número {numero} é divisível por {cont} números. Portanto, não é primo.')
print()
