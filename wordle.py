
"""
NOT COMPLETE
There's a bug that's yet to be solved.
More functionality will be added.
The program doesn't check whether user guesses are actual English words or not unlike the original game.
"""
# Try debug with word "wipes" and try "sinus"


from random_word import RandomWords

def get_random_word():
    r = RandomWords()
    word = r.get_random_word(includePartOfSpeech="noun", 
                            minCorpusCount = 100, 
                            minLength = 5, 
                            maxLength = 5)
    
    if (word is None) or (any(letter.isupper() for letter in word)) or (not word.isalpha()):
        return get_random_word()
    
    return word

def compare(user_guess, word):
    comparison = {}
    for letter in user_guess:
        comparison[letter] = []
    counter = 0
    for letter_guess, letter_word in zip(user_guess, word):
        if letter_guess == letter_word:
            comparison[letter_guess].append("Full match")
            word[counter] = 0
        elif letter_guess in list(word):
            comparison[letter_guess].append("Half match")
            word[counter] = 0
        else:
            comparison[letter_guess].append("No match")
        counter += 1
    visualize(comparison)
    return comparison

def win(comparison):
    for item in comparison:
        for element in item:
            if (element != "Full match"):
                return False
    return True

def make_guess(word):
    user_guess = input("Make a guess: ")
    while (len(user_guess) != 5):
        print("Only 5-letter words are accepted. Try again.")
        user_guess = input("Make a guess: ")
    comparison = (compare(user_guess, list(word))).values()
    return comparison

def visualize(comparison):
    letter_cells = ""
    comparison_cells = ""
    print("  ___    ___    ___    ___    ___")
    print(" |   |  |   |  |   |  |   |  |   |")
    for letter in comparison:
        for letter_comparison in comparison[letter]:
            letter_cells += f" | {letter.upper()} | "
            if (letter_comparison == "Full match"):
                comparison_cells += " |_✔_| "
            elif (letter_comparison == "Half match"):
                comparison_cells += " |_✸_| "
            else:
                comparison_cells += " |_✘_| "
    print(letter_cells)
    print(comparison_cells)

def main():
    
    word = get_random_word()
    #print(word.upper())

    tries = 0
    while True:
        if (win(make_guess(word))):
            print("You won!")
            break
        tries += 1
        if (tries == 6):
            print("You lost")
            print(f"It was '{word}'")
            break
if (__name__ == "__main__"):
    main()



