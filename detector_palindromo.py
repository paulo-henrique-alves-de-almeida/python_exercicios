frase = input('Digite uma frase: ')
frase = frase.replace(' ', '').upper().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ã', 'a').replace('à', 'a').replace('õ', 'o').replace('ü', 'u').replace('ú', 'u').replace('â', 'a').replace('ê', 'e').replace('ô', 'o').replace("a'", 'a').replace("e'", 'e').replace("i'", 'i').replace("u'", 'u').replace("o'", 'o').replace('ë', 'e').replace('ñ', 'n')
frase_invertida = frase[::-1]
print()
print(f'O inverso de {frase} é {frase_invertida}.')

if frase == frase_invertida:
    print('A frase é um palíndromo! :)')
else:
    print('A frase não é um palíndromo.')
print()
