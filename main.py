import json
from datetime import datetime
import matplotlib.pyplot as plt

class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, date):
        expense = Expense(amount, category, date)
        self.expenses.append(expense)

    def save_expenses(self, filename):
        with open(filename, 'w') as file:
            json.dump([vars(expense) for expense in self.expenses], file)

    def load_expenses(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.expenses = [Expense(expense['amount'], expense['category'], expense['date']) for expense in data]

    def plot_spending_over_time(self):
        categories = {}
        for expense in self.expenses:
            if expense.category not in categories:
                categories[expense.category] = []
            categories[expense.category].append(expense.amount)

        for category, amounts in categories.items():
            dates = [datetime.strptime(expense.date, '%Y-%m-%d') for expense in self.expenses if expense.category == category]
            plt.plot(dates, amounts, label=category)

        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title('Spending Over Time')
        plt.legend()
        plt.show()

def main():
    tracker = ExpenseTracker()

    # Load existing expenses from file
    tracker.load_expenses('expenses.json')

    while True:
        print("\nExpense Tracking System")
        print("1. Add Expense")
        print("2. View Spending Patterns Over Time")
        print("3. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            tracker.add_expense(amount, category, date)
        elif choice == "2":
            tracker.plot_spending_over_time()
        elif choice == "3":
            tracker.save_expenses('expenses.json')
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
