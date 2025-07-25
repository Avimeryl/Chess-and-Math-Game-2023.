# Modification to create the math questions
import random
import tkinter as tk
from tkinter import ttk

class MathQuizGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Math Blaster")

        # Set window size
        window_width = 400
        window_height = 300

        # Calculate the center coordinates of the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.equation_label = ttk.Label(self.root, font=("Arial", 14))
        self.equation_label.pack(pady=10)

        self.operator1_entry = ttk.Entry(self.root, font=("Arial", 12))
        self.operator1_entry.pack(pady=5)

        self.operator2_entry = ttk.Entry(self.root, font=("Arial", 12))
        self.operator2_entry.pack(pady=5)

        self.submit_button = ttk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.question_counter = 0
        self.remaining_time = 20
        self.timer_expired = False
        self.timer_label = ttk.Label(self.root, font=("Arial", 12), foreground="blue")
        self.timer_label.pack(pady=10)
        self.timer_id = None
        self.result_label = None
        self.is_correct = None

    def generate_equation(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)

        operator1 = random.choice(['+', '-', '*'])
        operator2 = random.choice(['+', '-', '*'])

        if operator1 == '+':
            intermediate_result = num1 + num2
        elif operator1 == '-':
            intermediate_result = num1 - num2
        else:
            intermediate_result = num1 * num2

        if operator2 == '+':
            answer = intermediate_result + num3
        elif operator2 == '-':
            answer = intermediate_result - num3
        else:
            answer = intermediate_result * num3

        equation = f"{num1} ? {num2} ? {num3} = {answer}"
        visible_equation = equation.replace('?', ' ')
        self.equation_label.configure(text=f"Equation: {visible_equation}")

        # Clear the entry fields
        self.operator1_entry.delete(0, tk.END)
        self.operator2_entry.delete(0, tk.END)

        self.correct_operators = f"{operator1} {operator2}"

        # Start the timer
        self.remaining_time = 20
        self.update_timer_label()
        self.timer_id = self.root.after(1000, self.timer_callback)

    def update_timer_label(self):
        self.timer_label.configure(text=f"Time Remaining: {self.remaining_time} seconds")

    def timer_callback(self):
        self.remaining_time -= 1
        if self.remaining_time >= 0:
            self.update_timer_label()
            self.timer_id = self.root.after(1000, self.timer_callback)
        else:
            self.timer_expired = True
            self.check_answer()

    def check_answer(self):
        self.root.after_cancel(self.timer_id)
        if self.timer_expired:
            result = "Time's up!"
            self.timer_expired = False
            self.is_correct = False
        else:
            user_operator1 = self.operator1_entry.get()
            user_operator2 = self.operator2_entry.get()
            if user_operator1 == self.correct_operators.split()[0] and user_operator2 == self.correct_operators.split()[1]:
                result = "Correct!"
                self.is_correct = True
            else:
                result = f"Wrong! The correct operators were: {self.correct_operators}."
                self.is_correct = False
        self.root.after(500, self.root.destroy)

        # Remove existing result label
        if self.result_label:
            self.result_label.pack_forget()

        self.result_label = ttk.Label(self.root, text=result, font=("Arial", 12))
        self.result_label.pack(pady=10)

    def run(self):
        self.generate_equation()
        self.root.mainloop()
        print(self.is_correct)
        return self.is_correct

# quiz = MathQuizGUI()
# quiz.run()
