# flashcard-challenge-game
<img width="881" height="636" alt="Screenshot 2026-05-17 at 8 41 05 PM" src="https://github.com/user-attachments/assets/c29a6e42-c4e9-4a61-a80f-10a4594e048f" />

This repository contains a Pygame based Flashcard Challenge game. The application allows users to create their own flashcards, quiz themselves, and track their score, streak, and quiz accuracy.

---

# What is Flashcard Challenge?

Flashcard Challenge is an interactive study game where users create their own flashcards and test themselves through a graphical quiz interface.

The game tracks:

• Final score  
• Accuracy percentage  
• Best answer streak  
• Missed questions for review  

The project demonstrates how Python can be used to build an interactive educational application with graphics and user interaction.

---

# Features

## 1. Create Custom Flashcards

Users can create their own flashcards directly inside the game.

For each flashcard, the user enters:

• A question  
• A correct answer  

The program stores flashcards as objects in a list during runtime.

---

## 2. Interactive Quiz Mode

The game quizzes the user using all created flashcards.

Features include:

• Randomized question order  
• Real time answer checking  
• Correct and incorrect feedback screens  
• Score tracking  
• Streak tracking  
• Accuracy calculation  

---

## 3. Results Screen

At the end of the quiz, the game displays:

• Final score  
• Accuracy percentage  
• Best streak achieved  
• Questions answered incorrectly  

The player can then choose to:

• Play again  
• Quit the game  

---

# Running the Project

First make sure you install pygame and pytest. To do this, enter 'pip3 install -r requirements.txt'. After that, run flashcard_challenge.py. A pygame window should open.

---

# Running Tests

This project uses pytest for testing. In terminal, run test_flashcards.py.

---

# Controls

## Keyboard

• Type answers using the keyboard  
• Press Backspace to delete text  
• Press Enter to submit answers  

## Mouse

• Click buttons to navigate the game  

---

# Code Structure

## flashcard_challenge.py

Main application file containing:

• FlashCard class  
• Game loop  
• Quiz system  
• Flashcard creation system  
• Score and streak tracking  
• Result screens  
• Pygame rendering logic  

## tests/test_flashcards.py

Contains unit tests for important methods and functionality.

---

# Example Gameplay

1. Start the game  
2. Create custom flashcards  
3. Start the quiz  
4. Answer questions 
5. View final score and statistics  

Example:

Question: What is 2 + 2?
Your Answer: 4

Correct!

---

# Testing

The following behaviors were tested:

1. Flashcard creation  
2. Correct answer checking  
3. Incorrect answer checking  
4. Case insensitive answer matching  
5. Score calculation logic  
6. Game startup and exit behavior  
7. Randomized quiz order  
8. Review of missed questions  

---

# Three Functions I Am Most Proud Of

## 1. FlashCard.check_answer()

I am proud of this method because it allows flexible answer checking without worrying about capitalization or extra spaces.

## 2. create_flashcards()

I like this function because it allows users to build their own custom quiz directly inside the game.

## 3. quiz_user()

I am proud of this function because it manages the main gameplay loop, score tracking, streak tracking, and answer validation.
