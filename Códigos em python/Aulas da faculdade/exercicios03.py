#3- Faça um programa que imprima uma tabela de multiplicação para números de 1 a 5. O
#programa deve usar loops for aninhados para calcular e imprimir a tabela de
#multiplicação.

for multiplicador in range (1,6):
    print(f"=====Tabuada do {multiplicador}=====")
    for numero in range(1,11):
        resultado = multiplicador *numero
        print(f"{multiplicador} X {numero} = {resultado}")
    print()