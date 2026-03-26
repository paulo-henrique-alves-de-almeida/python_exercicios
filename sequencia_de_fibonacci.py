from time import sleep

print()
print('=' * 25, 'Sequência de Fibonacci', '=' * 25)
print()

conhecimento = ''

while (conhecimento != 'S') and (conhecimento != 'N'):
    conhecimento = input('Você sabe o que é a sequência de Fibonacci? [S/N] ')
    conhecimento = conhecimento.upper().strip()

    if (conhecimento != 'S') and (conhecimento != 'N'):
        print('Digite apenas S ou N.')
        print()

if conhecimento == 'N':
    print('''
Vou te explicar:
    A \033[1msequência de Fibonacci\033[m é uma sucessão numérica infinita onde cada termo, a partir do terceiro, é a soma dos dois anteriores, começando geralmente por 0 e 1.
    
    Ela é famosa por representar padrões de crescimento na natureza, arte e arquitetura, aproximando-se da proporção áurea (ou \033[33mnúmero de ouro\033[m).
    ''')
    print('=' * 160)
print()

numero = -1
termo_1 = 0
termo_2 = 1

while numero < 0:
    try:
        numero = int(input('Digite quantos termos da sequência de Fibonacci quer mostrar: '))
        print()

        if numero < 0:
            print('Digite apenas números naturais.')
            print()
    except:
        print('Digite apenas números.')
        print()

if numero >= 1:
    print(termo_1, end = ' ') if numero <= 50 else print(termo_1) 
    if numero >= 2:
        print(termo_2, end = ' ') if numero <= 50 else print(termo_2)
        if numero >= 3:
                for i in range(3, numero + 1):
                    termo_3 = termo_1 + termo_2
                    print(termo_3, end = ' ') if numero <= 50 else print(termo_3)

                    # troca de termos
                    termo_1 = termo_2
                    termo_2 = termo_3

                    # evita travamento
                    if numero > 1000:
                         sleep(1)

print('''
      ''')
