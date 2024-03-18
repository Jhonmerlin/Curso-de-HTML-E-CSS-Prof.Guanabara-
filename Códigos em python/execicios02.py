 #Escreva um programa que peça ao usuário para digitar números inteiros positivos. O
#programa deve somar esses números até que o usuário digite '0'. Quando '0' for digitado, o
#programa deve parar de pedir números e imprimir a soma total



#lista_frutas = []  # Inicializa uma lista vazia para armazenar as frutas

#while True:
   # fruta = input("Digite o nome da fruta: ")
    #lista_frutas.append(fruta)  # Adiciona a nova fruta à lista

    #escolha = input("Deseja adicionar outra fruta? (sim/não): ")
    #if escolha == "sim":
        #continue  # Retorna ao início do loop para adicionar mais frutas
    #elif escolha == "não":
        #print("Lista de frutas:", lista_frutas)
        #break  # Sai do loop
    #else:
        #print("Opção inválida. Por favor, digite 'sim' ou 'não'.")
#

lista_inteiros = []


while True:
    inteiros = int(input("Digite um número inteiro: "))
    lista_inteiros.append(inteiros)
    #print(lista_inteiros)

    escolha = inteiros
    if escolha > 0:
        continue

    else:
        print(f"Seu valor total informado foi de {sum(lista_inteiros)}")
        break

