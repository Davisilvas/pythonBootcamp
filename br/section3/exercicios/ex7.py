name = 'Davi Silva Santos'
counter = 0
newStr = ''

while counter < len(name):
    letter = name[counter]
    newStr += f'*{letter}'
    counter += 1


newStr += '*'
print(newStr)

#PARA ITERAR DESTA MANEIRA TEM QUE ISOLAR A LETRA ANTES CABEÇÃO