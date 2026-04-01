from time import sleep
from random import randint

quantidade_jogos = -1

print()
print('=' * 20, 'JOGOS DA MEGA SENA', '=' * 20)
print()

while quantidade_jogos < 0:
    try:
        quantidade_jogos = int(input('Digite a quantidade de jogos a sortear: '))
        
        if quantidade_jogos < 0:
            print('Digite apenas números naturais.')
            print()
    except:
        print('Digite apenas números naturais.')
        print()

print()
for i in range(0, quantidade_jogos):
    jogo = set()
    while len(jogo) < 6:
        jogo.add(randint(1, 60))
    print(f'{i + 1}° Jogo: {jogo}')
    sleep(1)
    print()

print('''<<< BOA SORTE! >>>
        ''')
