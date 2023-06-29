while True:
    ...
    primeiroInput = input('Digite o primeiro número: ')
    operadorInput = input('Informe um operador [+, -, *, /]: ')
    segundoInput = input('Digite o segundo número: ')
    
    validarOperador = (operadorInput == '+') or \
        (operadorInput == '-') or \
        (operadorInput == '*') or \
        (operadorInput == '/')
    
    if validarOperador:
        soma = operadorInput == '+'
        subtracao = operadorInput == '-'
        multiplicacao = operadorInput == '*'
        divisao = operadorInput == '/'

    resultado = 0
    
    try:
        if primeiroInput.isnumeric():
            valor1 = float(primeiroInput)

        if segundoInput.isnumeric():
            valor2 = float(segundoInput)

        if soma:
            resultado = valor1 + valor2
        elif subtracao:
            resultado = valor1 - valor2
        elif multiplicacao:
            resultado = valor1 * valor2
        elif divisao:
            resultado = valor1 / valor2
    except:
        print('Os valores informados não são numéricos')

    print(f'O resultado é {resultado}')

    inputContinuidade = input(' Deseja realizar outra operação? [S/N]: ')

    parar = inputContinuidade == 'N'
    continuar = inputContinuidade == 'S'

    if parar:
        print('Você optou por não realizar outra operação.')
        break
    elif continuar:
        print('Você optou por continuar fazendo operações')