#Exericicio 3 - Somando elementos de uma lista

valor_1 = float(input("Digite o primeiro valor"))
valor_2 = float(input("Digite o segundo valor"))
valor_3 = float(input("Digite o terceiro valor"))

lista = [valor_1,valor_2,valor_3]

print(lista)

soma= lista[0]+ lista[1] + lista [2] #O segredo aqui é somar pelo indice que os valores estão distribuidos
print(f"O valor da soma da lista foi de  {soma}")