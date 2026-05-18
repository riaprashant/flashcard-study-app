class FlashCard:
    """A single flashcard with a question and answer."""

    def __init__(self, question: str, answer: str):
        """Create a new flashcard."""
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer: str) -> bool:
        """Check if the user's answer matches the flashcard answer."""
        return user_answer.strip().lower() == self.answer.strip().lower()


def get_non_empty_input(prompt: str) -> str:
    """Keep asking the user for input until they type something."""
    while True:
        user_input = input(prompt).strip()

        if user_input:
            return user_input

        print("Input cannot be empty. Try again.")


def add_flashcard(flashcards: list[FlashCard]) -> None:
    """Ask the user for a question and answer, then save a flashcard."""
    question = get_non_empty_input("Enter the question: ")
    answer = get_non_empty_input("Enter the answer: ")

    flashcards.append(FlashCard(question, answer))
    print("Flashcard added successfully!")


def calculate_score(flashcards: list[FlashCard], user_answers: list[str]) -> int:
    """Calculate how many answers the user got correct."""
    score = 0

    for card, user_answer in zip(flashcards, user_answers):
        if card.check_answer(user_answer):
            score += 1

    return score


def quiz_user(flashcards: list[FlashCard]) -> None:
    """Quiz the user on all saved flashcards."""
    if not flashcards:
        print("No flashcards available. Please add some first.")
        return

    user_answers = []

    for card in flashcards:
        print("\nQuestion:", card.question)
        user_answer = input("Your answer: ")
        user_answers.append(user_answer)

        if card.check_answer(user_answer):
            print("Correct")
        else:
            print("Incorrect. Answer:", card.answer)

    score = calculate_score(flashcards, user_answers)
    print("\nFinal Score:", score, "/", len(flashcards))


def display_menu() -> None:
    """Display the main menu options."""
    print("\n--- Flashcard App ---")
    print("1. Add Flashcard")
    print("2. Quiz")
    print("3. View Flashcards")
    print("4. Quit")


def view_flashcards(flashcards: list[FlashCard]) -> None:
    """Display all saved flashcard questions."""
    if not flashcards:
        print("No flashcards have been added yet.")
        return

    print("\nSaved Flashcards:")

    for index, card in enumerate(flashcards, start=1):
        print(f"{index}. {card.question}")


def main() -> None:
    """Run the flashcard study application."""
    flashcards = []

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            quiz_user(flashcards)
        elif choice == "3":
            view_flashcards(flashcards)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
