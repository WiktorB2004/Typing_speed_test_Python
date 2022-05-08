# Imports
import random
from curses import wrapper
from english_words import english_words_lower_set #type: ignore

# Generates a random sentence using strings from wordlist
def generate_sentence(wordlist):
    sentence = []
    sentence_length = random.randint(10, 25)
    for i in range(sentence_length):
        sentence.append(wordlist[random.randint(0, len(wordlist) - 1)])
    sentence = ' '.join(sentence)


# Display and style the content of the app on the users screen
def display():
    pass


# Check if user wrote correct character
def check_user_input():
    pass


# Analyze min,max and avg WPM
def analyze_typing_speed():
    pass


# Displays before starting a "game" function
def menu():
    input("Welcome to typing speed test by Wiktor Byrka to continue push any button...")
    return


# Main function of the program - handles whole performance of the app
def main():
    wordlist = list(english_words_lower_set)
    menu()
    generate_sentence(wordlist)


if __name__ == "__main__":
    main()
