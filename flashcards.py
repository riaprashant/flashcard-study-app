class FlashCard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.strip().lower()


def add_flashcard(flashcards):
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    flashcards.append(FlashCard(question, answer))


def quiz_user(flashcards):
    score = 0

    for card in flashcards:
        user_answer = input(card.question + ": ")

        if card.check_answer(user_answer):
            print("Correct")
            score += 1
        else:
            print("Incorrect. Answer:", card.answer)

    print("Score:", score, "/", len(flashcards))


def main():
    flashcards = []

    while True:
        print("\n1. Add Flashcard")
        print("2. Quiz")
        print("3. Quit")

        choice = input("Choose: ")

        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            quiz_user(flashcards)
        elif choice == "3":
            break


if __name__ == "__main__":
    main()
