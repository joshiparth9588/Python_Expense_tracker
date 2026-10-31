import tkinter as tk
from tkinter import messagebox
import json
import os

# Main Window
root = tk.Tk()
root.title("Python Expense Tracker")
root.geometry("800x600")

# Heading
heading = tk.Label(
    root,
    text="EXPENSE TRACKER",
    font=("Arial", 22, "bold")
)
heading.pack(pady=20)

# Amount Input
amount_label = tk.Label(root, text="Enter Amount:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

# Category Input
category_label = tk.Label(root, text="Enter Category:")
category_label.pack()

category_entry = tk.Entry(root)
category_entry.pack()


# Add Expense Function
def add_expense():
    amount = amount_entry.get().strip()
    category = category_entry.get().strip()

    # Check Empty Fields
    if amount == "" or category == "":
        messagebox.showwarning(
            "Warning",
            "Please fill all fields!"
        )
        return

    # Check Amount
    try:
        amount = float(amount)

        if amount <= 0:
            messagebox.showwarning(
                "Warning",
                "Enter a valid amount!"
            )
            return

    except ValueError:
        messagebox.showwarning(
            "Warning",
            "Amount must be a number!"
        )
        return

    # Expense Data
    expense = {
        "amount": amount,
        "category": category
    }

    # Read Existing Expenses
    try:
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                expenses = json.load(file)
        else:
            expenses = []

    except (json.JSONDecodeError, OSError):
        expenses = []

    # Add New Expense
    expenses.append(expense)

    # Save Expenses
    try:
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense Saved!")

        messagebox.showinfo(
            "Success",
            "Expense Saved Successfully!"
        )

        # Clear Input Boxes
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)

    except OSError as error:
        messagebox.showerror(
            "Error",
            f"Could not save expense: {error}"
        )


# Add Expense Button
add_button = tk.Button(
    root,
    text="Add Expense",
    command=add_expense
)
add_button.pack(pady=10)


# Run Application
root.mainloop()