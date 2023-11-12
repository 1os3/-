import tkinter as tk
from tkinter import messagebox
import random

class ArithmeticGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("加减法算术游戏")
        self.geometry("600x400")

        self.level = 0
        self.current_question = 0
        self.questions_per_level = 100
        self.operations = ['+', '-', '*', '/']
        self.level_ranges = [(0, 100), (0, 200), (0, 300), (0, 400), (0, 500)]  # 每个关卡的数值范围

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="在这里输入问题", font=("Arial", 24))
        self.label.pack(pady=20)

        self.entry = tk.Entry(self, font=("Arial", 24))
        self.entry.pack(pady=10)

        self.check_button = tk.Button(self, text="检查答案", command=self.check_answer, font=("Arial", 20))
        self.check_button.pack(pady=10)

        self.level_label = tk.Label(self, text=f"关卡: {self.level + 1}", font=("Arial", 16))
        self.level_label.pack()

        self.generate_question()

    def generate_question(self):
        a = random.randint(*self.level_ranges[self.level])
        b = random.randint(*self.level_ranges[self.level])
        operation = random.choice(self.operations)
        if operation == '/':
            # Avoid division by zero
            while b == 0:
                b = random.randint(*self.level_ranges[self.level])

        question = f"{a} {operation} {b}"
        self.label.config(text=question)
        self.expected_answer = str(eval(question))

        time_to_answer = random.randint(5, 10)
        self.after(time_to_answer * 1000, self.generate_question)

    def check_answer(self):
        user_answer = self.entry.get()
        if user_answer == self.expected_answer:
            self.current_question += 1
            if self.current_question == self.questions_per_level:
                self.level += 1
                self.current_question = 0
                self.level_label.config(text=f"关卡: {self.level + 1}")
                messagebox.showinfo("恭喜", "你已通过本关，进入下一关！")
            self.entry.delete(0, 'end')
            self.generate_question()
        else:
            messagebox.showerror("错误", "答案不正确，请再试一次！")

if __name__ == "__main__":
    app = ArithmeticGame()
    app.mainloop()