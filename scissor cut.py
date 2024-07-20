import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the result of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "Rock" and computer_choice == "Scissors") or \
       (user_choice == "Scissors" and computer_choice == "Paper") or \
       (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    return "You lose!"

# Function to play a round
def play_round(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    # Update labels
    label_computer_choice.config(text=f"Computer chose: {computer_choice}")
    label_result.config(text=result)
    
    # Update scores
    if result == "You win!":
        global user_score
        user_score += 1
    elif result == "You lose!":
        global computer_score
        computer_score += 1
    
    label_user_score.config(text=f"Your score: {user_score}")
    label_computer_score.config(text=f"Computer's score: {computer_score}")

# Function to prompt for play again
def play_again():
    if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
        label_computer_choice.config(text="Computer chose: ")
        label_result.config(text="")
    else:
        root.quit()

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.configure(bg='light pink')

# Initialize scores
user_score = 0
computer_score = 0

# Create and place widgets
tk.Label(root, text="Rock-Paper-Scissors Game", bg='light pink', fg='black', font=('Helvetica', 16)).pack(pady=10)

frame_buttons = tk.Frame(root, bg='light pink')
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Rock", command=lambda: play_round("Rock")).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Paper", command=lambda: play_round("Paper")).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Scissors", command=lambda: play_round("Scissors")).pack(side=tk.LEFT, padx=5)

label_computer_choice = tk.Label(root, text="Computer chose: ", bg='light pink', fg='black', font=('Helvetica', 12))
label_computer_choice.pack(pady=10)

label_result = tk.Label(root, text="", bg='light pink', fg='black', font=('Helvetica', 12))
label_result.pack(pady=10)

frame_scores = tk.Frame(root, bg='light pink')
frame_scores.pack(pady=10)

label_user_score = tk.Label(frame_scores, text=f"Your score: {user_score}", bg='light pink', fg='black', font=('Helvetica', 12))
label_user_score.pack(side=tk.LEFT, padx=10)

label_computer_score = tk.Label(frame_scores, text=f"Computer's score: {computer_score}", bg='light pink', fg='black', font=('Helvetica', 12))
label_computer_score.pack(side=tk.LEFT, padx=10)

tk.Button(root, text="Play Again", command=play_again).pack(pady=20)

# Run the main event loop
root.mainloop()
