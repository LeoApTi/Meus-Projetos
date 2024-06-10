# Lista de possíveis palavras que podem ser escolhidas
palavras = ['banana', 'uva', 'morango', 'abacate', 'melancia']

# Importando o método choice() do módulo ramdom
# Esse método escolhe uma palavra, aleatoriamente, dentro de uma dada sequência
from random import choice
palavra_escolhida = choice(palavras)

# Defindo o número de chances do jogador
chances = 6

palavra_escondida = []
letras_escolhidas = []
letras_erradas = []

# Gerando uma lista substituindo as letras da palavra_escolhida por '_'
for i in palavra_escolhida:
    palavra_escondida.append('_')
print(palavra_escondida)

# Código que faz o jogo funcionar
while chances > 0 and palavra_escondida.count('_') > 0:
    letra = str(input('Escolha uma letra: '))
    letras_escolhidas.append(letra)
    if letra in palavra_escolhida:
        for pos, i in enumerate(palavra_escolhida):
            if i == letra:
                palavra_escondida[pos] = letra
    else:
        letras_erradas.append(letra)
        chances -= 1
    print(palavra_escondida)
    print(f'Letras erradas: {letras_erradas}')
    print()

if palavra_escondida.count('_') == 0:
    print('Parabéns! Você acertou a palavra!')
else:
    print(f'Você perdeu! A palavra era {palavra_escolhida.upper()}.')