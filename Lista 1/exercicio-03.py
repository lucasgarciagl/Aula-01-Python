# 3) Desenvolva uma programação que peça ao usuário para digitar o ano do seu nascimento no formato (YYYY) e o ano atual também no formato (YYYY). Em seguida mostre na tela qual a idade do usuário em anos, em meses, em dias e em semanas.

anoNascimento = int(input('Digite o ano do seu nascimento: '))
anoAtual = int(input('Digite o ano atual: '))

# print(f'A idade do usuario é: {anoAtual - anoNascimento} anos')
# print(f'A idade do usuario em meses: {(anoAtual - anoNascimento)*12} meses')
# print(f'A idade do usuario em dias: {(anoAtual - anoNascimento)*365}dias')
# print(f'A idade do usuario em semanas: {(anoAtual - anoNascimento)*52}semanas')

ano = anoAtual - anoNascimento
meses = ano * 12
dias = ano * 365
semanas = ano * 52

print(f'A idade do usuario é: {ano} anos,\n {meses} meses,\n {dias} dias,\n1995 {semanas} semanas')





