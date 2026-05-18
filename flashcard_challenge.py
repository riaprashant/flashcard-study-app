import pygame
import sys
import random

pygame.init()

WIDTH = 900
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flashcard Challenge")

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 60)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (60, 120, 220)
GREEN = (0, 170, 80)
RED = (200, 40, 40)
GRAY = (220, 220, 220)

#Stores one flashcard question and answer
class FlashCard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.strip().lower()

#Draw text onto the screen
def draw_text(text, x, y, color=BLACK, used_font=font):
    surface = used_font.render(text, True, color)
    screen.blit(surface, (x, y))

#Draw text centered horizontally.
def draw_centered_text(text, y, color=BLACK, used_font=font):
    surface = used_font.render(text, True, color)
    rect = surface.get_rect(center=(WIDTH // 2, y))
    screen.blit(surface, rect)

#Draw a button and return its rectangle.
def draw_button(text, x, y, width, height, color):
    rect = pygame.Rect(x, y, width, height)

    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 3)

    text_surface = small_font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)

    screen.blit(text_surface, text_rect)

    return rect

#Close the game safely.
def quit_game():
    pygame.quit()
    sys.exit()

#Display the start screen.
def start_screen():
    while True:
        screen.fill(WHITE)

        draw_centered_text("Flashcard Challenge", 120, BLUE, big_font)
        draw_centered_text(
            "Create your own flashcards and test yourself.",
            240
        )
        draw_centered_text(
            "Track your score, streak, and accuracy.",
            290
        )

        start_button = draw_button(
            "Start",
            320,
            400,
            250,
            70,
            GRAY
        )

        quit_button = draw_button(
            "Quit",
            320,
            500,
            250,
            70,
            GRAY
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return

                if quit_button.collidepoint(event.pos):
                    quit_game()

#Allow the user to type text into an input box.
def get_text_input(prompt):
    user_text = ""

    while True:
        screen.fill(WHITE)

        draw_centered_text(prompt, 180, BLUE)

        pygame.draw.rect(screen, GRAY, (100, 280, 700, 60))
        pygame.draw.rect(screen, BLACK, (100, 280, 700, 60), 3)

        draw_text(user_text, 120, 295)

        submit_button = draw_button(
            "Submit",
            325,
            420,
            250,
            60,
            GRAY
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_text.strip() != "":
                        return user_text

                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]

                else:
                    if len(user_text) < 40:
                        user_text += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if submit_button.collidepoint(event.pos):
                    if user_text.strip() != "":
                        return user_text

#Allow the user to create their own flashcards.
def create_flashcards():
    flashcards = []

    while True:
        question = get_text_input("Enter a question")
        answer = get_text_input("Enter the answer")

        flashcards.append(FlashCard(question, answer))

        while True:
            screen.fill(WHITE)

            draw_centered_text("Flashcard Added!", 180, GREEN)
            draw_centered_text("Would you like to add another card?", 260)

            yes_button = draw_button(
                "Yes",
                220,
                400,
                180,
                70,
                GRAY
            )

            no_button = draw_button(
                "Start Quiz",
                500,
                400,
                180,
                70,
                GRAY
            )

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button.collidepoint(event.pos):
                        break

                    if no_button.collidepoint(event.pos):
                        return flashcards
            else:
                continue

            break

#Display correct or incorrect feedback.
def show_feedback(message, color):
    screen.fill(WHITE)

    draw_centered_text(message, 300, color, big_font)

    pygame.display.update()
    pygame.time.delay(1200)

#Run the flashcard quiz.
def quiz_user(flashcards):
    cards = flashcards.copy()
    random.shuffle(cards)

    score = 0
    streak = 0
    best_streak = 0
    missed_cards = []

    for index, card in enumerate(cards):
        user_answer = ""
        answered = False

        while not answered:
            screen.fill(WHITE)

            draw_text(
                f"Question {index + 1} of {len(cards)}",
                50,
                40
            )

            draw_text(f"Score: {score}", 50, 90)
            draw_text(f"Streak: {streak}", 50, 140)

            draw_text("Question:", 100, 240, BLUE)
            draw_text(card.question, 100, 300)

            pygame.draw.rect(screen, GRAY, (100, 390, 700, 60))
            pygame.draw.rect(screen, BLACK, (100, 390, 700, 60), 3)

            draw_text(user_answer, 120, 405)

            submit_button = draw_button(
                "Submit",
                325,
                510,
                250,
                60,
                GRAY
            )

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        answered = True

                    elif event.key == pygame.K_BACKSPACE:
                        user_answer = user_answer[:-1]

                    else:
                        if len(user_answer) < 40:
                            user_answer += event.unicode

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if submit_button.collidepoint(event.pos):
                        answered = True

        if card.check_answer(user_answer):
            score += 1
            streak += 1
            best_streak = max(best_streak, streak)

            show_feedback("Correct!", GREEN)

        else:
            streak = 0
            missed_cards.append(card)

            show_feedback(
                f"Incorrect! Answer: {card.answer}",
                RED
            )

    show_results(score, len(cards), best_streak, missed_cards)

#Display the final results screen.
def show_results(score, total, best_streak, missed_cards):
    accuracy = round((score / total) * 100)

    while True:
        screen.fill(WHITE)

        draw_centered_text("Quiz Complete!", 95, BLUE, big_font)

        draw_centered_text(f"Final Score: {score} / {total}", 200)
        draw_centered_text(f"Accuracy: {accuracy}%", 260)
        draw_centered_text(f"Best Streak: {best_streak}", 320)

        if missed_cards:
            draw_text("Questions To Review:", 70, 400, RED)

            y = 450

            for card in missed_cards[:4]:
                draw_text(
                    f"• {card.question}",
                    100,
                    y,
                    BLACK,
                    small_font
                )
                y += 35

        else:
            draw_centered_text("Perfect Score!", 420, GREEN)

        play_again_button = draw_button(
            "Play Again",
            180,
            560,
            220,
            60,
            GRAY
        )

        quit_button = draw_button(
            "Quit",
            500,
            560,
            220,
            60,
            GRAY
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    return main()

                if quit_button.collidepoint(event.pos):
                    quit_game()

#Run the Flashcard Challenge game.
def main():
    start_screen()

    flashcards = create_flashcards()

    if len(flashcards) == 0:
        quit_game()

    quiz_user(flashcards)


if __name__ == "__main__":
    main()
