def main():


    with open("atm_accounts2.txt") as dataFile:
        login = {}
        sav_bal = {}
        ch_bal = {}
        accounts = []

    
        for line in dataFile:
            
            line = line.strip()
            list1 = line.split(":")
            accounts.append(list1)
            print(accounts)

        for user_id, user_pin, saving_bal, check_bal in accounts:
            login[user_id] = int(user_pin)
            sav_bal[user_id] = float(saving_bal)
            ch_bal[user_id] = float(check_bal)

    user_log_in(login,sav_bal,ch_bal,accounts)




def user_log_in(login,sav_bal,ch_bal,accounts):

    logged_in = False
    verified = False

    while not logged_in:       

        while not verified:

            login_id = input("Enter your log in ID: \n>>>")

            if login_id in login.keys():
                print ("Correct user ID")
                correct_pin = int(login[login_id])
                verified = True    
         
            else:
                print ("Incorrect ID, try again")

        login_pin = int(input("Enter your log in pin: \n>>>"))
        if correct_pin == login_pin:
                  
            logged_in = True
            
        else:
            print("bad pin, please try again")
        
    main_menu(login,sav_bal,ch_bal,accounts,login_id)


def main_menu(login,sav_bal,ch_bal,accounts,login_id):

    
    print ('Welcome to Bank Account Application')
    done = False
  
    while (not done):
        #Display menu
        print ('===================================')
        print ('A - See Balance')
        print ('B - Withdraw')
        print ('C - Deposit')
        print ('D - Transfer')
        print ('Q - Quit')
        print ('===================================')
        print ('Please select an action by typing A, B, C, D, or Q')
        action = input ('? ')

        if (action == 'A' or action == 'a'):
            acct_balance (login,sav_bal,ch_bal,accounts,login_id)
        elif (action == 'B' or action == 'b'):
            acct_withdraw (login,sav_bal,ch_bal,accounts,login_id)
        elif (action == 'C' or action == 'c'):
            acct_deposit (login,sav_bal,ch_bal,accounts,login_id)
        elif (action == 'D' or action == 'd'):
            funds_transfer (login,sav_bal,ch_bal,accounts,login_id)
        elif (action == 'Q' or action == 'q'):
            ## Save transactoions now
            complete (login,sav_bal,ch_bal,accounts,login_id)
            done = True
        else:
            print ('Incorrect action type. Please try again')

        print ()

    print ('Thank you for using Bank Account Application')

def acct_balance(login,sav_bal,ch_bal,accounts,login_id):

    acct = input("\nChecking (c) or Savings (s):\n>>")

    if acct.lower() == "c":        
        
        print("Current Checking Blalance: ", ch_bal.get(login_id))

    else:
            
        print("Current Savings Blalance: ", sav_bal.get(login_id))




def acct_withdraw(login,sav_bal,ch_bal,accounts,login_id):

    withdraw_input_error = True

    while withdraw_input_error is True:

        acct = input("\nChecking (c) or Savings (s):\n>>")
        amt = float(input("How much would you like to withdraw: \n>>"))
    
        if acct.lower() == "c":

            check_start = ch_bal.get(login_id)

            new_check_bal = check_start - amt

            temp_ch_bal = {login_id:new_check_bal}

            ch_bal.update(temp_ch_bal)
        
            print("Current Checking Blalance: ", ch_bal.get(login_id))

            withdraw_input_error = False

        elif acct.lower() == "s":

            sav_start = sav_bal.get(login_id)

            new_sav_bal = sav_start - amt

            temp_sav_bal = {login_id:new_sav_bal}

            sav_bal.update(temp_sav_bal)
            
            print("Current Savings Blalance: ", sav_bal.get(login_id))

            withdraw_input_error = False

        else:
            print("invalid input, please try again selection only allows c or s.")

def acct_deposit(login,sav_bal,ch_bal,accounts,login_id):

    dep_input_error = True

    while dep_input_error is True:

        acct = input("\nChecking (c) or Savings (s):\n>>")
        amt = float(input("How much would you like to deposit: \n>>"))
    
        if acct.lower() == "c":

            check_start = ch_bal.get(login_id)

            new_check_bal = check_start + amt

            temp_ch_bal = {login_id:new_check_bal}

            ch_bal.update(temp_ch_bal)
        
            print("Current Checking Blalance: ", ch_bal.get(login_id))

            dep_input_error = False

        elif acct.lower() == "s":

            sav_start = sav_bal.get(login_id)

            new_sav_bal = sav_start + amt

            temp_sav_bal = {login_id:new_sav_bal}

            sav_bal.update(temp_sav_bal)
            
            print("Current Savings Blalance: ", sav_bal.get(login_id))

            dep_input_error = False

        else:
            print("invalid input, please try again selection only allows c or s.")



def funds_transfer (login,sav_bal,ch_bal,accounts,login_id):

    transfer_input_error = True

    while transfer_input_error is True:

        tans_type = input("Transfer from Checking (cts) or Savings (stc):\n>>")
        amt = float(input("How much would you like to transfer: \n>>"))
    
        if tans_type.lower() == "cts":

            check_start = ch_bal.get(login_id)

            new_check_bal = check_start - amt

            temp_ch_bal = {login_id:new_check_bal}

            ch_bal.update(temp_ch_bal)

            sav_start = sav_bal.get(login_id)

            new_sav_bal = sav_start + amt

            temp_sav_bal = {login_id:new_sav_bal}

            sav_bal.update(temp_sav_bal)
            
            print("Current Savings Blalance: ", sav_bal.get(login_id))
        
            print("Current Checking Blalance: ", ch_bal.get(login_id))

            transfer_input_error = False

        elif tans_type.lower() == "stc":

            check_start = ch_bal.get(login_id)

            new_check_bal = check_start + amt

            temp_ch_bal = {login_id:new_check_bal}

            ch_bal.update(temp_ch_bal)

            sav_start = sav_bal.get(login_id)

            new_sav_bal = sav_start - amt

            temp_sav_bal = {login_id:new_sav_bal}

            sav_bal.update(temp_sav_bal)
            
            print("Current Savings Blalance: ", sav_bal.get(login_id))
        
            print("Current Checking Blalance: ", ch_bal.get(login_id))

            transfer_input_error = False

        else:
            print("invalid input, please try again selection only allows c or s.")

def complete (login,sav_bal,ch_bal,accounts,login_id):

    final_sav_bal = sav_bal.get(login_id)
    final_ch_bal = ch_bal.get(login_id)

    for i in range(len(accounts)):
        if accounts[i][0] == login_id:
            accounts[i][2] = str(final_sav_bal)
            accounts[i][3] = str(final_ch_bal)

    saveFileName = ("atm_accounts2.txt")

    openSaveFile = saveFileName 

    temp_accounts_list = []
    
    for item in accounts:

        temp_list = ":".join(item)

        temp_accounts_list.append(temp_list)
        
    with open(openSaveFile, 'w') as f:
        
        for item in temp_accounts_list:
            
            f.write("%s\n" % item)
           
    print ("---data saved---")

