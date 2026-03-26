print()
print('=' * 25, 'FATORIAL E TERMINAL', '=' * 25)
print()

# pergunta ao usuário se conhece os conceitos do programa

conhecimento = 0

while (conhecimento != 1) and (conhecimento != 2):
    try:
        conhecimento = int(input('''Você conhece os conceitos de Fatorial e Terminal de um número?
[1] Sim
[2] Não
'''))
        if (conhecimento < 1) or (conhecimento > 2):
            print('Digite apenas 1 ou 2.')
            print()
    except:
        print('Digite apenas 1 ou 2.')
        print()

if conhecimento == 2:
    print('''
Vou te explicar:
          
    \033[1mFatorial: \033[mO fatorial (representado por n!) é o produto de um número natural por todos os seus antecessores inteiros até 1.
          
    \033[1mTerminal: \033[mO terminal de um número natural (representado como n?) é a soma de todos os números inteiros positivos até 1.
''')
    print('=' * 160)
print()

# coleta o número
numero = -1
fot = 0
label = ''

while numero < 0:
    try:
        numero = int(input('Digite um número natural: '))

        if numero < 0:
            print('O número não pode ser negativo.')
            print()
    except:
        print('Digite apenas números naturais.')
        print()

print()

# coleta a escolha do usuário
while (fot != 1) and (fot != 2):
    try:
        fot = int(input('''Escolha o que calcular com o número:
[1] Fatorial
[2] Terminal
'''))
    
        if (fot < 1) or (fot > 2):
            print('Digite apenas 1 ou 2.')
            print()
    except:
        print('Digite apenas 1 ou 2.')
        print()

resultado = 1 if fot == 1 else 0
print()

for n in range(numero, 0, -1):
    if fot == 1:
        resultado *= n
    else:
        resultado += n

    if n == numero:
        label = str(n)
    else:
        label += f' x {n}' if fot == 1 else f' + {n}'

if (numero < 1000) and (numero > 0):
    print(f'{numero}!', end = ' ') if fot == 1 else print(f'{numero}?', end=' ')
    print(f'= {label} = {resultado}')
else:
    print(f'{numero}! = {resultado}') if fot == 1 else print(f'{numero}? = {resultado}')
print()
