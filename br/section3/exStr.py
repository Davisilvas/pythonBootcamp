name = input("Digite seu nome completo: ")
ageStr = input("Digite a sua idade: ")

if ageStr.isnumeric() and name:
    age = int(ageStr)
    
    if name and age:    
        print(f'Seu nome é {name}')
        print('Seu nome invertido é', name[::-1])
        print('-' * 20)
        if ' ' in name:
            print("Seu nome tem espaços")
        else:
            print("Seu nome não contem espaços")
        print('-' * 20)
        print(f'Seu nome tem {len(name)} letras')
        print(f'A primeira letra do seu nome é {name[0]}')
        print(f'A última letra do seu nome é {name[-1]}')

elif not name:
    print("Você não nos informou o seu nome")
elif not ageStr.isnumeric():
    print("Você não informou um valor numérico para a idade.")
elif not ageStr:
    print("Você não nos informou sua idade.")



