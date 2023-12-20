import random

# Função para gerar um nome aleatóri
def gerar_nome():
    nomes = ['Alice', 'Bob', 'Carol', 'David', 'Eve']
    return random.choice(nomes)

# Função para gerar um e-mail aleatório
def gerar_email():
    dominios = ['gmail.com', 'yahoo.com', 'hotmail.com']
    nome = gerar_nome().lower()
    dominio = random.choice(dominios)
    return f'{nome}@{dominio}'

# Função para gerar um número de telefone aleatório
def gerar_telefone():
    numero = ''.join(random.choice('0123456789') for _ in range(9))
    return f'({numero[:2]}) {numero[2:5]}-{numero[5:]}'

# Função para gerar o nome de uma cidade aleatória
def gerar_cidade():
    cidades = ['Cidade A', 'Cidade B', 'Cidade C', 'Cidade D', 'Cidade E']
    return random.choice(cidades)

# Função para gerar o nome de um estado aleatório
def gerar_estado():
    estados = ['Estado A', 'Estado B', 'Estado C', 'Estado D', 'Estado E']
    return random.choice(estados)

# Função para salvar os dados em um arquivo
def salvar_dados(dados):
    with open('dados.txt', 'a') as arquivo:
        for dado in dados:
            arquivo.write(f'{dado}\n')

# Função para exibir as opções de dados a serem gerados
def exibir_opcoes():
    print('Escolha uma ou mais opções de dados a serem gerados:')
    print('1. Gerar nome')
    print('2. Gerar e-mail')
    print('3. Gerar telefone')
    print('4. Gerar cidade')
    print('5. Gerar estado')
    print('Digite "parar" para finalizar o programa.')

# Função principal
def main():
    opcoes = {
        1: gerar_nome,
        2: gerar_email,
         3: gerar_telefone,
        4: gerar_cidade,
        5: gerar_estado
    }
    dados_gerados = []
    continuar = True

    while continuar:
        exibir_opcoes()
        escolha = input('Escolha uma opção: ')

        if escolha.isdigit() and int(escolha) in opcoes:
            opcao = opcoes[int(escolha)]
            dado = opcao()
            dados_gerados.append(dado)
            print(f'Dado gerado: {dado}')
        elif escolha.lower() == 'parar':
            continuar = False
        else:
            print('Opção inválida. Tente novamente.')

    salvar_arquivo = input('Deseja salvar os dados em um arquivo? (s/n): ')
    if salvar_arquivo.lower() == 's':
        salvar_dados(dados_gerados)

    print('Dados gerados:')
    for dado in dados_gerados:
        if 'telefone' not in dado and 'cidade' not in dado and 'estado' not in dado:
            print(dado)

if __name__ == '__main__':
    main()
