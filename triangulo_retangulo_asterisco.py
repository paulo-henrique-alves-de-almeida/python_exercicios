base = -1

while base < 0:
    try:
        print()
        base = int(input('Digite o tamanho da base do triângulo retângulo: '))

        if base < 0:
            print()
            print('Número inválido.')
            print()
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    except: 
        print()
        print('Digite um número natural.')
        print()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print()
caracter = input('Digite o caracter que será usado para formar o triângulo retângulo: ')
print()

if base != 0:
    for i in range(1, base + 1):
        print(caracter * i)
print()