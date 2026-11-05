soma_total = 0

print('\n===== SOMADOR AUTOMÁTICO =====')
print('Digite um número que deseja somar. Digite 0 para encerrar.\n')

while True:
    try:
        numero = float(input('Digite um número: (Precione 0 para encerrar)'))

        # 2. condição de saida do loop
        if numero == 0:
            break

        soma_total += numero
        print(f'Subtotal atual: {soma_total}')

    except ValueError:
        print('Erro! porfavor digite apenas números validos')

print('\n-------------------------------------------------')
print(f'Progama encerrado. Soma total final: {soma_total} ')
print('-------------------------------------------------')