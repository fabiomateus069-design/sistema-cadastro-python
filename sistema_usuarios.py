import json

print("=== SISTEMA DE CADASTRO MUTIPLOS (JSOM) ===")

NOME_ARQUIVO = "cadastro_mult.json"

# 1. Carregar lista existente ou criar uma lista vazia
try:
    with open(NOME_ARQUIVO, "r", encoding="utf_8") as arquivo:
        lista_usuario = json.load(arquivo)
    print(f"\n Foram carregados {len(lista_usuario)} usuario(s) do arquivo.")
except FileNotFoundError:
    lista_usuario = []
    print("\n Nenhum arquivo encontrado. Uma nova lista foi iniciada.")

# 2. Coleta de dados do novo usuario
nome = input("\nDigite seu nome: ")
idade = int(input("digite sua idade: "))
telefone = input("Digite o seu telefone: ")
cidade = input("Digite a sua cidade: ")
email = input("Digite o seu Email: ")

# 3. Estrutura em dicionario
novo_usuario = {
    "nome": nome,
    "idade": idade,
    "telefone": telefone,
    "cidade": cidade,
    "email": email
}
# 4. Adiciona o novo registro á lista existente
lista_usuario.append(novo_usuario)

# 5. Salva a lista completa atualizada no arquivo JSON
with open(NOME_ARQUIVO, "w", encoding="utf_8") as arquivo:
    json.dump(lista_usuario, arquivo, indent=4, ensure_ascii=False)

print("\n Usuario cadastrado com sucesso!!")

# 6. Exibir todos cadastros no terminal
print("\n=== LISTA ATUALIZADA DE USUÁRIO ===")
for i, usuario in enumerate(lista_usuario, 1):
    print(
        f"{i}. {usuario['nome']} - {usuario['cidade']} "
        f"({usuario['idade']} anos)"
    )