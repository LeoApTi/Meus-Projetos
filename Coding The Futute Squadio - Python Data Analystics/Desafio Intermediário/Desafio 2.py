ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input(' '))

# Entrada dos códigos dos ativos
for ativo in range(0,quantidadeAtivos):
    codigoAtivo = input(' ').strip()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for n in ativos:
    print(n)
