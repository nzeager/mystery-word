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
def round(game_info):
    print(''.join(game_info['letters']))
    print(''.join(game_info['board_letters']))
    letter_guess = input(
        'Guess a letter: ')
    if (letter_guess in game_info['letters']):
        for i in range(0, len(game_info['letters'])):
            if game_info['letters'][i] == letter_guess:
                game_info['board_letters'][i*2] = letter_guess
    else:
        game_info['guess_left'] -= 1
    print(f'Guesses remaining: {game_info["guess_left"]}')


if __name__ == "__main__":
    play_game()
