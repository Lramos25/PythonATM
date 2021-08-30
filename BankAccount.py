# BankAccount.py
# Author: Luis Ramos
# Date: 28 April 2021

#import Transaction class
from Transaction import *
from datetime import datetime

def main():
    """Display main menu and class functions based on the selected action"""

    print ('Welcome to Bank Account Application')
    print ()

    done = False

    # Create an empty list of transactions
    list_of_transactions = []

    #Loop as long as done is False
    while (not done):
        #Display menu
        print ('===================================')
        print ('A - Read data from the file')
        print ('B - Display list of transactions')
        print ('C - Add a new transaction')
        print ('D - Calculate current balance')
        print ('E - Save data to a file')
        print ('Q - Quit')
        print ('===================================')
        print ('Please select an action by typing A, B, C, D, E, or Q')
        action = input ('? ')

        if (action == 'A' or action == 'a'):
            read_data (list_of_transactions)
        elif (action == 'B' or action == 'b'):
            display_list (list_of_transactions)
        elif (action == 'C' or action == 'c'):
            add_transaction (list_of_transactions)
        elif (action == 'D' or action == 'd'):
            calculate_balance (list_of_transactions)
        elif (action == 'E' or action == 'e'):
            save_data (list_of_transactions)
        elif (action == 'Q' or action == 'q'):
            done = True
        else:
            print ('Incorrect action type. Please try again')

        print ()

    print ('Thank you for using Bank Account Application')

def read_data (list_of_transactions):
    """Read data from the input file, create transaction object and add it to
       the list of transactions"""

       # Ask user for name of the input file, read each line of the data,
       # split line using colon (:) is delimiter, create transaction object
       # and add it to the list of transaction. Display error message if the
       # input file is not found.

    try:
        readFileName = ("bank_account_data")

        ex = ".txt" #will force the file to be a text file without the user needed to add it to the file name

        openFile = readFileName+ex #combine the user input with the file extension

    #open the input file to be read
        infile = open(openFile, "r")
    
    #loop to read line and append list
        for line in infile:
            
            line = line.strip()
            list1 = line.split(":")
            list_of_transactions.append(list1)

        #print (list_of_transactions) ##used for testing only
                   
        infile.close()

    except FileNotFoundError as err:

        print ("File is not found, please try again")
        
    print ('Read Data Function')
    


def display_list (list_of_transactions):
   """ Displays list of transactions """

   # Sort the list of transactions by date and display list of transactions
   # in form of a table

##-->>   USED THE LAMDBA FUNCTION WITH A KEY SO IF THE SORT CRITERIA CHANGES LATER THE CODE CAN BE ADJUSTED EASY ENOUGH. <<--##
##-->>   USING JUST PRINT (SORTED(LIST...)) WOULD HAVE WORKED BECAUSE THE DATE IS THE FIRST ELEMENT BUT I WANTED TO MAKE FUTRURE CHANGES EASIER <<--##
   print (sorted(list_of_transactions, key = lambda x:(x[0])))
   
           


def add_transaction (list_of_transactions):
    """Adds a new transaction to list of Transactions"""

    # Ask user for date, type, and amount of transaction, create a transaction
    # object and append it to the list of transactions.
    # Display an error message if the transaction type is not valid or amount
    # is negative. Valid transaction types are deposit, withdraw, bank charge
    # and interest

    new_transaction = []

    valid_types = ["deposit", "withdraw", "bank charge", "interest"]
    

    date_valid = False

    while not date_valid:
        new_date = input("Enter the date of the transaction as YYYYMMDD:\n ")

        try:
        
            check_date = datetime.strptime(new_date, "%Y%m%d")

            date_valid = True
        
            date_string = check_date.strftime("%Y%m%d")

        except ValueError as err:
            print ("Try again, format of date should be YYYMMDD")
                                
    new_transaction.append(date_string)


    type_valid = False

    while not type_valid:
        
        new_type = input("What type of transaction is this \n Valid transaction types are deposit, withdraw, bank charge or interest: \n ")

        try:

            if new_type not in valid_types:

                print ("Try again, Valid transaction types are deposit, withdraw, bank charge or interest")

            else:

                type_valid = True
            
                print (new_type)

        except ValueError as err:
            print ("Try again, Valid transaction types are deposit, withdraw, bank charge or interest")
        
    new_transaction.append(new_type)


    
    amount_valid = False

    while not amount_valid:
        
        new_amount = float(input("What is the amount: "))
        
        try:
            if new_amount <= 0:

                print ("Invalid input, must enter a positive number")
                
            else:
                
                amount_valid = True
            
                new_amount = "{:.2f}".format(new_amount)
                
                new_transaction.append(new_amount)

        except ValueError as e:
            print ("Try again, must input an amount in dollar(s) and cent(s) ex. 2.13 or 2")

    
    list_of_transactions.append(new_transaction)
   
    print ('Add Transaction Function')



def calculate_balance (list_of_transactions):

    """Calculates the current balance"""

    # Start with initializing balance to zero
    # For each transaction in the list of transactions you will
    # add the amount to balance if the transaction type is deposit or interest
    # subtract the amount if transaction type is withdraw or bank charge
    # Print the balance on the screen

    current_balance = 0

    positive_total = [float(z) for x,y,z in list_of_transactions if y == "deposit" or y == "interest"]

    total_sum = sum(positive_total)
        
    negitive_total = [float(z) for x,y,z in list_of_transactions if y == "withdraw" or y == "bank charge"]

    total_diff = sum(negitive_total)

    current_balance = (current_balance + total_sum)- total_diff

    print ("total credits come to: ", total_sum)

    print ("total withdraws come to: ", total_diff)

    print ("current balance is: ", current_balance)
        
    print ("Your current Balance is: $", current_balance)
            
        


def save_data (list_of_transactions):
    """ Saves list of transaction to a file"""

    # Ask user for name of the output file, sort the list of transactions by date
    # and save the data using the following format:
    # date:transaction_type:amount
    # Display a message that data was saved to the output file.

    saveFileName = input("What file should be read? ")

    ex = ".txt" #will force the file to be a text file without the user needed to add it to the file name

    openSaveFile = saveFileName+ex #combine the user input with the file extension

    temp_transaction_list = []
    
    for item in sorted(list_of_transactions, key = lambda x:(x[0])):

        temp_list = ":".join(item)

        temp_transaction_list.append(temp_list)
    

    print (temp_transaction_list)
        
    with open(openSaveFile, 'w') as f:
        
        for item in temp_transaction_list:
            
            f.write("%s\n" % item)
           
    print ('Save Data Function')
            
