from num2words import num2words
from time import sleep

print()
print('=' * 15, 'NÚMERO POR EXTENSO', '=' * 15)
print()

# coleta o número de começo
while True:
    try:
        comeco = int(input('Digite qual será o número inicial: '))
    except:
        print('Digite apenas números inteiros.')
    else:
        break
print()

# coleta o número do fim
while True:
    try:
        final = int(input('Digite qual será o número final: '))
    except:
        print('Digite apenas números.')
    else:
        break
print()
print('=' * 30)
print()

passo = 1

if final < comeco:
    passo = -1

for n in range(comeco, final + passo, passo):
    print(f'{n} - {num2words(n, lang = 'pt-BR')}')
    if ((final - comeco) > 1000) or ((final - comeco) < -1000):
        sleep(1)
