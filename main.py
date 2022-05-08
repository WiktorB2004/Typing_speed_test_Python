# Imports
import random
import time
import curses
from curses import wrapper
from english_words import english_words_lower_set #type: ignore
from os import system

# Generates a random sentence using strings from wordlist
def generate_sentence(wordlist):
    sentence = []
    sentence_length = random.randint(10, 20)
    for i in range(sentence_length):
        sentence.append(wordlist[random.randint(0, len(wordlist) - 1)])
    return sentence

# Display and style the content of the app on the users screen
def display(stdscr):
    start_time = time.time()
    wordlist = list(english_words_lower_set)
    sentence = generate_sentence(wordlist)
    sentence = ' '.join(sentence)
    x, y = 0, 0
    user_input = []
    errors = 0
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    stdscr.clear()
    stdscr.addstr(0, 0, sentence)
    stdscr.move(y, x)
    while len(user_input) < len(sentence):
        key = stdscr.getkey()
        x = len(user_input)
        if key == '0':
            break
        elif key == '\x08':
            user_input.pop()
            stdscr.addstr(y, x - 1, sentence[x-1:])
            stdscr.move(y, x)
        elif ord(key) > 96 and ord(key) < 123 or ord(key) == 32 or ord(key) == 39:
            user_input.append(key)
            is_correct = check_user_input(sentence, key, x)
            if is_correct:
                stdscr.addstr(y, x, str(key), curses.color_pair(1))
            else:
                stdscr.addstr(y, x, str(key), curses.color_pair(2))
                errors += 1
    stdscr.refresh()
    stdscr.getkey()
    return len(sentence.split(' ')), round(time.time() - start_time), errors


# Check if user given correct character
def check_user_input(sentence, key, x):
    return sentence[x] == key


# Analyze avg WPM
def analyze_typing_speed(words, time):
    return f'Average WPM: {(words/time)*60}'


# Displays before starting a "game" function
def menu():
    input("Welcome to typing speed test by Wiktor Byrka to continue push any button... (to quit the test push 0 two times)")
    return


# Main function of the program - handles whole performance of the app
def main():
    system('mode con: cols=200 lines=50')
    menu()
    output = wrapper(display)
    words, time, error_count = output
    print(f'{analyze_typing_speed(words, time)}\nErrors: {error_count}')
    play_again = input('Click any button to exit or type again to play again: ')
    if play_again.lower() == 'again':
        main()

if __name__ == "__main__":
    main()
