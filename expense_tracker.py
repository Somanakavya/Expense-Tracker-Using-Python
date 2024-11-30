import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
from tkinter import ttk

# Define the file name for storing expenses
EXPENSE_FILE = 'expenses.csv'

# Function to log an expense
def log_expense(date, category, amount, description):
    with open(EXPENSE_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
        print(f"Logged expense: {date}, {category}, {amount}, {description}")

# Function to read all expenses
def read_expenses():
    expenses = []
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:  # Ensure each row has exactly 4 columns
                    expenses.append(row)
    return expenses

# Function to display summary
def display_summary():
    expenses = read_expenses()
    summary = {}
    total_amount = 0
    for expense in expenses:
        category = expense[1]
        amount = float(expense[2])
        total_amount += amount
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    for category, total in summary.items():
        print(f"{category}: Rs. {total:.2f}/-")
    return total_amount

# Function to filter expenses by date range
def filter_expenses(start_date, end_date):
    expenses = read_expenses()
    filtered_expenses = []
    for expense in expenses:
        date = datetime.strptime(expense[0], "%Y-%m-%d")
        if start_date <= date <= end_date:
            filtered_expenses.append(expense)
    return filtered_expenses

# Function to visualize expenses
def visualize_expenses(expenses, title='Expenses Visual'):
    # Prepare data for bar chart (Date and Price)
    dates = [expense[0] for expense in expenses]
    amounts = [float(expense[2]) for expense in expenses]

    # Prepare data for pie chart (Category and Price)
    category_summary = {}
    for expense in expenses:
        category = expense[1]
        amount = float(expense[2])
        if category in category_summary:
            category_summary[category] += amount
        else:
            category_summary[category] = amount
    categories = list(category_summary.keys())
    amounts_by_category = list(category_summary.values())

    # Create bar chart
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(dates, amounts, color='skyblue')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Expenses by Date')
    plt.xticks(rotation=45)

    # Create pie chart
    plt.subplot(1, 2, 2)
    plt.pie(amounts_by_category, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category')

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

# Function to create a GUI for input and displaying the summary card
def create_gui():
    root = Tk()
    root.title("Expense Tracker")
    root.geometry("400x500")
    
    # Title Card
    title_label = Label(root, text="Expenses Tracker", font=("Helvetica", 16))
    title_label.pack(pady=10)

    # Input fields
    frame = ttk.Frame(root, padding="10")
    frame.pack(pady=10)

    date_label = Label(frame, text="Date (YYYY-MM-DD)")
    date_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    date_entry = Entry(frame)
    date_entry.grid(row=0, column=1, padx=5, pady=5)

    category_label = Label(frame, text="Category")
    category_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    category_entry = Entry(frame)
    category_entry.grid(row=1, column=1, padx=5, pady=5)

    amount_label = Label(frame, text="Amount")
    amount_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    amount_entry = Entry(frame)
    amount_entry.grid(row=2, column=1, padx=5, pady=5)

    description_label = Label(frame, text="Description")
    description_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    description_entry = Entry(frame)
    description_entry.grid(row=3, column=1, padx=5, pady=5)

    # Log Expense Button
    def log_expense_gui():
        date = date_entry.get()
        category = category_entry.get()
        amount = amount_entry.get()
        description = description_entry.get()
        if not date or not category or not amount:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return
        try:
            datetime.strptime(date, "%Y-%m-%d")
            float(amount)
        except ValueError:
            messagebox.showwarning("Input Error", "Invalid date or amount format.")
            return
        log_expense(date, category, amount, description)
        date_entry.delete(0, 'end')
        category_entry.delete(0, 'end')
        amount_entry.delete(0, 'end')
        description_entry.delete(0, 'end')
        print("Expense logged and fields cleared")

    log_button = Button(frame, text="Log Expense", command=log_expense_gui)
    log_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Display Summary Button
    total_amount_var = StringVar()
    total_amount_var.set(f"Total Amount Spent: Rs. 0.00/-")

    def display_summary_gui():
        total_amount = display_summary()
        total_amount_var.set(f"Total Amount Spent: Rs. {total_amount:.2f}/-")
        print(f"Total amount calculated: Rs. {total_amount:.2f}/-")

    summary_button = Button(frame, text="Display Summary", command=display_summary_gui)
    summary_button.grid(row=5, column=0, columnspan=2)

    # Total Amount Card
    total_label = Label(root, textvariable=total_amount_var, font=("Helvetica", 14))
    total_label.pack(pady=10)

    # Visualize Button
    visualize_button = Button(root, text="Visualize All Expenses", command=lambda: visualize_expenses(read_expenses()))
    visualize_button.pack(pady=5)

    # Date Range Inputs for Filtering
    date_range_frame = ttk.Frame(root, padding="10")
    date_range_frame.pack(pady=10)

    start_date_label = Label(date_range_frame, text="Start Date (YYYY-MM-DD)")
    start_date_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    start_date_entry = Entry(date_range_frame)
    start_date_entry.grid(row=0, column=1, padx=5, pady=5)

    end_date_label = Label(date_range_frame, text="End Date (YYYY-MM-DD)")
    end_date_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    end_date_entry = Entry(date_range_frame)
    end_date_entry.grid(row=1, column=1, padx=5, pady=5)

    # Filter Expenses Button
    def filter_expenses_gui():
        start_date_str = start_date_entry.get()
        end_date_str = end_date_entry.get()
        if not start_date_str or not end_date_str:
            messagebox.showwarning("Input Error", "Please enter both start and end dates.")
            return
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Input Error", "Invalid date format.")
            return
        filtered_expenses = filter_expenses(start_date, end_date)
        visualize_expenses(filtered_expenses, title=f"Expenses from {start_date_str} to {end_date_str}")

    filter_button = Button(date_range_frame, text="Filter and Visualize Expenses", command=filter_expenses_gui)
    filter_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
