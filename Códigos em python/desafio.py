# Criando uma entrada de Input, print 
comando_entrada = input("Olá, qual seu nome?")
print(f'Uma curiosidade sobre seu nome {comando_entrada}')
hexadecimal= bin(ord(comando_entrada[0]))
binario = hex(ord(comando_entrada[0]))
decimal = ord(comando_entrada[0])
print(f"A sua primeira letra {comando_entrada[0]} corresponde a \n {decimal} em decimal , \n {hexadecimal} em Hexadecimal \n {binario} em binario")
print("\t Dia 11")