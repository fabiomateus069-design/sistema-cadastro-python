def modulo1_senha(senha):
    # 1. Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False

    # 2. Verifica se tem pelo menos uma letra maiúscula
    # 3. Verifica se tem pelo menos um número
    tem_maiuscula = False
    tem_numero = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        if caractere.isdigit():
            tem_numero = True

    if not tem_maiuscula or not tem_numero:
        return False

    return True


# ___Teste do programa___
senha_digitada = input(
    'Digite uma senha (com mínimo 8 caracteres, uma letra maiúscula '
    'e um número): '
)
if modulo1_senha(senha_digitada):
    print('senha valida!')

else:
    print(
        'senha invalida!'
        ' A senha deve ter no mínimo 8 caracteres, '
        'uma letra maiúscula e um número.'
        )