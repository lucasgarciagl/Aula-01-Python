# 5) Uma feira de livros está fazendo promoção onde na compra de 3 livros, o(a) comprador(a) ganha 15% de desconto. Criar um programa que receba os valores dos 3 livros e mostra na tela o total dos livros sem desconto e com desconto.


valorLivro1 = float(input('Informe o valor do livro 1: '))
valorLivro2 = float(input('Informe o valor do livro 2: '))
valorLivro3 = float(input('Informe o valor do livro 3: '))

totalLivros = valorLivro1 + valorLivro2 + valorLivro3
desconto = 0.15 * totalLivros


print(f'>>>Valores livros com desconto<<<\n O valor Total dos livros com desconto é: {desconto}\n\n>>>Valores livros sem desconto<<<\nO valor total dos livros sem desconto é:{totalLivros}' )