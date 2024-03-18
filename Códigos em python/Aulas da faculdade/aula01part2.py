import datetime
#Elabore um algoritmo em Python que verifica a idade de uma pessoa para determinar se ela é elegível para votar e, adicionalmente, se ela está na faixaetária que permite a candidatura a um cargo político.
idade_usuario = int(input("Olá em que ano você nasceu?"))
ANO_BASE=2024
calculo = ANO_BASE - idade_usuario
print(f"Você possui no dia de hoje {calculo} anos.")
#Verifica o ano do usuario usando o ano base como referência

#Verifica a idade e se e possível a eleição ou não a presidencia!
if calculo >= 16 and calculo < 18:
    print("Você pode votar caso deseje!")
if calculo >=18 and calculo < 16:
    print("Você é obrigado(a) a votar!")
if calculo < 16:
    print("Você não pode votar!")
if calculo >= 35:
    print("Você é obrigado a votar e pode se canditar a presidencia!")
if calculo != int:
    print("É pra digitar número consagrado!")