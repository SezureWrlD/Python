def show_history(self):
    history_window = tk.Toplevel(self.window)
    history_window.title("Answer History")

    for i, answer in enumerate(self.user_answers):
        label = tk.Label(history_window, text=f"Question {i + 1}: {answer}")
        label.pack()

    def show_history(self):
        history_window = tk.Toplevel(self.window)
        history_window.title("Answer History")

        for i, answer in enumerate(self.user_answers):
            label = tk.Label(history_window, text=f"Question {i+1}: {answer}")
            label.pack()

    def show_history(self):
        history_window = tk.Toplevel(self.window)
        history_window.title("Answer History")

        for i, answer in enumerate(self.user_answers):
            label = tk.Label(history_window, text=f"Question {i+1}: {answer}")
            label.pack()