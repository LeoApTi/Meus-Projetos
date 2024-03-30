valor = float(input())

if valor > 0:
    #Imprime a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
    print('Deposito realizado com sucesso!')
    print(f'Saldo atual: R$ {valor:.2f}')
elif valor == 0:
    #Imprime a mensagem de encerrar o programa.
    print('Encerrando o programa...')
else:
    #Imprime a mensagem de valor inválido.
    print('Valor invalido! Digite um valor maior que zero.')
