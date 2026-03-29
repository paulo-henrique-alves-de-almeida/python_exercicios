idade_grupo = 0
maior_idade_homem = -1
nome_homem_velho = ''
mulheres_sub_20 = 0

for i in range(1, 5):
    # reseta as variáveis
    sexo = ''
    idade = -1

    print()

    print(f'===== {i}° pessoa =====')
    # coleta o nome da pessoa {i}
    nome = input('Nome: ')
    nome = nome.strip()

    # coleta o sexo da pesso {i}
    while (sexo != 'M') and (sexo != 'F'):
        sexo = input('Sexo [M/F]: ')
        sexo = sexo.upper().strip()

        if (sexo != 'M') and (sexo != 'F'):
            print('Digite apenas M ou F.')
            print()
    
    # coleta a idade da pessia {i}
    while (idade < 0) or (idade > 125):
        try:
            idade = int(input('Idade: '))

            if (idade < 0) or (idade > 125):
                print('Idade inválida.')
                print()
        except:
            print('Digite apenas números.')
            print()

    # soma a idade de todos do grupo
    idade_grupo += idade

    # verifica a idade do homem mais velho
    if (idade > maior_idade_homem) and (sexo == 'M'):
        maior_idade_homem = idade
        nome_homem_velho = nome
    
    # conta quantas mulheres têm menos de 20 anos
    if (idade < 20) and (sexo == 'F'):
        mulheres_sub_20 += 1

media_idade = idade_grupo / 4

print()
print('=' * 50)
print()
print(f'A média de idade do grupo é {media_idade:.2f}.')
print(f'O nome do homem mais velho é {nome_homem_velho} e tem {maior_idade_homem} anos.') if maior_idade_homem != -1 else print('Não existem homens.')
print(f'Existem {mulheres_sub_20} mulheres com menos de 20 anos.')
print()
