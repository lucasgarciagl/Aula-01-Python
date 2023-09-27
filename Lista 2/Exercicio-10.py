# 10) Uma pousada cobra R$280 reais a diária por quarto e R$15 reais o café por pessoa por dia. Você pretende passar um tempo com alguns amigos nessa pousada, sendo que todos ficarão no mesmo quarto. Informar a quantidade de pessoas, o número de diárias e quantas pessoas do grupo vão querer café diário. Mostrar na tela o total a pagar.


pessoas = int(input('Informe a quantidade de pessoas hospedadas: '))
qtdDiaria = int(input('Informe a quantidade diárias: '))
cafeDiaria = int(input('Quantas pessoas irão querer o café diário?: '))


valorDiaria = 280
valorCafe = 15

totalDiaria =  qtdDiaria * valorDiaria
totalCafe = cafeDiaria * valorCafe

totalGeral = totalDiaria + totalCafe

print(f'O total de sua diária na hospedagem é de : R${totalGeral} reais!')