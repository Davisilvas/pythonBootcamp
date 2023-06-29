nameInput = input('Nos informe apenas o seu primeiro nome: ')

try:
    
    nameInput.capitalize()
    strLen = len(nameInput)

    curto = strLen <= 4
    medio = strLen >= 5 and strLen <= 6
    longo = strLen >= 7

    if curto:
        print(f'O nome {nameInput} é curto!')
    elif medio:
        print(f'O nome {nameInput} é médio!')
    elif longo:
        print(f'O nome {nameInput} é longo!')

except:
    ...