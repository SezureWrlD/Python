def check_answer(self):
    selected_answer = self.answer_var.get()
    if selected_answer:
        question = self.questions[self.current_question_index]
        user_answer = question["options"][int(selected_answer) - 1]
        self.user_answers.append(user_answer)
        self.current_question_index += 1
        self.next_question()
    else:
        messagebox.showwarning("No Answer", "Please select an answer!")

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