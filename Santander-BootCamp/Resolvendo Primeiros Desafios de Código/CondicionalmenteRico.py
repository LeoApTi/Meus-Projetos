# Entrada de dados
saldo_total = int(input('Digite seu saldo: '))
valor_saque = int(input('Digite o valor de saque: '))

# Criar as condições necessárias para impressão da saída.
if saldo_total >= valor_saque:
    novo_saldo = saldo_total - valor_saque
    print(f'Saque realizado com sucesso. Novo saldo: {novo_saldo}')
else:
    print(f'Saldo insuficiente. Saque não realizado!')
