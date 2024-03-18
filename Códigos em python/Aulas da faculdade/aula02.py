#Anotações importantes! input() sempre devolve uma str!

exemplo = input("Digite um número!")
print(type(exemplo)) # independente do que for digitado,sem um conversor como int,float,bool,str(padrão) o comando input() gera uma str!

# Podemos separar um dado utilizando o comando sep='como será separado'
print("B","N","N","." , sep='A' , end="\n")
print("16","03","2024", sep="/" , end="\n")
print("","16,50 ","20,20 "," 40,00", sep="R$", end="\n")

#Comando print sempre fecha o comando com o \n para quebrar a linha, o comando end="" é possível modificar o final, ou até mesmo juntar prints!

print("Hoje é um bom dia", end=" ")
print("para beber!")

# Comando != diferente ajuda a avaliar a inserção de códigos pelo if
exemplo1 = input("Hoje lá na casa do seu zé?")

if exemplo1 != "Vai rolar putaria":
    print("Errado meu chapa!")
else:
    print("Satisfação aspira!")



