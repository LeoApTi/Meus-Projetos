# Lista para armazenar os itens
itens = []

# Solicitar ao usuário os itens possuídos
for item in range(3):
  itens.append(str(input()))
  
# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item.capitalize()}")
