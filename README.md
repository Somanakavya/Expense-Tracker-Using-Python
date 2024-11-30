# Expense Tracker Using Python and Tkinter

A simple Python-based Expense Tracker application with a GUI for logging, managing, and visualizing expenses. The project uses **Tkinter** for the user interface, **Matplotlib** for data visualization, and **CSV** for storing expense data.

---

## Features
- **Log Expenses:** Add expenses with fields for date, category, amount, and description.
- **View Summary:** Display a summary of total expenses and breakdown by categories.
- **Filter by Date Range:** Filter expenses between specific start and end dates.
- **Visualize Expenses:** 
  - Bar chart for expenses by date.
  - Pie chart for expenses by category.
- **User-Friendly Interface:** Built with Tkinter for smooth interaction.

---

## Installation

### Prerequisites
- Python 3.x
- Required libraries: `matplotlib`, `tkinter`

### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/expense-tracker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd expense-tracker
    ```
3. Install required dependencies (if not already installed):
    ```bash
    pip install matplotlib
    ```

---

## Usage

### Running the Application
1. Run the Python script:
    ```bash
    python expense_tracker.py
    ```
2. The GUI window will open.

---

## Application Overview

### GUI Layout
1. **Log Expenses**:  
   - Enter the date (YYYY-MM-DD), category, amount, and description, then click "Log Expense."
2. **Display Summary**:  
   - Click "Display Summary" to view the total amount spent and breakdown by category.
3. **Visualize All Expenses**:  
   - Click "Visualize All Expenses" to see bar and pie charts.
4. **Filter and Visualize by Date Range**:  
   - Enter a start and end date, then click "Filter and Visualize Expenses."

---

## Visualization Examples
- **Bar Chart**: Displays expenses by date.
- **Pie Chart**: Shows category-wise expense distribution.

---

## File Structure
- **`expenses.csv`**: Stores logged expenses (created automatically).
- **`expense_tracker.py`**: Main Python file containing the application code.
