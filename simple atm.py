from selectors import (
    open_account,
    withdrawal,
    to_deposit,
    check_balance,
    exit_app,
    invalid_entry,
)

keep_running = True
selection_bank = {
    "1": open_account,
    "2": withdrawal,
    "3": to_deposit,
    "4": check_balance,
    "5": exit_app
}
# This will allow the App to keep running as long as the keep_running is True.
while keep_running:
    # I am telling the user what the App is all about.
    print("**** Welcome To ZURI ATM.\n Please Enter 1 To Open Account, \n 2 To Withdraw, \n 3 To Deposit, \n 4 To Check Balance, \n 5 To Exit. \n ****")
    # Allowing the user to make a selection
    selection = input("Enter Your Selection: ")
    action = selection_bank.get(selection,invalid_entry)
    keep_running = action()
# End of the program
print("*********** Thank You For Using ZURI ATM. See You Some Other Time. ***********")