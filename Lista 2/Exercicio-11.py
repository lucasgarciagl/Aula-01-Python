# 11) As baleias da Groenlândia estão entre os animais que vivem mais tempo na Terra, em média 200 anos. A reprodução se dá a cada 4 anos, tendo somente 1 filhote por vez. Programar um sistema que calcule o total de filhotes ao longo da vida e a média de filhotes de uma baleia dessa espécie por década.


vidaBaleia = 200
reproducao = 4
filhote = 1
decada = 10

totalFilhotes = vidaBaleia / reproducao

mediaFilhotes = totalFilhotes / decada

print(f'O total de filhotes de baleias da Groenlândia ao longo da vida são, {totalFilhotes} filhotes e a média de filhotes por década é {mediaFilhotes} filhotes.')