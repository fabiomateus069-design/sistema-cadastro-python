import json

print("=== LENDO DADOS DO ARQUIVO JSON ===")

try:
    # 1. tenta abrir o aquivo JSON existente
    with open("usuaario.json", "r", encoding="utf-8") as arquivo:
        dados_carregados = json.load(arquivo)

    print("\n Usuário encontrado no arquivo!")
    print(f"Nome: {dados_carregados['nome']}")
    print(f"Idade: {dados_carregados['idade']}")
    print(f"Telefone: {dados_carregados['telefone']}")
    print(f"Cidade: {dados_carregados['cidade']}")

except FileNotFoundError:
    print("\n O arquivo 'usuario.json' ainda não existe!") 