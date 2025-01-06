
# Personal Expense Tracker

A Python tool to manage, analyze, and visualize expenses. I have included four different tools for personal expense tracking built in python. This project was created for me to revisit python3 coding.
- expense_tracker.py: Simple expense tracker where you can add, view and summarize expenses. You can save/load csv files by specifying the file name. Also has the option to filter by date and visulize expenses in pie/bar charts.
- expense_tracker_singlefile.py: Similar to 'expense_tracker.py' but you do not need to specify any particular file to load and save expenses. It will automatically create(if not present) and add expenses to expenses.csv file in the same filepath.
- expense_tracker_gui.py: Has a similar functionality as the 'expense_tracker.py' but in GUI tool rather than command line.
- expense_tracker_gui_singlefile.py: Combines the funtionality of the above two. Uses a single csv file for expense tracking with a GUI functionality.

## Features
- Add, view, and summarize expenses.
- Save/load CSV files(expense_tracker.py/expense_tracker_gui.py). 
- Filter by date.
- Bar and pie chart visualizations.
- GUI functionality (expense_tracker_gui.py/expense_tracker_gui_singlefile.py)

## Setup
Install dependencies:
```bash
pip install tabulate matplotlib
```
Run the script:
```bash
python expense_tracker.py
```

## Requirements

-   Python 3.7+
-   `tabulate`, `matplotlib`

## License

[MIT](https://github.com/nirajdsouza/personal-expense-project-python/blob/main/LICENSE) License