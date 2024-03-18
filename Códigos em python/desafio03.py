import random

jogadas = ['Pedra', 'Papel','Tesoura']

def jogar (ultima_jogada =None):
    if ultima_jogada is None:
        return random.choice(jogadas)
    indice = jogadas.index(ultima_jogada+1)
    resultado= ultima_jogada + indice
    return indice , resultado

print(jogar())