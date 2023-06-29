contador = -5

while contador <= 10:
    print(contador)
    contador += 1 
    # -> Essa var 'contador' vai acabar com valor 11.

print('acabou o loop while 1.')

print('#' * 15)

while contador <= 20:
    print(contador)
    contador += 1
    if contador == 15:
        print("OPA, CHEGOU NO 15. VOU PULAR FORA")
        break

print('#' * 15)
    
while contador <= 20:
    if contador == 17:
        print("O 17 a gente não printa")
        contador +=1
        continue
        # Do continue pra baixo não é mais executado.
    print(contador)
    contador +=1 
