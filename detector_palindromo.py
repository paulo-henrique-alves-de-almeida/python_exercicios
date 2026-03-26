frase = input('Digite uma frase: ')
frase = frase.replace(' ', '').upper()
frase_invertida = frase[::-1]
print()
print(f'O inverso de {frase} é {frase_invertida}.')

if frase == frase_invertida:
    print('A frase é um palíndromo! :)')
else:
    print('A frase não é um palíndromo.')
