name = input("Whats your name? ")

valor1 = int(input("Insita o primeiro valor "))
valor2 = int(input("Insita o segundo valor "))
# Isso acima é um code smells, a melhor forma seria pegar o valor, validar ele e depois fazer o cast do valor.

soma = valor1 + valor2

print("Irei somar os valores...")
print(f'A soma dos valores é: {soma}') #{soma=}