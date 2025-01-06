import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from datetime import datetime
import csv
import matplotlib.pyplot as plt

# Initialize the expense list
expenses = []

# Function to add a new expense
def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    date = date_entry.get()

    try:
        # Validate amount and date
        amount = float(amount)
        datetime.strptime(date, "%Y-%m-%d")

        # Add expense to the list
        expenses.append({"Category": category, "Amount": amount, "Date": date})
        messagebox.showinfo("Success", "Expense added successfully!")
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid amount or date format. Please try again.")

# Function to view all expenses
def view_expenses():
    if not expenses:
        messagebox.showinfo("Info", "No expenses to display.")
        return

    # Create a new window to display expenses
    view_window = tk.Toplevel()
    view_window.title("View Expenses")

    columns = ("Category", "Amount", "Date")
    tree = ttk.Treeview(view_window, columns=columns, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    for col in columns:
        tree.heading(col, text=col)

    for expense in expenses:
        tree.insert("", tk.END, values=(expense["Category"], expense["Amount"], expense["Date"]))

# Function to filter expenses by date
def filter_expenses_by_date():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    try:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

        filtered_expenses = [
            expense for expense in expenses
            if start_date_obj <= datetime.strptime(expense["Date"], "%Y-%m-%d") <= end_date_obj
        ]

        if not filtered_expenses:
            messagebox.showinfo("Info", "No expenses found in the given date range.")
            return

        # Create a new window to display filtered expenses
        filter_window = tk.Toplevel()
        filter_window.title("Filtered Expenses")

        columns = ("Category", "Amount", "Date")
        tree = ttk.Treeview(filter_window, columns=columns, show="headings")
        tree.pack(fill=tk.BOTH, expand=True)

        for col in columns:
            tree.heading(col, text=col)

        for expense in filtered_expenses:
            tree.insert("", tk.END, values=(expense["Category"], expense["Amount"], expense["Date"]))

    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")

# Function to plot expenses
def plot_expenses():
    if not expenses:
        messagebox.showinfo("Info", "No expenses to plot.")
        return

    # Summarize expenses by category
    summary = {}
    for expense in expenses:
        category = expense["Category"]
        amount = expense["Amount"]
        summary[category] = summary.get(category, 0) + amount

    # Extract data for plotting
    categories = list(summary.keys())
    amounts = list(summary.values())

    # Plot bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts, color="skyblue")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Expenses by Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to save expenses to a file
def save_to_file():
    if not expenses:
        messagebox.showinfo("Info", "No expenses to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Category", "Amount", "Date"])
            writer.writeheader()
            writer.writerows(expenses)
        messagebox.showinfo("Success", "Expenses saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")

# Function to load expenses from a file
def load_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["Amount"] = float(row["Amount"])
                expenses.append(row)
        messagebox.showinfo("Success", "Expenses loaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file: {e}")

# Main GUI Window
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("500x500")

# Add Expense Section
tk.Label(root, text="Add Expense").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Category:").grid(row=1, column=0, sticky=tk.E)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

tk.Label(root, text="Amount:").grid(row=2, column=0, sticky=tk.E)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1)

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=3, column=0, sticky=tk.E)
date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=4, column=0, columnspan=2, pady=10)

# View and Filter Section
tk.Button(root, text="View All Expenses", command=view_expenses).grid(row=5, column=0, columnspan=2, pady=10)

tk.Label(root, text="Filter Expenses by Date").grid(row=6, column=0, columnspan=2, pady=10)

tk.Label(root, text="Start Date:").grid(row=7, column=0, sticky=tk.E)
start_date_entry = tk.Entry(root)
start_date_entry.grid(row=7, column=1)

tk.Label(root, text="End Date:").grid(row=8, column=0, sticky=tk.E)
end_date_entry = tk.Entry(root)
end_date_entry.grid(row=8, column=1)

tk.Button(root, text="Filter Expenses", command=filter_expenses_by_date).grid(row=9, column=0, columnspan=2, pady=10)

# Save and Load Section
tk.Button(root, text="Save Expenses to File", command=save_to_file).grid(row=10, column=0, columnspan=2, pady=10)
tk.Button(root, text="Load Expenses from File", command=load_from_file).grid(row=11, column=0, columnspan=2, pady=10)

# Plot Section
tk.Button(root, text="Plot Expenses", command=plot_expenses).grid(row=12, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
