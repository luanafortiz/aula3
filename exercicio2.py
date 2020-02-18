dias = {1:'domingo',2: 'segunda', 3:'terça',4:'quarta',5:'quinta',6:'sexta',7:'sabado'}
diadasemana = int(input('digite o numero do dia da semana: '))
if diadasemana <= 7:
    resposta = dias[diadasemana]
    print(resposta)
else:
    print('digite um número entre 1 e 7')