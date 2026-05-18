import random


class FlashCard:
    """A flashcard with a question, answer, and difficulty level."""

    def __init__(self, question: str, answer: str, difficulty: str):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty

    def check_answer(self, user_answer: str) -> bool:
        """Check whether the user's answer matches the correct answer."""
        return user_answer.strip().lower() == self.answer.strip().lower()


def print_line() -> None:
    """Print a divider line to make the app easier to read."""
    print("=" * 60)


def print_section(title: str) -> None:
    """Print a formatted section title."""
    print_line()
    print(title.upper())
    print_line()


def get_non_empty_input(prompt: str) -> str:
    """Keep asking the user for input until they enter something."""
    while True:
        user_input = input(prompt).strip()

        if user_input:
            return user_input

        print("Input cannot be empty. Try again.")


def choose_difficulty() -> str:
    """Let the user choose a difficulty level for a flashcard."""
    print("\nChoose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Choose 1, 2, or 3: ").strip()

        if choice == "1":
            return "Easy"
        if choice == "2":
            return "Medium"
        if choice == "3":
            return "Hard"

        print("Invalid choice. Please enter 1, 2, or 3.")


def add_flashcard(flashcards: list[FlashCard]) -> None:
    """Create a new flashcard and add it to the deck."""
    print_section("Add Flashcard")

    question = get_non_empty_input("Enter the question: ")
    answer = get_non_empty_input("Enter the answer: ")
    difficulty = choose_difficulty()

    flashcards.append(FlashCard(question, answer, difficulty))
    print("\nFlashcard added successfully!")


def view_flashcards(flashcards: list[FlashCard]) -> None:
    """Show all flashcards currently saved in the deck."""
    print_section("Saved Flashcards")

    if not flashcards:
        print("No flashcards have been added yet.")
        return

    for index, card in enumerate(flashcards, start=1):
        print(f"{index}. [{card.difficulty}] {card.question}")


def practice_mode(flashcards: list[FlashCard]) -> None:
    """Let the user review flashcards without being scored."""
    print_section("Practice Mode")

    if not flashcards:
        print("No flashcards available. Please add some first.")
        return

    for card in flashcards:
        print("\nQuestion:", card.question)
        input("Press Enter to reveal the answer...")
        print("Answer:", card.answer)


def quiz_mode(flashcards: list[FlashCard]) -> list[FlashCard]:
    """Quiz the user, track score, and return missed flashcards."""
    print_section("Quiz Mode")

    if not flashcards:
        print("No flashcards available. Please add some first.")
        return []

    quiz_cards = flashcards.copy()
    random.shuffle(quiz_cards)

    score = 0
    streak = 0
    best_streak = 0
    missed_cards = []

    for number, card in enumerate(quiz_cards, start=1):
        print(f"\nQuestion {number} of {len(quiz_cards)}")
        print(f"Difficulty: {card.difficulty}")
        print("Question:", card.question)

        user_answer = input("Your answer: ")

        if card.check_answer(user_answer):
            print("Correct!")
            score += 1
            streak += 1
            best_streak = max(best_streak, streak)
        else:
            print("Incorrect.")
            print("Correct answer:", card.answer)
            streak = 0
            missed_cards.append(card)

        print("Current streak:", streak)

    show_quiz_summary(score, len(quiz_cards), best_streak, missed_cards)
    return missed_cards


def show_quiz_summary(
    score: int,
    total_questions: int,
    best_streak: int,
    missed_cards: list[FlashCard],
) -> None:
    """Display the final quiz results."""
    print_section("Quiz Summary")

    accuracy = calculate_accuracy(score, total_questions)

    print("Final Score:", score, "/", total_questions)
    print("Accuracy:", str(accuracy) + "%")
    print("Best Streak:", best_streak)

    if missed_cards:
        print("\nQuestions to review:")
        for card in missed_cards:
            print("-", card.question)
    else:
        print("\nPerfect score! No missed questions.")


def calculate_accuracy(score: int, total_questions: int) -> int:
    """Calculate quiz accuracy as a percentage."""
    if total_questions == 0:
        return 0

    return round((score / total_questions) * 100)


def review_missed_questions(missed_cards: list[FlashCard]) -> None:
    """Let the user review only the questions they missed."""
    print_section("Review Missed Questions")

    if not missed_cards:
        print("No missed questions to review yet.")
        return

    for card in missed_cards:
        print("\nQuestion:", card.question)
        input("Press Enter to reveal the answer...")
        print("Answer:", card.answer)


def show_menu() -> None:
    """Display the main menu."""
    print("\n--- Flashcard Study App ---")
    print("1. Add Flashcard")
    print("2. View Flashcards")
    print("3. Practice Mode")
    print("4. Quiz Mode")
    print("5. Review Missed Questions")
    print("6. Quit")


def main() -> None:
    """Run the Flashcard Study App."""
    flashcards = []
    missed_cards = []

    print_section("Welcome to the Flashcard Study App")
    print("Create flashcards, practice them, quiz yourself, and review mistakes.")

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            view_flashcards(flashcards)
        elif choice == "3":
            practice_mode(flashcards)
        elif choice == "4":
            missed_cards = quiz_mode(flashcards)
        elif choice == "5":
            review_missed_questions(missed_cards)
        elif choice == "6":
            print("Goodbye! Keep studying.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
