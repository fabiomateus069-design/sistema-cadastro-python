def validar_senha(senha: str) -> bool:
    if len(senha) < 10:
        return False

    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)

    return tem_maiuscula and tem_numero


senha_digitada = input(
    'Digite uma senha (com mínimo 10 caracteres, uma letra maiúscula '
    'e um número): '
)

if validar_senha(senha_digitada):
    print('A senha digitada é válida!')
else:
    print(
        'Senha inválida!, por favor, insira uma senha '\
        'com no mínimo 10 caracteres, contendo pelo menos uma'\
        'letra maiúscula e um número.'
    )