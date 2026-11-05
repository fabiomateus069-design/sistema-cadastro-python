def new_func():
    print('por favor digite um número inteiro.')


while True:
    try:
        numero = int(input('Digite um numero inteiro:'))

        print(f'Parabens! você digitou um numero inteiro: {numero}')
        break

    except ValueError:
        print('Erro! O número digitado não é inteiro, ', end='')
        print('por favor digite um numero inteiro.')