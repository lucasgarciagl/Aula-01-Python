# 6) Criar um programa que calcule o IMC, no qual o usuário deve digitar o seu peso e altura, realizar o cálculo (peso / altura * altura) e mostrar o resultado na tela.


peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

print(f'Seu IMC é: {peso / (altura * altura)}')