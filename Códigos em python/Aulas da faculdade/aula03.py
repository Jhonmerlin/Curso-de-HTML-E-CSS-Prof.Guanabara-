#EX 02 Login simples
# Faça um programa que simula um login simples. O usuário deve digitar "admin"
#como nome de usuário e "senha123" como senha. O programa deve #continuar
#pedindo essas informações até que sejam inseridas corretamente. #Após a
#inserção correta, o programa deve imprimir "Login realizado com #sucesso!"


contador = 0

while contador <= 3:
    usuario = input("Olá, digite o seu usuario: ")
    senha = input("Digite a sua senha: ")
    if usuario == "admin" and senha == "senha123":
        print(f"Login feito com sucesso, seja bem vindo {usuario}")
        break
    if contador >= 3:
        print("Login bloqueado, por favor tente mais tarde!")
        break
    if usuario != "admin" and senha != "senha123":
        print("Você digitou errado tente novamente")
        contador += 1
        continue