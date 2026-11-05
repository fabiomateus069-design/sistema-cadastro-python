# 1. Entrada de dados para receber o cadastro
print('\n===== SISTEMA DE CADASTRO INDIVIDUAL =====')
id = 104
nome = input('Informe o seu nome:')
idade = int(input('Informe a sua idade:'))
telefone = str(input('Informe o seu telefone:'))
saldo = float(input('Me informe seu saldo:'))

# 2. armazenamento de dados
cliente = {
    "id": {104},
    "nome": {nome},
    "idade": {idade},
    "telefone": {telefone},
    "saldo": {saldo}
}

# 3. Saida de dados
print('\n=====USUARIO CADASTRADO=====')
print(f'cliente: {cliente}')