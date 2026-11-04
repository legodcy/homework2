# Science
science_q = [
    "Which planet do we live on?",
    "What color is the sky on a clear day?",
    "What gas do humans breathe in to live?",
    "How many legs does a dog have?",
    "Water freezes into what?",
    "What is the closest star to Earth?",
    "Which planet is called the Red Planet?",
    "How many planets are in our solar system?",
    "Which organ pumps blood in the body?",
    "What is the natural satellite of Earth?"
]
science_a = ["earth", "blue", "oxygen", "4", "ice", "sun", "mars", "8", "heart", "moon"]

# Sports
sports_q = [
    "How many players are on the field for one football team?",
    "Which sport uses a basket and a hoop?",
    "What color is the medal for first place?",
    "Which sport is played at Wimbledon?",
    "How many rings are on the Olympic flag?",
    "Which sport uses a shuttlecock?",
    "How many minutes is a regular football match?",
    "Which sport do you play in a pool?",
    "Which country is Lionel Messi from?",
    "How many players of one team are on a basketball court?"
]
sports_a = ["11", "basketball", "gold", "tennis", "5", "badminton", "90", "swimming", "argentina", "5"]

# History (Iran)
history_q = [
    "What is the capital of Iran?",
    "What is the Persian New Year called?",
    "What is the old name of Iran in the West?",
    "Who founded the Achaemenid Empire?",
    "Who wrote the Shahnameh?",
    "Who wrote the book Golestan?",
    "Which poet wrote the Rubaiyat and was also an astronomer?",
    "Naqsh-e Jahan Square is in which city?",
    "What is the official language of Iran?",
    "Persepolis is an ancient city in which country?"
]
history_a = ["tehran", "nowruz", "persia", "cyrus", "ferdowsi", "saadi", "khayyam", "isfahan", "persian", "iran"]

while True:
    print("\n=== Quiz Game ===")
    print("1 - Science")
    print("2 - Sports")
    print("3 - History")
    print("4 - Exit")

    choice = input("Choose a category: ")

    match choice:
        case "1":
            questions = science_q
            answers = science_a
            category_name = "Science"
        case "2":
            questions = sports_q
            answers = sports_a
            category_name = "Sports"
        case "3":
            questions = history_q
            answers = history_a
            category_name = "History"
        case "4":
            print("Goodbye!")
            break
        case _:
            print("Invalid option, try again")
            continue

    print("\n--- " + category_name + " Quiz ---")
    score = 0

    for i in range(len(questions)):
        print("\nQuestion", i + 1, ":", questions[i])
        user_answer = input("Your answer: ")

        if user_answer.lower().strip() == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The answer is:", answers[i])

    print("\n=== Result ===")
    print("Your score:", score, "out of", len(questions))

    if score >= 8:
        print("Excellent!")
    elif score >= 5:
        print("Good job!")
    else:
        print("Try again!")
