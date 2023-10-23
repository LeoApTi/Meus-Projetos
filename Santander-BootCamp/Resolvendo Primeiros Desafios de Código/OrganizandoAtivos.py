ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input('Quantos ativos? '))

# Entrada dos códigos dos ativos
for ativo in range(0,quantidadeAtivos):
    codigoAtivo = input('Ativo: ').strip()
    ativos.append(codigoAtivo)

# Ordenar os ativos em ordem alfabética.
ativos.sort()

# Imprimir a lista de ativos ordenada.
for n in ativos:
    print(n)
