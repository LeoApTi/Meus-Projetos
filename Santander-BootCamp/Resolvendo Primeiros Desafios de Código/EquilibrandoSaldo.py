saldo_atual = float(input('Digite o saldo atual: '))
valor_deposito = float(input('Digite o valor para depósito: '))
valor_retirada = float(input('Digite o valor para retirada: '))

# Calcular o saldo atualizado de acordo com a descrição deste desafio.
def saldo_atualizado(saldo_atual, valor_deposito, valor_retirada):
  if valor_retirada > (saldo_atual + valor_deposito):
    print(f'Saldo insuficiente! Você tem {saldo_atual+valor_deposito} de saldo na conta.')
  else:
    valor_atualizado = saldo_atual + valor_deposito - valor_retirada
    print(f'Saldo atualizado na conta: {valor_atualizado:.1f}')


# Imprimir a saída (uma casa decimal).
saldo_atualizado(saldo_atual, valor_deposito, valor_retirada)
