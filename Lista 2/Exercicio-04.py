# 4) Um(a) programador(a) deseja, ao final do mês, saber quantas horas por semana em média estudou programação. Crie um programa no qual seja digitado a quantidade de horas de cada semana do mês e no final mostre a média de horas por semana naquele mês.


horasSemana1 = float(input('Digite a quantidade de horas de estudo totais da semana 1: '))
horasSemana2 = float(input('Digite a quantidade de horas de estudo totais da semana 2: '))
horasSemana3 = float(input('Digite a quantidade de horas de estudo totais da semana 3: '))
horasSemana4 = float(input('Digite a quantidade de horas de estudo totais da semana 4: '))
horasSemana5 = float(input('Digite a quantidade de horas de estudo totais da semana 5: '))

TotalDeHoras = (horasSemana1 + horasSemana2 + horasSemana3 + horasSemana5 + horasSemana5) / 5

print(f'Seu total de horas de estudo é: {TotalDeHoras}')