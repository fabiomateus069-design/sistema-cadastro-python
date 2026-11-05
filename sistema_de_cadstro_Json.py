import json

print('===== CADATROS DE USUARIOS COM PESISTENCIA (JSON) =====')

NOME_DO_ARQUIVO = 'armazem_de_usuarios.json'

# 1. Armazenar os dados de usuarios cadastrados em uma lista
try:
    with open(NOME_DO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        lista_de_usuarios = json.load(arquivo)
        print(
            f"\n Foram carregados {len(lista_de_usuarios)} usuario(s) "
            "do arquivo."
        )
except FileNotFoundError:
    lista_de_usuarios = []
    print('\n Nenhum arquivo foi encontrado, uma nova lista foi criada!')

    # 2 Entrada de dados do usuario
    nome = input('\nInforme seu nome: ')
    idade = int(input('informe a sua idade: '))
    cidade = input('Infome a sua cidade: ')
    telefone = input('Informe o seu telefone pessoal: ')
    gmail = input('Infomer seu email valido:')

    # 3. armazenamento de dados em dicionario
    usuario = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade,
        'telefone': telefone,
        'gmail': gmail
    }

    # 4. Adicionar o novo registro a lista vazia
    adicionar_usuario = input(
        '\n Deseja cadastrar um novo usuario? (S/N):'
    ).upper()

    if adicionar_usuario == 'S':
        lista_de_usuarios.append(usuario)
        while True:
            nome = input('Informe seu nome: ')
            idade = int(input('informe a sua idade: '))
            cidade = input('Infome a sua cidade: ')
            telefone = input('Informe o seu telefone pessoal: ')
            gmail = input('Infomer seu email valido:')

            usuario = {
                'nome': nome,
                'idade': idade,
                'cidade': cidade,
                'telefone': telefone,
                'gmail': gmail
            }

            lista_de_usuarios.append(usuario)

            encerrar_cadastro = input(
                '\n Deseja cadastrar um novo usuario? (S/N):'
            ).upper()
            if encerrar_cadastro == 'N':
                break
    else:
        lista_de_usuarios.append(usuario)

    # 5. Salvar a lista completa atualizada no arquivo JSON
    with open(NOME_DO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_de_usuarios, arquivo, indent=4, ensure_ascii=False)

        # 5. Saida de dados salvos no arquivo JSON
        print('\n===== USUARIO CADASTRADO COM SUCESSO =====')
        for i, usuario in enumerate(lista_de_usuarios, 1):
            print(
                f"{i}. {usuario['nome']} - {usuario['cidade']} "
                f"({usuario['idade']} anos) - "
                f"{usuario['telefone']} - {usuario['gmail']}"
            )
        print(f'Usuario: {usuario}')

        

        
