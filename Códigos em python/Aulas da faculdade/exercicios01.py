# 1 - Esta é uma continuação do exercício 3 visto em aula. Desta vez, você deve modificar o
# programa de login para que ele permita apenas um número limitado de tentativas de
# acesso. Defina um número máximo de tentativas e utilize um loop for (ao invés de while)
# para pedir ao usuário seu nome e senha. Se o usuário não conseguir fazer login após o
# número máximo de tentativas, o programa deve imprimir uma mensagem indicando que o
# acesso foi bloqueado.


#usuario_login = input("Digite seu usuário:") #<<<< Login
#senha_login = input("Digite a sua senha: ")  #<<<< SENHA DO USUARIO
 
contador = 0 #CONTADOR PARA TRAVAR O LOPING

#variavel_teste = input("Digite Bolo: ")

##for contador in range(3):
    
    #if usuario_login == "Admin" and senha_login == "senha123":
       # print(f"Login bem sucedido! seja bem vindo {usuario_login}")
       # break

    #if usuario_login != "Admin" and senha_login != "senha123":
        #contador += 1
        #continue

    #elif contador > 3 :
       # print("Limite de erros alcançado, tente novamente mais tarde")
        #break
        
for contador in range(3):
    usuario_login = input("Digite o nome de usuário: ")
    senha_login = input("Digite a senha: ")
    print(contador)

    if usuario_login == "Admin" and senha_login == "senha123":
        print(f"Login bem sucedido! Seja bem vindo, {usuario_login}")
        break
    
    else:
        if contador < 2:
            print("Usuário ou senha incorretos. Tente novamente.")
        else:
            print("Limite de tentativas excedido. Tente novamente mais tarde.")



