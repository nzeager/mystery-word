import random

# ADD: After everything below add 'More features'
# ADD: After 'More features' add 'Spicy Mode'
# ADD: Don't penalize for invalid guesses


def play_game():
    # pull in word
    with open('words.txt', 'r') as input_file:
        contents = input_file.read()

    # pick word, create list of letters
    word_list = contents.split()
    word = random.choice(word_list)

    # create board and list of letters
    length = len(word)
    board = "_ "*length

    # game dictionary
    game = {
        'guess_left': 8,
        'letters': list(word),
        'board_letters': list(board),
        'letters_guessed': []
    }

    # runs game
    print(f'Welcome to Mystery Word! Your word has {length} letters.')

    # runs rounds until you guess the word or run out of guessesgit
    while (game['guess_left'] > 0 and '_' in game['board_letters']):
        round(game)

    # Messages for success/failure (reveal word)
    if (game['guess_left'] == 0):
        print(
            f'You have run out of guesses. The correct word was "{word}". Thank you for playing.')
    else:
        print(
            f'Congratulations! You got the word "{word}" Thank you for playing.')

    # Asks if user wants to play again
    print('')
    play = input('Do you want to play again? (y/n) ').lower()
    if (play == 'y'):
        print('')
        play_game()


def round(game_info):
    # uncomment below line to see word in game (for testing)
    print(''.join(game_info['letters']))

    # Display game board and ask for guess
    print(''.join(game_info['board_letters']))
    letter_guess = input(
        'Guess a letter: ').lower()

    # Don't penalize player if they repeat a guess.
    # Don't allow guesses with >1 character.
    # For new guesses, append guess to list of letters
    # guessed so far and mark player right or wrong.
    if (letter_guess in game_info['letters_guessed']):
        print('You have already guessed this letter.')
    elif (len(letter_guess) != 1 or letter_guess == []):
        print("Please enter 1 letter.")
    else:
        game_info['letters_guessed'].append(letter_guess)
        if (letter_guess in game_info['letters']):
            for i in range(0, len(game_info['letters'])):
                if game_info['letters'][i] == letter_guess:
                    game_info['board_letters'][i*2] = letter_guess
            print('Good guess!')
        else:
            game_info['guess_left'] -= 1
            print('Guess again.')

    # Tell player how many guesses are left and
    # what letters they've guessed so far
    print('')
    print(f'Guesses remaining: {game_info["guess_left"]}')
    print(f'Letters guessed so far: {", ".join(game_info["letters_guessed"])}')


if __name__ == "__main__":
    play_game()
