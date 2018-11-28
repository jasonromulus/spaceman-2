import random
# template load word
def load_word(): # works
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    split_words_list = words_list[0].split(' ')
    secret_word = random.choice(split_words_list)
    return secret_word

def get_blank_word(secret_word, letters_guessed):  #letters_guessed is a list of the letters i guessed.
    # String that stores blanks if letter is incorrect or blanks and correct letter if guess is correct
    hidden_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            hidden_word += letter + ""
        else:
            hidden_word += " _ "
    return hidden_word

def choices_available(letters_guessed):
    choices = list("abcdefghijklmnopqrstuvwxyz")
    for letter in letters_guessed:
        if letter in choices:
            # remive that letter in choices
            choices.remove(letter)
    return choices

def is_secret_word_guessed(secret_word, letters_guessed):
    """
        Keep playing the game and check if the user wins
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def spaceman_head():
    print(" o ")

def draw_spaceman(guess):

    if guess == 1:
        spaceman_head()
    elif guess == 2:
        spaceman_head()
        print(" | ")
    elif guess == 3:
        spaceman_head()
        print("/| ")
    elif guess == 4:
        spaceman_head()
        print("/|\\")
    elif guess == 5:
        spaceman_head()
        print("/|\\")
        print("/ ")
    elif guess == 6:
        spaceman_head()
        print("/|\\")
        print("/ \\")

def spaceman():
    # get a secret_word
    secret_word = str(load_word())
    # an empty list for letters_guessed
    letters_guessed = []
    # ask a user for a letter to guess
    guess = 0
    while not is_secret_word_guessed(secret_word, letters_guessed) and guess != 7:
        print("The word you need to guess is {} .".format(get_blank_word(secret_word, letters_guessed)))
        user_guess = input("Please type a letter \n -> ")
        if user_guess not in letters_guessed:
            letters_guessed.append(user_guess)
            choices_available(letters_guessed)
            #print("Guessed letters: {} ").format(str(letters_guessed) + " ")
            if user_guess not in secret_word:
                guess += 1
                draw_spaceman(guess)
            # elif is_secret_word_guessed(secret_word, letters_guessed) == true:
            #     print("you won!")
        else:
            print('type another letter...')
    # elif is_secret_word_guessed(secret_word, letters_guessed) == true:
    #     # when they win what do you want them to say
    #     print('you won')
    else:
        if is_secret_word_guessed(secret_word, letters_guessed) == True:
            print("YAY YOU WON!")
        elif is_secret_word_guessed(secret_word, letters_guessed) == False:
            print("YOU LOST. BUT IF YOU HAD FUN YOU WON!")



spaceman()