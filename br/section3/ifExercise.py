primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')
soma = 0

if primeiro_valor.isnumeric() and segundo_valor.isnumeric():
    int(primeiro_valor)
    int(segundo_valor)
    soma = primeiro_valor + segundo_valor

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor= } é maior que o {segundo_valor =}')
    print(f'E a soma dos valores é: ')
else:
    print(f'{segundo_valor= } é maior que o {primeiro_valor =}')
    print(f'E a soma dos valores é: ')