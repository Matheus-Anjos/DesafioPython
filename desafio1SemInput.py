#cria a lista com os números

lista = [1,2,3,4]

#declara ad variaveis do menor número possível e menor número da lista para comparação
menor_numero_possivel = 0
indice_menor_numero = 0
menor_numero_lista = lista[0]

#declara os incrementos que serão utilizados nos loops
i = 0
j = 0

#encontra o menor número da lista e seu índice
for i in range(len(lista)) :
    if ( lista[i] < menor_numero_lista) :
        menor_numero_lista = lista[i]
        indice_menor_numero = i

#caso o menor número não tenha um sucessor, este será o menor número da lista
if not (lista[indice_menor_numero] + 1) in lista :
            menor_numero_possivel = lista[indice_menor_numero] + 1

#caso o menor número tenha um sucessor, verificar se próximos que o sucedem tem um sucessor, caso não tenha, este será o menor número possível da lista de inteiros que não pertence a lista
else :
   for j in range(len(lista)) :
       if (lista[indice_menor_numero] + j) in lista and not (lista[indice_menor_numero] + j+1) in lista :
        menor_numero_possivel = lista[indice_menor_numero] + j+1 
        break

#imprimi os valores
print("o menor número inteiro possível que não pertence a lista é " , menor_numero_possivel)