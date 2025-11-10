import tkinter as tk
from tkinter import messagebox

# --- Quiz Data ---
quiz_data = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Switzerland": "Bern",
    "Austria": "Vienna"
}

# --- Main App Setup ---
root = tk.Tk()
root.title("🌍 European Capitals Quiz")
root.geometry("500x300")
root.config(bg="#e0f7fa")

# --- Variables ---
countries = list(quiz_data.keys())
index = 0
score = 0

# --- Widgets ---
title_label = tk.Label(root, text="European Capitals Quiz", font=("Arial", 18, "bold"), bg="#e0f7fa", fg="#00695c")
title_label.pack(pady=20)

question_label = tk.Label(root, text="", font=("Arial", 14), bg="#e0f7fa")
question_label.pack(pady=10)

answer_entry = tk.Entry(root, font=("Arial", 14))
answer_entry.pack(pady=10)

feedback_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#e0f7fa", fg="#004d40")
feedback_label.pack(pady=5)

next_button = tk.Button(root, text="Submit", font=("Arial", 12, "bold"), bg="#00897b", fg="white", command=lambda: check_answer())
next_button.pack(pady=20)

# --- Functions ---
def show_question():
    """Display the current question."""
    global index
    if index < len(countries):
        question_label.config(text=f"What is the capital of {countries[index]}?")
        feedback_label.config(text="")
        answer_entry.delete(0, tk.END)
    else:
        show_result()

def check_answer():
    """Check the user's answer and give feedback."""
    global index, score
    user_answer = answer_entry.get().strip().lower()
    correct_answer = quiz_data[countries[index]].lower()

    if user_answer == correct_answer:
        feedback_label.config(text="✅ Correct!", fg="green")
        score += 1
    else:
        feedback_label.config(text=f"❌ Wrong! The correct answer is {quiz_data[countries[index]]}.", fg="red")

    index += 1
    root.after(1500, show_question)  # Wait 1.5 seconds, then show next question

def show_result():
    """Display the final score."""
    messagebox.showinfo("Quiz Complete", f"You got {score} out of {len(quiz_data)} correct!")
    root.destroy()

# --- Start Quiz ---
show_question()
root.mainloop()
