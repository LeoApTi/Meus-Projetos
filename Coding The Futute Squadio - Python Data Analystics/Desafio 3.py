capacidade_atual, aumento_percentual = map(int, input().split())

# Calculo da nova capacidade do disco de Mithril
nova_capacidade = capacidade_atual + (capacidade_atual * (aumento_percentual / 100))

# Impressão da nova capacidade
print(int(nova_capacidade))
