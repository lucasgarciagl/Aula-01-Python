# 5) Uma cidade pretende apurar os votos de sua eleição. Faça um programa para ler o número total de eleitores. Em seguida o número de votos do candidato X, o número de votos do candidato Y, total de votos brancos e total de votos nulos (a soma desses quatro, deve ser igual ao total de eleitores). Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.


totalEleitores = int(input('Qual o total de Eleitores? '))
totalVotoX = int(input('Qual o total de votos do candidato X? '))
totalVotoY = int(input('Qual o total de votos do candidato Y? '))
totalVotoBranco = int(input('Qual o total de votos Brancos? '))
totalVotoNulo = int(input('Qual o total de votos Nulos? '))

# print(f'O total de eleitores é: {totalEleitores}')
# print(f'O percentual de Votos do candidato X é: {(totalVotoX * 100) / totalEleitores} %')
# print(f'O percentual de Votos do candidato Y é: {(totalVotoY * 100) / totalEleitores} %')
# print(f'O percentual de Votos em Branco é: {(totalVotoBranco * 100) / totalEleitores} %')
# print(f'O percentual de Votos Nulos é: {(totalVotoNulo * 100) / totalEleitores} %')



#Correção

percentualCandidatoX = (totalVotoX * 100) / totalEleitores
percentualCandidatoY = (totalVotoY * 100) / totalEleitores
percentualVotosEmBranco = (totalVotoBranco * 100) / totalEleitores
percentualVotosNulos = (totalVotoNulo * 100) / totalEleitores

print(f'O total de eleitores é: {totalEleitores} \n\npercentual de votos do candidato X é {percentualCandidatoX}% \npercentual de votos do candidato Y é {percentualCandidatoY}% \npercentual de votos em Branco é {percentualVotosEmBranco}%\npercentual de votos Nulos é {percentualVotosNulos}% ')