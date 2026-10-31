import json
import os
from datetime import date


# Expense Class
class Expense:

    def __init__(self, amount, category, note):
        self.amount = amount
        self.category = category
        self.note = note
        self.expense_date = str(date.today())

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "note": self.note,
            "date": self.expense_date
        }


# Expense Tracker Class
class ExpenseTracker:

    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    # Load Expenses
    def load_expenses(self):

        if os.path.exists(self.filename):

            try:
                with open(self.filename, "r") as file:
                    return json.load(file)

            except json.JSONDecodeError:
                return []

        return []

    # Save Expenses
    def save_expenses(self):

        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    # Add Expense
    def add_expense(self):

        try:
            amount = float(input("Enter amount: Rs."))

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

            category = input("Enter category: ")
            note = input("Enter note: ")

            expense = Expense(amount, category, note)

            self.expenses.append(expense.to_dict())

            self.save_expenses()

            print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid amount.")

    # View Expenses
    def view_expenses(self):

        if not self.expenses:
            print("No expenses found.")
            return

        print("\n--- ALL EXPENSES ---")

        for index, expense in enumerate(self.expenses, start=1):

            print(
                f"{index}. Rs.{expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['note']} | "
                f"{expense['date']}"
            )

    # Total Expenses
    def total_expenses(self):

        total = sum(
            expense["amount"] for expense in self.expenses
        )

        print(f"Total Expense: Rs.{total:.2f}")

    # Category Summary
    def category_summary(self):

        summary = {}

        for expense in self.expenses:

            category = expense["category"]
            amount = expense["amount"]

            summary[category] = summary.get(category, 0) + amount

        print("\n--- CATEGORY SUMMARY ---")

        for category, amount in summary.items():

            print(f"{category}: Rs.{amount:.2f}")

    # Delete Expense
    def delete_expense(self):

        self.view_expenses()

        if not self.expenses:
            return

        try:
            number = int(input("Enter expense number to delete: "))

            if 1 <= number <= len(self.expenses):

                removed = self.expenses.pop(number - 1)

                self.save_expenses()

                print(
                    f"Deleted expense: Rs.{removed['amount']:.2f}"
                )

            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")


# Main Function
def main():

    tracker = ExpenseTracker()

    while True:

        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.total_expenses()

        elif choice == "4":
            tracker.category_summary()

        elif choice == "5":
            tracker.delete_expense()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()