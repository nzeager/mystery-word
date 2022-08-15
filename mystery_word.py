import random


def play_game():
    # pull in word
    with open('words.txt', 'r') as input_file:
        contents = input_file.read()

    # pick word, create list of letters
    word_list = contents.split()
    word = random.choice(word_list)
    # letters = list(word)

    # create board and list of letters
    length = len(word)
    board = "_ "*length
    # board_letters = list(board)

    # game dictionary
    game = {
        'guess_left': 8,
        'letters': list(word),
        'board_letters': list(board)
    }

    # take guess
    # update board
    while (game['guess_left'] > 0 and '_' in game['board_letters']):
        round(game)


# tracks action for one round
def round(game):
    print(''.join(game['letters']))
    print(''.join(game['board_letters']))
    letter_guess = input(
        'Guess a letter: ')
    if (letter_guess in game['letters']):
        for i in range(0, len(game['letters'])):
            if game['letters'][i] == letter_guess:
                game['board_letters'][i*2] = letter_guess
    else:
        game['guess_left'] -= 1
    print(f'Guesses remaining: {game["guess_left"]}')


if __name__ == "__main__":
    play_game()
