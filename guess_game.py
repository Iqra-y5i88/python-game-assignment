import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number Game")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="I'm thinking of a number between 1 and 100.")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result_label.config(text="Too low!")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high!")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} tries!")
                self.ask_play_again()
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def ask_play_again(self):
        play_again = messagebox.askyesno("Play Again?", "Would you like to play again?")
        if play_again:
            self.reset_game()
        else:
            self.master.quit()

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()

#Created by "25032215 at Keele University"
