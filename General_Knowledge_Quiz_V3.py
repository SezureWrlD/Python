import tkinter as tk
from tkinter import messagebox
import csv

class QuizApp:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.user_answers = []
        self.build_gui()

    def build_gui(self):
        self.window = tk.Tk()
        self.window.title("General Knowledge Quiz")

        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack(pady=10)

        self.answer_var = tk.StringVar()

        self.option1 = tk.Radiobutton(self.window, text="", variable=self.answer_var, value=1)
        self.option1.pack(pady=5, anchor="w")

        self.option2 = tk.Radiobutton(self.window, text="", variable=self.answer_var, value=2)
        self.option2.pack(pady=5, anchor="w")

        self.option3 = tk.Radiobutton(self.window, text="", variable=self.answer_var, value=3)
        self.option3.pack(pady=5, anchor="w")

        self.check_button = tk.Button(self.window, text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=10)

        self.history_button = tk.Button(self.window, text="History", command=self.show_history)
        self.history_button.pack(pady=5)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question["question"])
            self.option1.config(text=question["options"][0])
            self.option2.config(text=question["options"][1])
            self.option3.config(text=question["options"][2])
            self.answer_var.set(None)
        else:
            messagebox.showinfo("Quiz Completed", "You have completed the quiz!")
            self.window.destroy()

    def check_answer(self):
        selected_answer = self.answer_var.get()
        if selected_answer:
            question = self.questions[self.current_question_index]
            user_answer = question["options"][int(selected_answer)-1]
            self.user_answers.append(user_answer)
            self.current_question_index += 1
            self.next_question()
        else:
            messagebox.showwarning("No Answer", "Please select an answer!")

    def show_history(self):
        history_window = tk.Toplevel(self.window)
        history_window.title("Answer History")

        for i, answer in enumerate(self.user_answers):
            label = tk.Label(history_window, text=f"Question {i+1}: {answer}")
            label.pack()

# Quiz Questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin"],
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Venus"],
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"],
    },
    {
        "question": "Which animal is known as the 'King of the Jungle'?",
        "options": ["Lion", "Elephant", "Tiger"],
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["Mount Everest", "K2", "Makalu"],
    },
]
import tkinter as tk
from tkinter import messagebox
import csv

class QuizApp:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.user_answers = []
        self.build_gui()

    def build_gui(self):
        self.window = tk.Tk()
        self.window.title("General Knowledge Quiz")

        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack(pady=10)

        self.answer_var = tk.StringVar()

        self.option1 = tk.Radiobutton(self.window, text="", variable=self.answer_var, value=1)
        self.option1.pack(pady=5, anchor="w")

        self.option2 = tk.Radiobutton(self.window, text="", variable=self.answer_var, value=2)
        self.option2.pack(pady=5, anchor="w")

        self.option3 = tk.Radiobutton(self.window, text="", variable=self.answer_var, value=3)
        self.option3.pack(pady=5, anchor="w")

        self.check_button = tk.Button(self.window, text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=10)

        self.history_button = tk.Button(self.window, text="History", command=self.show_history)
        self.history_button.pack(pady=5)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question["question"])
            self.option1.config(text=question["options"][0])
            self.option2.config(text=question["options"][1])
            self.option3.config(text=question["options"][2])
            self.answer_var.set(None)
        else:
            messagebox.showinfo("Quiz Completed", "You have completed the quiz!")
            self.window.destroy()

    def check_answer(self):
        selected_answer = self.answer_var.get()
        if selected_answer:
            question = self.questions[self.current_question_index]
            user_answer = question["options"][int(selected_answer)-1]
            self.user_answers.append(user_answer)
            self.current_question_index += 1
            self.next_question()
        else:
            messagebox.showwarning("No Answer", "Please select an answer!")

    def show_history(self):
        history_window = tk.Toplevel(self.window)
        history_window.title("Answer History")

        for i, answer in enumerate(self.user_answers):
            label = tk.Label(history_window, text=f"Question {i+1}: {answer}")
            label.pack()

# Quiz Questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin"],
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Venus"],
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"],
    },
    {
        "question": "Which animal is known as the 'King of the Jungle'?",
        "options": ["Lion", "Elephant", "Tiger"],
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["Mount Everest", "K2", "Makalu"],
    },
]

# Create the Quiz App
quiz_app = QuizApp(quiz_questions)

# Create the Quiz App
quiz_app = QuizApp(quiz_questions)
