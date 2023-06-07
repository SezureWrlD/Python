def export_results(self):
    filename = "quiz_results.csv"
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Question", "Answer"])
            for i, question in enumerate(self.questions):
                writer.writerow([question["question"], self.user_answers[i]])
        messagebox.showinfo("Export Successful", "Quiz results exported to 'quiz_results.csv'")
    except Exception as e:
        messagebox.showerror("Export Error", f"An error occurred while exporting the quiz results:\n{e}")

    def export_results(self):
        filename = 'quiz_results'
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Question", "Answer"])
                for i, question in enumerate(self.questions):
                    writer.writerow([question["question"], self.user_answers[i]])
            messagebox.showinfo("Export Successful", "Quiz results exported to 'quiz_results'")
        except Exception as e:
            messagebox.showerror("Export Error", f"An error occurred while exporting the quiz results:\n{e}")