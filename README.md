# Flashcard Study App
Demonstration of a Flashcard-Based Study Tool

This project is a terminal-based Flashcard Study Application. The program allows users to create flashcards, store them in memory, and quiz themselves using an interactive command-line interface. It demonstrates basic object-oriented programming, user input handling, and simple program logic in Python.

---

## What is the Flashcard Study App?

The Flashcard Study App is a simple study tool in which users create question-and-answer flashcards and test themselves through a quiz mode. The application provides immediate feedback on answers and tracks the user’s score throughout the session.

This project demonstrates how simple data structures and user interaction can be used to build an educational tool.

---

## App Features

This application includes two main components:

### 1. Flashcard Creation
Users can create flashcards by entering a question and its corresponding answer.

Each flashcard is:
- Stored as an object
- Saved in a list during runtime

Input validation ensures:
- Questions cannot be empty
- Answers cannot be empty

If invalid input is entered, the program prompts the user again.

---

### 2. Quiz Mode
Users can test themselves using all stored flashcards.

In quiz mode:
- Questions are shown one at a time
- The user enters an answer for each question
- The program immediately checks correctness
- Feedback is displayed (“Correct” or “Incorrect”)
- A final score is displayed at the end of the quiz

---

## Program Interface

When the program is run, the user sees a menu:
1. Add flashcard
2. Quiz
3. Quit

The user selects an option using keyboard input.

---

## Input Behavior

The program enforces simple input rules:

- Empty questions are rejected
- Empty answers are rejected
- Users are repeatedly prompted until valid input is entered
- Answer checking is case-insensitive

---

## Code Structure

The program is structured into the following components:

- FlashCard class  
  Stores a question and answer and checks correctness

- add_flashcard()  
  Handles creation and storage of flashcards

- quiz_user()  
  Runs quiz session and tracks score

- check_answer()  
  Compares user input to correct answer

- main()  
  Controls program flow and menu navigation

---

## Example Behavior

A user can create flashcards and immediately quiz themselves.

Example session:

Enter the question: What is 2 + 2?
Enter the answer: 4
Flashcard added successfully!

Question: What is 2 + 2?
Your answer: 4
Correct

Final Score: 1 / 1


---

## Testing

Testing for this project is documented in `test.txt`.

The test plan includes:

- Running the program using `python flashcards.py`
- Adding flashcards with valid and invalid input
- Starting a quiz with and without flashcards
- Checking correct and incorrect answers
- Verifying score calculation
- Confirming program exit behavior

---

## How to Run

Install Python and run the program using:
flashcards.py

---

## Controls

- Menu Input: Select options 1–3
- Keyboard Input: Enter questions and answers
- Quiz Input: Type answers and press Enter
- Exit: Choose option 3
