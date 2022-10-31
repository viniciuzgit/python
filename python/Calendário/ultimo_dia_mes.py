import calendar

print('\nDia em que acaba cada mês: \n')
finalmes = calendar.mdays
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro']

cont = 0
cont2 = 1
mes = meses[0]
final = finalmes[0]

for i in meses:
    print(mes)
    mes = meses[cont]
    print(final)
    final = finalmes[cont2]
    cont += 1
    cont2 += 1
