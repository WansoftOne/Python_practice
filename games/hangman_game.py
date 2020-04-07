import random

IMAGES = ['''

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
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
'''
]

WORDS = ['AIRPORT', 'TRAIN', 'PLAIN', 'COFE', 'TELEPHONE', 'COMPUTER', 'COUNTRY']

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0 
    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Type a letter:  '))
        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries)
                print('GAME OVER.. The correct word is {}'.format(word))
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter
            letter_indexes = []
        
        try:
            hidden_word.index('-')
        except ValueError:
            print("CONGRATULATIONS YOU WIN!!!! The word is {}".format(word))
            break



def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('//////////////////////////////////////////////////////////////////')

def random_word():
    idx = random.randint(0, len(WORDS) -1 )
    return WORDS[idx]

if __name__ == "__main__":
    print('W E L C O M E  T O  H A N G M A N  G A M E')
    run()