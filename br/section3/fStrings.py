name = 'Davi Silva Santos'
height = 1.851
weight = 110.0
imc = weight / height ** 2

l1 = f'{name} tem {height:.2f} de altura'
l2 = f'pesa {weight}KGs e seu IMC é: {imc:.2f}'

formato = 'Nome = {} | Altura = {} | peso = {} | IMC = {:.2f}'.format(name, height, weight, imc)
# as chaves aceitam os índices dos args
# os parâmetros podem ser nomeados

print(l1)
print(l2)
print(formato)