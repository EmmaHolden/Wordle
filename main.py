from listofwords import word_list
import random
import colorama as cr

cr.init(autoreset=True)


def print_display(display):
    printed_display = ""
    for l in display:
        printed_display += l
    print(printed_display)


def get_input():
    is_valid = False
    while not is_valid:
        answer = input("\nPlease enter a five-letter word.\n").upper()
        is_valid = answer.isalpha() and len(answer) == 5
    return answer


def update_display(word_length, secret, answer, display):
    for x in range(word_length):
        updated_character = ""
        if secret[x] == answer[x]:
            updated_character = f"{cr.Fore.GREEN}{answer[x]}"
        elif answer[x] in secret and secret[x] != answer[x]:
            updated_character = f"{cr.Fore.WHITE}{answer[x]}"
        else:
            updated_character = f"{cr.Fore.RED}{answer[x]}"
        display[x] = updated_character


def populate_display(length):
    display = []
    for _ in range(length):
        display += "_"
    return display


def main():
    max_tries = 6
    secret_word = random.choice(word_list).upper()
    word_length = len(secret_word)
    display_list = populate_display(word_length)
    end_of_game = False
    print(
        "Welcome to Wordle.\nYou have six attempts to try to guess a five-letter word.\n"
        "You need to know the following things:\nIf you guess the correct letter in the correct place, it will turn"
        " green.\nIf the letter is correct but in the wrong place, it will be white.\nIf the letter is not in the "
        "word, it will be red.\n")
    while end_of_game == False:

        print_display(display_list)
        answer = get_input()
        max_tries -= 1
        update_display(word_length, secret_word, answer, display_list)
        if max_tries == 0:
            end_of_game = True
            print(f"Sorry, you lose. The answer was {secret_word}")
            play_again_lose = input("Would you like to play again?\n")
            if play_again_lose.lower() == "yes":
                main()
            else:
                print("Okay. Goodbye.")
        if secret_word == answer:
            end_of_game = True
            play_again_win = input("That's correct. You win! Would you like to play again?\n")
            if play_again_win == "yes":
                main()
            else:
                print("Okay. Goodbye.")


main()


