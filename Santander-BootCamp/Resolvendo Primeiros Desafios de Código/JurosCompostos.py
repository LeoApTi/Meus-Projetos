valor_inicial = float(input('Capital: '))
taxa_juros = float(input('Taxa de Juros: [Divida o valor inteiro por 100 ex.: 5% = 0.05] '))
periodo = int(input('Período em anos: '))

# Iterar, baseado no período em anos, para calculo do valorFinal com os juros.
valor_final = valor_inicial * (1 + taxa_juros) ** (periodo)

print(f"Valor final do investimento: R$ {valor_final:.2f}")
