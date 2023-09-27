# 2) Na sua lista de compras do mercado, constam apenas 3 itens: arroz, batata palha e um suco de garrafa. Porém, você possui apenas uma nota de R$100 para pagar. Faça um programa no qual sejam digitados os valores dos itens e mostre na tela valor que você deve receber (troco).


ValorArroz = float(input('Qual o valor do Arroz? '))
ValorBatataPalha = float(input('Qual o valor da Batata Palha? '))
ValorSucoDeGarrafa = float(input('Qual o valor do suco de Garrafa? '))

TotalDinheiro = 100

TotalTroco =  TotalDinheiro - ValorArroz - ValorBatataPalha - ValorSucoDeGarrafa 

print(f'Você tem R$100 reais e o valor do seu troco será de: R${TotalTroco} reais')
