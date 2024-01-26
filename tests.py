# import random

# # Inicializa a string vazia
# numero = ''

# # Loop para escolher 9 dígitos
# for i in range(9):
#     escolha = random.choice('0123456789')

#     # Adiciona o dígito escolhido à string
#     numero += escolha

# # Imprime a string resultante de 9 dígitos
# print(f'({numero[:2]}){numero[2:5]}-{numero[5:]}')



nome = input('Digite o seu nome: ')

with open('dados.txt', 'w') as arquivo:
  arquivo.write(nome)


with open('dados.txt', 'r') as dado:
  dado_lido = dado.read()
  print(dado_lido)