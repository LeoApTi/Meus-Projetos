# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
from random import choice
from os import system, name
from unidecode import unidecode

# Board (tabuleiro)
board = ['''
+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

board.reverse()

def limpa_tela():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

# Classe
class Hangman:

  # Método Construtor
    def __init__(self, palavra):
        self.chances = 6
        self.palavra_escolhida = palavra[0]
        self.palavra_escondida = []
        self.letras_escolhidas = []
        self.letras_erradas = []
        self.remove_caracter_especial()
        print(f'Tema: {palavra[1]}')
        
  # Método para remover caracteres especiais
    def remove_caracter_especial(self):
        for i in self.palavra_escolhida:
            if i != '-' and i != ' ':
                self.palavra_escondida.append('_')
            else:
                self.palavra_escondida.append(i)

  # Método para adivinhar a letra
    def advinhar(self, letra):
        letra = letra.lower()
        if letra.isalpha() == False:
            print('\n\033[93mCaractér inválido! Digite uma letra do alfabeto(A-Z)!\033[0m')
        elif letra in self.letras_escolhidas:
            print('\n\033[93mVocê já tentou essa letra! Tente outra.\033[0m\n')
        else:
            self.letras_escolhidas.append(letra)
            if letra in self.palavra_escolhida:
                for pos, i in enumerate(self.palavra_escolhida):
                    if i == letra:
                        self.palavra_escondida[pos] = letra
            else:
                self.letras_erradas.append(letra)
                self.chances -= 1

  # Método para verificar se o jogo terminou
    def terminou(self):
        return self.palavra_escondida.count('_') == 0 or self.chances == 0

  # Método para verificar se o jogador venceu
    def verificar_win(self):
        if self.palavra_escondida.count('_') == 0:
            print('\033[92mParabéns! Você acertou a palavra!\033[0m')
        else:
            print('\033[91mVocê perdeu!\033[0m')
            print(f'A palavra era {self.palavra_escolhida.upper()}')
        print()
            
  # Método para não mostrar a letra no board
    def letra_board(self):
        print(' '.join(self.palavra_escondida))
        print(f'\nLetras erradas: {" ".join(self.letras_erradas)}')
        print(f'Letras escolhidas: {" ".join(self.letras_escolhidas)}\n')
        
        
  # Método para checar o status do game e imprimir o board na tela
    def status(self):
        print(board[self.chances])
       

def rand_palavra():
    palavras = {
  'Cor':["vermelho", "laranja", "amarelo", "verde", "azul", 
           "índigo", "violeta", "roxo", "rosa", "branco", 
           "preto", "cinza", "prata", "dourado", "marrom", 
           "bege", "turquesa", "aqua", "teal", "azul marinho", 
           "lavanda", "magenta", "coral", "ouro", "verde limão", 
           "lima", "salmão", "âmbar", "azul celeste", "bordô", 
           "caramelo", "chocolate", "ciano", "creme", "âmbar", 
           "grafite", "índigo", "magenta", "malva", "ocre", 
           "ocre", "púrpura", "safira", "topázio", "vanilla", 
           "verde-oliva", "vermelho-fogo", "vermelho-telha", "verde-musgo"],
  'Fruta':["maçã", "banana", "laranja", "uva", "morango", 
            "abacaxi", "mamão", "melancia", "kiwi", "pêssego",
            "limão", "pera", "cereja", "ameixa", "figo",
            "goiaba", "abacate", "caqui", "tangerina", "manga",
            "pitaya", "framboesa", "mirtilo", "jabuticaba", "caju",
            "pêssego", "nectarina", "melão", "maracujá", "jambo",
            "lichia", "romã", "carambola", "jaca", "melão",
            "cereja", "groselha", "ameixa", "damasco", "nectarina",
            "pomelo", "tomate", "manga", "papaia", "tâmara",
            "cacau", "physalis", "tamarindo", "kiwano", "longan"]
}
    tema_escolhido = choice(list(palavras.keys()))
    palavra_escolhida_sem_uni = choice(palavras[tema_escolhido])
    palavra_escolhida = unidecode(palavra_escolhida_sem_uni)
    palavra_tema = [palavra_escolhida, tema_escolhido]
    return palavra_tema

def main():
    limpa_tela()
    print(f'{"=="*5 }Jogo da Forca {"=="*5}')
    game = Hangman(rand_palavra())
    while not game.terminou():
        game.status()
        game.letra_board()
        letra = str(input('Escolha uma letra: '))
        game.advinhar(letra)
    game.status()
    game.verificar_win()
    print(f'{"=="*5} Game Over {"=="*5}')

if __name__ == '__main__':
    main()