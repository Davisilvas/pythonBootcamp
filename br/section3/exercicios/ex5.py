inputHora = input('Que horas são?? ')

try:
    hora = int(inputHora)

    manha = hora >= 0 and hora <= 11
    tarde = hora >= 12 and hora <= 17
    noite = hora >= 18 and hora <= 23

    msg = ' '

    if manha:
        msg = 'Bom dia flor do dia'
    elif tarde:
        msg = 'Boa tarde'
    elif noite:
        msg = 'Boa noite'
    else:
        msg = 'O horário informado não se adequa ao formato 24 horas.'
    
    print(msg)

except:
    print('O horário informado não se adequa ao formato 24 horas.')
