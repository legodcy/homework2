import random

words = ["python", "computer", "keyboard", "program", "variable",
         "function", "internet", "monitor", "student", "teacher"]

while True:
    # Choose a random word
    word = words[random.randrange(len(words))]

    display = []
    for letter in word:
        display.append("_")

    wrong_letters = []
    guessed_letters = []
    wrong = 0
    max_wrong = 6

    print("\n=== Hangman ===")
    print("The word has", len(word), "letters. You can make", max_wrong, "mistakes.")

    while wrong < max_wrong and "_" in display:
        print("\nWord:", " ".join(display))
        print("Wrong letters:", wrong_letters)
        print("Remaining mistakes:", max_wrong - wrong)

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter just one letter")
        elif guess in guessed_letters:
            print("You already guessed this letter")
        else:
            guessed_letters.append(guess)

            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        display[i] = guess
                print("Correct!")
            else:
                wrong += 1
                wrong_letters.append(guess)
                print("Wrong!")

    # Result
    if "_" not in display:
        print("\nYou won! The word was:", word)
    else:
        print("\nYou lost! The word was:", word)

    again = input("\nPlay again? (y/n): ").lower().strip()

    match again:
        case "y":
            continue
        case _:
            print("Goodbye!")
            break
