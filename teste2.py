import json

print("=== CADASTRO DE USÚARIO COM PERCISTÊNCIA JSON===")

# 1. Coleta de dados 
nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
telefone = input("Digite o seu telefone: ")
cidade = input("Digite a sua cidade: ")

# 2. Estrutura em dicionário
usuario = {
    "nome": nome,
    "idade": idade,
    "telefone": telefone,
    "cidade": cidade 
}

# 3. Salvado no arquivo JSON
with open("usuaario.json", "w", encoding="utf_8") as arquivo:
    json.dump(usuario, arquivo, indent=4, ensure_ascii=False)

print("\n--------------------------------------------")
print("Cadastro realizado com sucesso!")
print("Os dados foram gravados no arquivo 'usuario.json'.")