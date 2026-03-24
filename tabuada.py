print()
print('=' * 20, 'TABUADA', '=' * 20)
print()

# coleta de qual número será a tabuada
while True:
    try:
        numero = int(input('Digite o número do qual quer ver a tabuada: '))
        print()
    except:
        print('Digite apenas números inteiros.')
        print()
    else:
        break

# coleta quantos termos a tabuada terá
termos = -1
while termos < 0:
    try:
        termos = int(input('Digite quantos termos a tabuada terá: '))
        print()

        if termos < 0:
            print('Digite apenas números naturais.')
            print()
    except: 
        print('Digite apenas números naturais.')
        print()

for i in range (0, termos + 1):
    print(numero, 'X', i, '=', numero * i)
print()
