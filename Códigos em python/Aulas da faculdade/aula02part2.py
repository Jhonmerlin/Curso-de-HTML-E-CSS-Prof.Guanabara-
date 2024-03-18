#Sobre listas

lista = ["Banana","Uva","Pera","Abacate",["Pizza","Sorvete"]] # É POSSIVEL MESCLAR QUALQUER TIPO DE DADO DENTRO DE UMA LISTA, INCLUSIVE OUTRA LISTA!
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1]) #<<< A lista permite a flexibilidade de usar valores negativos como -1 para buscar o último item da lista, que no caso é o abacate

#ADICIONAR NOVOS VALORES A LISTA

lista.append("Abacaxi")#<<<<< Adiciona o novo item no final da lista, não é necessário passar o indice
print(lista)
lista.insert(2,"Tangerina") #<<<< Adiciona o item ao local designado sendo então variavel.inser(lugar,"Oque será adicionado aqui")
print(lista)

#REMOVENDO ITENS DA LISTA
lista.remove("Abacate") #Faz uma busca na lista e remove o que for compátivel com o valor passado
print(lista)
lista.pop(0)# Parecido com o insert, ele remove apenas onde o indice foi informado no caso a banana= [0]
print(lista)