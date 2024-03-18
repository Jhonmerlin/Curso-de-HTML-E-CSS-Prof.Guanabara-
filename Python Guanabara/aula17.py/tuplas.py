#Tuplas são imutáveis!

nome=('Carlos', 'Ricardo', 'Toninho')
print(nome[0])
print(nome[1])
print(nome[2])
#nome[3]='Roberto' #<<<< Tuplas não aceitam adicionar novos itens
#print(nome[3]) #<<<<<<<< Não FUNCIONA!
nome[2]='Jovenir' #<<<< Também não aceita que novos itens assumam lugares de outros
