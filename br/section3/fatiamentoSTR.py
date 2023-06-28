"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
O índice final normalmente não é incluso.
"""
variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[4:8])
print(variavel[4:8:2])
print(variavel[4::2])
print(variavel[::-1])

print(8 * "-")
print(len(variavel))