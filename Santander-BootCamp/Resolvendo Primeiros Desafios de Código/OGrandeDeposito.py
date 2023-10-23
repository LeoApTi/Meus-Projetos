valor = float(input('Valor para depósito: '))

while valor < 0:
    # Imprimir a mensagem de valor inválido.
    print('Valor inválido! Digite um valor maior que zero.')
    valor = float(input('Valor para depósito: '))
if valor > 0:
    # Imprimir a mensagem de sucesso, formatando o saldo atual.
    print('Deposito realizado com sucesso!')
    print(f'Saldo atual: R$ {valor:.2f}')
elif valor == 0:
    # Imprime a mensagem de encerrar o programa.
    print('Encerrando o programa...')
