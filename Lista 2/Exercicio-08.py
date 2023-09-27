# 8) Os leões baios são animais territoriais. Seu território compreende cerca de 320km² por indivíduo, exceto quando formam casais, nesse caso o casal costuma dominar uma área de 400km², juntos. Considerando que existam 9 fêmeas e 5 machos em determinada reserva ambiental. Elaborar um programa no qual você deve digitar quantos casais (dados de pesquisa de campo) existem dentre esse total e mostrar na tela a soma geral de área dominada, incluindo todos indivíduos.

#3200 por leao
#4000 por casal
#9 femeas + 5 machos


casalLeao = int(input('Informe com base na pesquisa de campo, quantos casais de leões existem na reserva: '))

areaLeaoIndividual = 3200
areaLeaoCasal = 4000

areaOcupadaCasal = casalLeao * areaLeaoCasal
restanteIndividuos = 14 - (casalLeao * 2)
restanteArea = restanteIndividuos *  areaLeaoIndividual

totalAreaAmbiental = (casalLeao * areaLeaoCasal) + restanteArea

print(f'A soma da área dominada é: {totalAreaAmbiental}km²')