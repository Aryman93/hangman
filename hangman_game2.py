import random
import import_countries
import hangman_ascii_art
import time

"""class gameplay:
    def print_life_wrng-wrds_country_dashes_hangman(life, not_in_word, count):
        print(f'life= {life}            ', end='')
        print(f'not in word: {not_in_word}')
        print("The secret word is the capital of " + '\x1b[0;33;40m' + count + '\x1b[0m')
        print_dashes_and_letters(word, letterS_guessed)
        hangman_ascii_art.draw_hangman(life)"""


def store_highscore_in_file(dictionary, fn="/home/matthew/codecool/hangman/highscores.txt", top_n=10):
    with open(fn,"w") as f:
        for idx, (name, pts) in enumerate(sorted(dictionary.items(), key=lambda x: -x[1])):
            f.write(f"{name}:{pts}\n")
            if top_n and idx == top_n-1:
                break

def load_highscore_from_file(fn="/home/matthew/codecool/hangman/highscores.txt"):
    highscore = {}
    try:
        with open(fn, "r") as f:
            for line in f:
                name, _, points = line.partition(":")
                if name and points:
                    highscore[name] = int(points)
    except FileNotFoundError:
        return {}
    return highscore

def print_highscores_and_ask_for_name(scores, player_name):
    print(f'You scored {scores} points')
    k = load_highscore_from_file()
    if player_name != ' ':
        try:
            if k[player_name] < scores:
                k[player_name] = scores
        except:
            k[player_name] = scores
    store_highscore_in_file(k, top_n=10)
    kk = load_highscore_from_file()
    sorted(kk)
    print('   Highscores:')
    x = 1
    for line in open('/home/matthew/codecool/hangman/highscores.txt'):
        print(f'{x}. {line}', end='')
        x += 1
    input('Press Enter to continue ')

def make_word_without_repetition(word):
    word_without_repetitions = ('')
    for k in range(len(word)):
        if word[k] not in word_without_repetitions and word[k] != ' ':
            word_without_repetitions = word_without_repetitions + word[k].lower()
    return word_without_repetitions

def print_dashes_and_letters(word, letterS_guessed):
    print('')
    for i in range(len(word)):
        if word[i].lower() in letterS_guessed:
            print(f"{word[i]} ", end=(''))
        elif word[i] == (' '):
            print('  ', end='')
        else:
            print('_ ', end=(''))
    print('')

def ask_if_y_or_n(question, y, n):
    a = ''
    while a != n or a != y:
        a = input(question).lower()
        if a == n:
            return n
        elif a == y:
            return y

game_running = True
new_game = True
tried_a_letter = False
didnt_guess_a_letter = False
wrong_word = False

while game_running:
    if new_game == True:
        new_game = False
        word_try = 0
        w_or_l_asked = False
        w_or_l = ' '
        start_time = time.time()
        countries, capitals = import_countries.import_countries_and_capitals()
        a = random.choice(range(0, len(capitals)))
        word = capitals[a]
        count = countries[a]
        player_word = ''
        life = 5
        letterS_guessed = ('')
        not_in_word = ('')
        word_without_repetitions = make_word_without_repetition(word)
        run = input("\n\n\n\n\n\n Press enter to start the game.\n\n\n\n\n\n", )
        letter = (' ')
    wrong_word = False
    
    if life > 0:
        print(f'life= {life}            ', end='')
        print(f'not in word: {not_in_word}')
        print("The secret word is the capital of " + '\x1b[0;33;40m' + count + '\x1b[0m')
        print_dashes_and_letters(word, letterS_guessed)
        hangman_ascii_art.draw_hangman(life)
        if didnt_guess_a_letter == True or (player_word != word.lower() and word_try > 0):
            print("You didn't guess")
        else:
            print('')
        if (len(letter) == 1) and (w_or_l_asked == False):
            w_or_l = input('Would you like to guess the word, or a letter?: (w/Enter)')
            if w_or_l == 'w' or w_or_l == '':
                w_or_l_asked = True
                continue
            else:
                continue
        
        w_or_l_asked = False
        if w_or_l == 'w':
            player_word = input('Enter a word: ').lower()
            word_try += 1
            if player_word != word.lower():
                wrong_word = True
                life -= 2
                if life < 0:
                    life = 0

        if w_or_l == '':
            didnt_guess_a_letter = False
            letter = input('Enter a letter: ').lower()
            if len(letter) == 1 and letter in word.lower() and letter not in letterS_guessed:
                tried_a_letter = True
                letterS_guessed = letterS_guessed + letter
            elif len(letter) == 1 and letter not in word.lower() and letter not in not_in_word:
                not_in_word = not_in_word + letter + " "
                didnt_guess_a_letter = True
                life -=  1
            else:
                continue

        if len(letterS_guessed) == len(word_without_repetitions) or player_word == word.lower():
            print(f'life= {life}            ', end='')
            print(f'not in word: {not_in_word}')
            print("The secret word is the capital of " + '\x1b[0;33;40m' + count + '\x1b[0m')
            print(word)
            print("   /////\\\\\\\\")
            print("  /         \\")
            print(" /           \\")
            print("|    ^   ^    |")
            print("|    _____    |")
            print("|    \___/    |")
            print(" \\           /")
            print("   \\_______/")
            print('')
            tries = int(len(letterS_guessed) + len(not_in_word) / 2 + word_try)
            scores = 1040 - tries*40 - int(time.time() - start_time)
            ans_win = ask_if_y_or_n('\x1b[1;32;40m' + "You won!" + '\x1b[0m' + f" It took you {int(time.time() - start_time)} seconds and {tries} tries. Restart? (y/n)", 'y', 'n')
            wrong_word = False
            print_highscores_and_ask_for_name(scores, input("Please enter your name: "))
            if ans_win == 'n':
                game_running = False
            else:
                new_game = True
                    
        if life < 1:
            print(f'life= {life}            ', end='')
            print(f'not in word: {not_in_word}')
            print("The secret word is the capital of " + '\x1b[0;33;40m' + count + '\x1b[0m')
            print_dashes_and_letters(word, letterS_guessed)
            hangman_ascii_art.draw_hangman(life)
            print("You didn't guess, correct answer is " + '\x1b[0;33;40m' + f'{word}' + '\x1b[0m')
            ans_lose = ask_if_y_or_n('\x1b[1;31;40m' + "You lost." + '\x1b[0m' + " Restart? (y/n)", 'y', 'n')
            scores = 0
            print_highscores_and_ask_for_name(scores, ' ')
            if ans_lose == 'n':
                game_running = False
            else:
                new_game = True