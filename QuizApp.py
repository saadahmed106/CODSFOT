import tkinter as tk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "correct_option": 0
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Mercury"],
                "correct_option": 0
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct_option": 1
            }
            # Add more questions here
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(padx=10, pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(padx=5, pady=5)

        self.next_question_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_question_button.pack(padx=10, pady=10)

        self.score_label = tk.Label(root, text="")
        self.score_label.pack(padx=10, pady=10)

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            options = question_data["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])

        else:
            self.question_label.config(text="Quiz completed!")
            self.next_question_button.config(state=tk.DISABLED)
            self.score_label.config(text=f"Your score: {self.score}/{len(self.questions)}")

    def check_answer(self, selected_option):
        correct_option = self.questions[self.current_question]["correct_option"]
        if selected_option == correct_option:
            self.score += 1
        self.current_question += 1
        self.load_question()

    def next_question(self):
        self.current_question += 1
        self.load_question()

root = tk.Tk()
quiz_app = QuizApp(root)
root.mainloop()

