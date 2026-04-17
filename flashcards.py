class FlashCard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.strip().lower()


def add_flashcard(flashcards):
    while True:
        question = input("Enter the question: ").strip()
        if question == "":
            print("Question cannot be empty. Try again.")
        else:
            break

    while True:
        answer = input("Enter the answer: ").strip()
        if answer == "":
            print("Answer cannot be empty. Try again.")
        else:
            break

    flashcards.append(FlashCard(question, answer))
    print("Flashcard added successfully!")


def quiz_user(flashcards):
    if len(flashcards) == 0:
        print("No flashcards available. Please add some first.")
        return

    score = 0

    for card in flashcards:
        print("\nQuestion:", card.question)
        user_answer = input("Your answer: ")
        if card.check_answer(user_answer):
            print("Correct")
            score += 1
        else:
            print("Incorrect. Answer:", card.answer)
    print("\nFinal Score:", score, "/", len(flashcards))


def main():
    flashcards = []

    while True:
        print("\n--- Flashcard App ---")
        print("1. Add Flashcard")
        print("2. Quiz")
        print("3. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            quiz_user(flashcards)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
