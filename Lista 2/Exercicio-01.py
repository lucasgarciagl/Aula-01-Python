# 1) Você é um amante da natureza e adora fazer trilhas. Criar um programa que calcule a velocidade média das trilhas que você realiza. Para isso, devem ser digitados os dados de distância percorrida (quilômetros) e tempo que a trilha durou (horas). Fazer então o cálculo da velocidade média e mostrar na tela a mensagem "Sua média de velocidade durante essa trilha foi de X km/h", sendo X a velocidade. 


DistanciaPercorrida = int(input('Digite a distância percorrida na trilha: ')) 
TempoDeTrilha = int(input('Digite o tempo que durou a trilha: ')) 

VelocidadeMedia = (DistanciaPercorrida / TempoDeTrilha)

print(f'Sua média de velocidade durante essa trilha foi de {VelocidadeMedia} km/h"')