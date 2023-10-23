import pandas as pd
import requests
import json
import random

# EXTRAIR OS IDS DOS USUÁRIOS NA PLANILHA LOCAL
df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

# RETORNA O JSON DO USUÁRIO SE ELE EXISTIR, CASO CONTRÁRIO NÃO RETORNA NADA
def get_user(id):
    response = requests.get(f'https://sdw-2023-prd.up.railway.app/users/{id}')
    return response.json() if response.status_code == 200 else None
users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

# OBTER UMA FRASE ALEATÓRIA DE UM ARQUIVO LOCAL CONTENDO VÁRIAS FRASES E ADICIONÁ-LA EM SUA DESCRIÇÃO
df = pd.read_csv('Frases.csv')
frases = df['Frases'].tolist()
for user in users:
    numFrase = random.randint(0, 8)
    news = frases[numFrase]
    user['news'].append({"icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news})

# VERIFICAR SE OS USUÁRIOS EXISTEM
def update_user(user):
    response = requests.put(f'https://sdw-2023-prd.up.railway.app/users/{user["id"]})', json=user)
    return True if response.status_code == 200 else False


# VERIFICAR SE O ARQUIVO FOI MODIFICADO COMO SOLITICADO
for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}!")
