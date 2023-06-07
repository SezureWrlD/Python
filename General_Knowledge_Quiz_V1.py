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

        self.export_button = tk.Button(self.window, text="Export Results", command=self.export_results)
        self.export_button.pack(pady=5)

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
