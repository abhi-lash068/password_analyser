
import tkinter as tk
from tkinter import messagebox
import re
import string

COMMON_PASSWORDS = {"password", "123456", "admin", "letmein", "qwerty", "welcome"}

def evaluate_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short. Use at least 8 characters.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Mix uppercase and lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[' + re.escape(string.punctuation) + ']', password):
        score += 1
    else:
        feedback.append("Include special characters (!@#$%^&* etc).")

    return score, feedback

def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS

def check_password_strength():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    score, feedback = evaluate_password(password)

    if is_common_password(password):
        feedback.append("Common password. Avoid dictionary words.")
        score = min(score, 2)

    if score >= 5:
        strength = "Strong"
        color = "green"
    elif score >= 3:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    result_label.config(text=f"Strength: {strength}", fg=color)

    feedback_text.delete("1.0", tk.END)
    if feedback:
        for tip in feedback:
            feedback_text.insert(tk.END, f"• {tip}\n")
    else:
        feedback_text.insert(tk.END, "Your password is strong and secure!")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry.pack()

tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

feedback_text = tk.Text(root, height=6, width=45, font=("Arial", 10))
feedback_text.pack(pady=5)

root.mainloop()
