#insere a string
texto = input("Informe uma palavra")

#insere os arrays que irão armazenar as letras e a quantidade de repetições
guardarLetra = []
quantidadeRepeticoes = []

#captura a letra e a quantidade de repetições
for letra in texto:
    quantidadeRepeticoes.append(texto.count(letra))
    guardarLetra.append(letra)

#encontra a maior quantidade de repetições armazenada no array
maiorQuantidadeRepeticoes = max(quantidadeRepeticoes)

#encontra o indice da maior quantidade de repeticoes
indiceMaximo = quantidadeRepeticoes.index(maiorQuantidadeRepeticoes)

#com este indice, encontrar a letra correspondente que está armazenada em outro vetor
letraMaisRepete = guardarLetra[indiceMaximo]

#imprimi a letra que mais se repete na string e a quantidade de repeticoes
print(letraMaisRepete , " : ", maiorQuantidadeRepeticoes)

