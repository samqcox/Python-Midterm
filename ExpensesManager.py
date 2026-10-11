from Expense import *


class ExpensesManager(object):
    """A class for managing expenses in a dictionary.
    """

    # We do not have an __init__ function and will call the default constructor

    def get_expense(self, expenses, expense_type):
        """Returns the Expense object for the given expense type in the given expenses dictionary.

        Prints a friendly message and returns None if the expense type doesn't exist.

        (Note: Printing a friendly message means that the program should not raise an error or otherwise terminate.
        Simply tell the user that the requested expense type does not exist and continue the program.

        Also note that None is a specific keyword in Python of NoneType. You should not return a string “None” from
        this method.)
        """

        # TODO Insert your code

        #check if expense type exists, if not return none
        if expense_type not in expenses:

            # friendly message
            print("The requested expense type does not exist in the given expenses dictionary.")
            return None

        #return expense object
        return expenses[expense_type]

    def add_expense(self, expenses, expense_type, value):
        """If the expense_type already exists in the given expenses dictionary, add the value to the associated
        Expense object amount.

        Otherwise, create a new entry in the expenses dictionary with the expense_type as the
        key and the value as an Expense object with the given expense_type and value parameters.

        Prints the updated Expense object.

        This method doesn’t return anything.
        """

        # TODO Insert your code

        #check expense_type is in the dict
        if expense_type in expenses:

            #if it is add amount to expense type
            expenses[expense_type].add_amount(value)
        else:

            #otherwise create new entry in the dictionary
            expenses[expense_type] = Expense(expense_type, value)

        #print the updated expense object
        print(expenses[expense_type])


    def deduct_expense(self, expenses, expense_type, value):
        """From the given expenses dictionary, get the Expense object associated with the given expense_type and
        deduct the given value from the amount.

        Raises a RuntimeError if the given value is greater than the existing amount of the Expense object. Note: You
        are not supposed to use try/except to catch the RuntimeError you raised. We expect the method to raise a
        RuntimeError if the value is greater than the existing total of the expense type.

        Prints a friendly message if the expense type doesn't exist from the given expenses dictionary. (Note:
        Printing a friendly message means that the program should not raise an error or otherwise terminate. Simply
        tell the user that the requested expense type does not exist and continue the program.)

        Print the updated Expense object if RuntimeError is not raised.

        This method doesn’t return anything.
        """

        # TODO Insert your code

        #check if expense_type exists in dict
        if expense_type in expenses:

            #raise RuntimeError if the given value is greater than existing amount
            if value > expenses[expense_type].amount:
                raise RuntimeError

            else:
                # deduct amount from expense type
                expenses[expense_type].deduct_amount(value)
                #print updated expense type
                print(expenses[expense_type])

        else:
            # print friendly message if expense type does not exist
            print("The requested expense type does not exist")

    def update_expense(self, expenses, expense_type, value):
        """From the given expenses dictionary, update the Expense object associated with the given expense_type and
        use the given value.

        Prints a friendly message if the expense type doesn't exist.  Note: Printing a friendly message means that
        the program should not raise an error or otherwise terminate. Simply tell the user that the requested expense
        type does not exist and continue the program.

        Prints the updated Expense object if it exists.

        This method doesn’t return anything.
        """

        # TODO Insert your code
        #check if expense type is in dictionary
        if expense_type in expenses:
            #update the amount to given value
            expenses[expense_type].amount = value
            #print updated expense object if it exists
            print(expenses[expense_type])
        else:
            print("The requested expense type does not exist")


    def sort_expenses(self, expenses, sorting):
        """Converts the key:value pairs in the given expenses dictionary to a list of tuples containing the expense
        type and amount of the Expense object (Expense.expense_type, Expense.amount) and sorts based on the given
        sorting argument.

        If the sorting argument is the string ‘expense_type’, sorts the list of tuples based on the expense type
        (e.g. ‘rent’) in ascending alphabetical order of the expense_type, e.g. sorted results: ("coffee", 5.0),
        ("food", 5000.0), ("rent", 1000.0)

        Otherwise, if the sorting argument is ‘amount’, sorts the list of tuples based on the total expense amount
        (e.g. 825.0) in descending order of the expense amount, e.g. sorted results: ("food", 5000.0), ("rent",
        1000.0), ("coffee", 5.0)

        Returns the list of sorted tuples. (Note: If the given sorting argument is not an acceptable value
        (e.g. ‘expense_type’ or 'amount'), this method does nothing except print a friendly message and return None.)
        """

        # TODO Insert your code
        #initialize list to store tuples
        lst = []
        #use built in dict items method to get all key:value pairs
        items = expenses.items()
        #iterate over key,value pairs and append then to list
        for key, value in items:
            lst.append((key, value.amount))
        if sorting == "amount":
            #sort list by amount descending
            lst.sort(key = lambda item: item[1], reverse = True)
            return lst
        elif sorting == "expense_type":
            #sort list expense type alphabetically
            lst.sort(key = lambda item: item[0])
            return lst
        else:
            print("The sorting argument is not an acceptable value")
            return None


    def export_expenses(self, expenses, expense_types, file):
        """Exports the Expense objects associated with the given expense_types from the given expenses dictionary to
        the given file.

        Do not append to the file. If the function is called again and the given file already exists, make sure it
        overwrites what was previously in the file instead of appending to it.

        Iterates over the given expenses dictionary, filters based on the given expense types (a list of strings),
        and exports to a file.  Skips any expense type in the given list of expense types that doesn't exist.

        If the expenses argument is the dictionary {"food": Expense("food", 5000.00), "rent": Expense("rent",
        1000.00), "coffee": Expense("coffee", 5.00), "clothes": Expense("clothes", 58.92)} and the expense_types
        argument is the list of strings [‘coffee', 'clothes', 'rent’], exports a file containing: coffee: 5.00
        clothes: 58.92 rent: 1000.00

        If the expenses argument is the dictionary {"food": Expense("food", 5000.00), "rent": Expense("rent",
        1000.00), "coffee": Expense("coffee", 5.00), "clothes": Expense("clothes", 58.92)} and the expense_types
        argument is the list of strings [‘coffee', 'clothes', 'sports’], exports a file containing: coffee: 5.00
        clothes: 58.92

        Note, the specified expense type 'sports' does not exist in the expenses dictionary, so it is ignored.

        If an item is duplicated in the given expense types, don’t worry about it, just export the data as is. You
        should not deduplicate the expense types.

        This method doesn’t return anything.
        """

        # TODO Insert your code
        #open given file in write mode so it can overwrite
        f = open(file, 'w')
        #iterate over expense_types
        for expense in expense_types:
            # nly export expense types that exist
            if expense in expenses:
                #build the line and round expense amount
                f.write(f'{expense}: {expenses[expense].amount:.2f}\n')
        #close file
        f.close()



