import csv
from datetime import datetime
from tabulate import tabulate
import matplotlib.pyplot as plt

# Initialize an empty list to store expenses
expenses = []

# Function to add a new expense
def add_expense():
    try:
        category = input("Enter category (e.g., Food, Transport): ")
        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD): ")

        # Validate date format
        datetime.strptime(date, "%Y-%m-%d")

        # Add the expense to the list
        expenses.append({"Category": category, "Amount": amount, "Date": date})
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid input. Please check the amount or date format.\n")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses to show.\n")
        return
    
    print(tabulate(expenses, headers="keys"))
    print()

# Function to summarize expenses by category
def view_summary():
    if not expenses:
        print("No expenses to summarize.\n")
        return

    summary = {}
    for expense in expenses:
        category = expense["Category"]
        amount = expense["Amount"]
        summary[category] = summary.get(category, 0) + amount

    # Display the summary
    print("Expense Summary:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")
    print(f"Total: ${sum(summary.values()):.2f}\n")

# Function to save expenses to a file
def save_to_file():
    filename = input("Enter filename to save (e.g., expenses.csv): ")
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Category", "Amount", "Date"])
            writer.writeheader()
            writer.writerows(expenses)
        print(f"Expenses saved to {filename} successfully!\n")
    except Exception as e:
        print(f"Error saving file: {e}\n")

# Function to load expenses from a file
def load_from_file():
    filename = input("Enter filename to load (e.g., expenses.csv): ")
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            global expenses
            expenses = list(reader)
            # Convert Amount to float for proper calculations
            for expense in expenses:
                expense["Amount"] = float(expense["Amount"])
        print(f"Expenses loaded from {filename} successfully!\n")
    except Exception as e:
        print(f"Error loading file: {e}\n")

def filter_expenses_by_date():
    if not expenses:
        print("No expenses to filter.\n")
        return

    try:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        # Convert strings to date objects for comparison
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

        # Filter expenses within the date range
        filtered_expenses = [
            expense for expense in expenses
            if start_date_obj <= datetime.strptime(expense["Date"], "%Y-%m-%d") <= end_date_obj
        ]

        # Display filtered expenses
        if filtered_expenses:
            print(tabulate(filtered_expenses, headers="keys", tablefmt="grid"))
        else:
            print("No expenses found in the given date range.\n")
    except ValueError:
        print("Invalid date format. Please try again.\n")

def plot_expenses():
    if not expenses:
        print("No expenses to plot.\n")
        return

    # Summarize expenses by category
    summary = {}
    for expense in expenses:
        category = expense["Category"]
        amount = expense["Amount"]
        summary[category] = summary.get(category, 0) + amount

    # Extract categories and amounts for plotting
    categories = list(summary.keys())
    amounts = list(summary.values())

    # Plot bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts, color='skyblue')
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Expenses by Category")
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout for better readability
    plt.show()

    # Optionally, ask if the user wants a pie chart
    choice = input("Do you want to see a pie chart as well? (yes/no): ").strip().lower()
    if choice == "yes":
        plt.figure(figsize=(8, 8))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title("Expenses by Category (Pie Chart)")
        plt.show()


# Main menu
def main():
    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Filter Expenses by Date")
        print("7. Plot Expenses")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            save_to_file()
        elif choice == "5":
            load_from_file()
        elif choice == "6":
            filter_expenses_by_date()
        elif choice == "7":
            plot_expenses()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
