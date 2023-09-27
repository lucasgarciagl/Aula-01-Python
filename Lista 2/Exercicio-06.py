# 6) Criar um programa que realize o cálculo de uma média da faculdade. A média é composta por três notas: Atividade Individual (peso 1), Seminário em Equipe (peso 1), Projeto final (peso 3). O usuário deve digitar as três notas e a média deve ser mostrada na tela.


atividadeIndividual = float(input('Informe a nota da Atividade Individual: '))
seminarioEquipe = float(input('Informe a nota do Seminário em Equipe: '))
projetoFinal = float(input('Informe a nota do Projeto Final: '))

mediaFinal = (atividadeIndividual + seminarioEquipe + projetoFinal) / 3

print(f'A sua média final é: {mediaFinal}')