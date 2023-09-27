# 7) Em uma fábrica de reciclagem de materiais, cada 10kg de plástico rendem R$2,00 cada 30kg de papel rendem R$3,00 e cada 50kg de metal rendem R$5,00. Perguntar ao usuário a quantidade (kg) de cada material que deseja entregar na fábrica e mostrar o total que receberá em reais.

#10kg de plástico rendem R$2,00
#30kg de papel rendem R$3,00
#50kg de metal rendem R$5,00

plastico = int(input('Quantos Kg de plastico deseja entregar?'))
papel = int(input('Quantos Kg de papel deseja entregar?'))
metal = int(input('Quantos Kg de metal deseja entregar?'))

totalPlastico = plastico * 2
totalPapel =  papel * 3
totalMetal = metal * 5

print(f'O valor a receber pelo plastico é:{totalPlastico} reais\nO valor a receber pelo papel é:{totalPapel}reais\nO valor a receber pelo metal é:{totalMetal}reais')