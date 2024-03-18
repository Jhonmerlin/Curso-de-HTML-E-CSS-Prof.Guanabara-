#Exercicio 5 - Calculando a área de um triangulo

largura = float(input("Digite a largura do seu triangulo: "))
altura = float(input("Digite a altura do seu triangulo: "))

area = (largura * altura)
perimetro = (2*(largura+altura))

print(f"Com os valores fornecidos da largura:{largura} e de altura:{altura}, temos os valores de")
print(f"Area = {area} e Perimetro {perimetro}")
