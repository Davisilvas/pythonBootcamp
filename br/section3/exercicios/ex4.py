'''
def verificaPar(n):
    verificacao = n % 2
    if verificacao == 0:
        return print(f"O número {n} é par!")
    else:
        return print(f"O número {n} é impar!")


try:
    num = input("Por favor digite um número inteiro: ")
    intNum = int(num)

    if intNum is int:
        calc = intNum % 2
        if calc == 0:
            print("é par")
        else:
            print("é impar")

    elif intNum is float:
        print("O valor informado deve ser do tipo INTEIRO!")

except Exception as e:
    print(e)
'''

entrada = input("Digite um número inteiro: ")

try:
    entrada_int = float(entrada)
    par_impar= entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'
    
    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')