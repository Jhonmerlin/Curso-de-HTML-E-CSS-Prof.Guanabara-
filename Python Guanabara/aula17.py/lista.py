#Listas difrentes das tuplas aceitam modificação
guloseima = ['Bolo','salgadinho','sorvete']
print(guloseima[0])
print(guloseima[1])
print(guloseima[2])
guloseima[2] = 'Mariola' #Aqui veja que o sorvete que está no index 2 foi subistituido pela mariola
print(guloseima)
guloseima.append('Pé de moleque')#<<<<< Adiciona um elemento no final da lista
print(guloseima)
guloseima.insert(0,'Cocada') #<<<<< Adiciona um item em um local determinado da lista
print(guloseima)
del guloseima[3] #Tanto o pop quanto remove, tiram itens de um determinado index desejado e indicado
guloseima.pop(2) #
guloseima.remove('Bolo') #<<<<<< Aqui a remoção é feita pelo o contéudo que está na lista, ele reorganiza os indices que estão na lista
print(len(guloseima))  #<<<<, Verifica quantos valores tem na lista
valores = list(range(4,11)) # Criando Uma lista com o metodo for 
print(valores)
valores.sort()
print(valores)