"""
This Python exam will involve implementing a system for managing expenses.  You will
download the skeleton of the program, then implement the functions/methods.  The design of the
program has been set up for you.

In this system, users will be able to add and deduct expenses, update expenses, sort expenses,
and export filtered expenses to a file.  The program will initially load a collection of expenses
from 2 different .txt files (in the same format) and store them as Expense objects in a dictionary.

NOTE(S):
- It is important that you DO NOT edit the expenses.txt file or the expenses_2.txt file.  If you do,
you could fail the automated testing.
- DO NOT change the spacing or remove any blank lines.
- DO NOT copy/paste the text from the expenses.txt file or the expenses_2.txt file into another file.
"""

from ExpensesLoader import *
from ExpensesManager import *


def main():
    # To store dictionary of expenses
    expenses = {}

    # Create instance of ExpensesLoader class
    expenses_loader = ExpensesLoader()

    # Call import_expenses method in ExpensesLoader class
    # to import expense files and store in dictionary
    expenses_loader.import_expenses(expenses, 'expenses.txt')
    expenses_loader.import_expenses(expenses, 'expenses_2.txt')

    # For testing purposes, uncomment the following line
    print(expenses)

    # Create instance of ExpensesManager class
    expenses_manager = ExpensesManager()

    while True:

        # Print welcome and options
        print('\nWelcome to the expense management system!  What would you like to do?')
        print('1: Get expense info')
        print('2: Add an expense')
        print('3: Deduct an expense')
        print('4: Update an expense')
        print('5: Sort expenses')
        print('6: Export expenses')
        print('0: Exit the system')

        # Get user input
        option_input = input('\n')

        # Try and cast to int
        try:
            option = int(option_input)

        # Catch ValueError
        except ValueError:
            print("Invalid option.")

        else:

            # Check options
            if (option == 1):

                # Get expense type and print expense info
                expense_type = input('Expense type? ')

                # Call get_expense method in ExpensesManager class
                print(expenses_manager.get_expense(expenses, expense_type))

            elif (option == 2):

                # Get expense type
                expense_type = input('Expense type? ')

                # Try and get amount to add and cast to float
                try:
                    amount = float(input('Amount to add? '))

                # Catch ValueError
                except ValueError:
                    print("Invalid amount.")

                else:
                    # Add expense
                    # Call add_expense method in ExpensesManager class
                    expenses_manager.add_expense(expenses, expense_type, amount)

            elif (option == 3):

                # Get expense type
                expense_type = input('Expense type? ')

                # Try and get amount to deduct and cast to float
                try:
                    amount = float(input('Amount to deduct? '))

                # Catch ValueError
                except ValueError:
                    print("Invalid amount.")

                else:
                    # Deduct expense
                    # Call deduct_expense method in ExpensesManager class
                    expenses_manager.deduct_expense(expenses, expense_type, amount)

            elif (option == 4):

                # Get expense type
                expense_type = input('Expense type? ')

                # Try and get amount to update expense to
                try:
                    amount = float(input('Amount to update expense to? '))

                # Catch ValueError
                except ValueError:
                    print("Invalid amount.")

                else:
                    # Update expense
                    # Call update_expense method in ExpensesManager class
                    expenses_manager.update_expense(expenses, expense_type, amount)

            elif (option == 5):

                # Get sort type
                sort_type = input('What type of sort? (\'expense_type\' or \'amount\') ')

                # Sort expenses
                # Call sort_expenses method in ExpensesManager class
                print(expenses_manager.sort_expenses(expenses, sort_type))

            elif (option == 6):

                # Get filename to export to
                file_name = input('Name of file to export to?')

                # Get expense types to export
                expense_types = []

                while True:
                    expense_type = input("What expense type you want to export? Input N to quit: ")
                    if expense_type == "N":
                        break

                    expense_types.append(expense_type)

                # Export expenses
                # Call export_expenses method in ExpensesManager class
                expenses_manager.export_expenses(expenses, expense_types, file_name)

            elif (option == 0):

                # Exit expense system
                print('Good bye!')
                break

            # Corner case
            else:
                print("Invalid option.")


if __name__ == '__main__':
    main()
