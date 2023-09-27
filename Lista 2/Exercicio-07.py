# 7) Seu sonho é construir uma piscina. Para cada metro quadrado, são necessários 120 azulejos. O cálculo de área em metros quadrados, é feito multiplicando a largura pelo comprimento. Digitar os valores (em metros) da largura e comprimento que deseja a piscina. Mostrar na tela a quantidade de azulejos que devem ser comprados e o valor total a ser pago, sendo que uma caixa de azulejo com 60 unidades custa R$45,50.

print('>>Calculo de azulejos para construção de piscina<<\n\n Digite os valores em metros:')

largura = float(input('Digita a largura da piscina: '))
comprimento = float(input('Digite o comprimento da piscina: '))

totalMetragem = largura * comprimento
metroQuadrado = 120
caixaAzulejos = 60
valorCaixaAzulejos = 45.50
totalAzulejos = totalMetragem * metroQuadrado 
valorTotalAzulejos = (totalAzulejos / caixaAzulejos) * valorCaixaAzulejos

print(f'A quantidade de azulejos a serem compradas é: {totalAzulejos}\n\n E o Valor total a ser gasto em azulejos é: {valorTotalAzulejos}')