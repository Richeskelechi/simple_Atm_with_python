from atexit import register
from utilities import get_user,try_again

# list of registered Users in The App
registredUser = [
    {
        "name": "Deo John",
        "password": "john45",
        "cash": 70000,
        "pin": 6657,
        "userID": "0001"
    },
    {
        "name": "Sidney Snow",
        "password": "snow34",
        "cash": 76030,
        "pin": 3422,
        "userID": "0002"
    },
    {
        "name": "Carl Mark",
        "password": "mark89",
        "cash": 70000,
        "pin": 8976,
        "userID": "0003"
    },
    {
        "name": "Mike Sam",
        "password": "sam67",
        "cash": 45390,
        "pin": 1280,
        "userID": "0004"
    },
]

def open_account():
    print("**** Welcome To ZURI ATM.\n Please Enter Your Name, \n Password, \n Pin and, \n Amount To Deposit. \n ****")
    name = input("Enter Your Name: ")
    password = input("Enter Your Password: ")
    pin = input("Enter Your Transaction Pin: Please Use Just four Digits: ")
    cash = input("Enter The Amount to deposit. Must be numeric: ")
    # Here I am using a try and except to ensure that the amount and pin is numeric
    try:
        int(cash)
        int(pin)
        cash = int(cash)
        pin = int(pin)
        # here I am getting the length of the list so that I can get a new userID for the new user
        new_user_id = len(registredUser) + 1
        # I am creating a new user with the information that the user entered
        new_user_info = {
            "name": name,
            "password": password,
            "cash": cash,
            "pin": pin,
            "userID": f"000{str(new_user_id)}"
        }
        registredUser.append(new_user_info)
        print(f"**** Your Account Has Been Created Successfully. Your UserID is {new_user_info['userID']} Thank You****")
        # I am calling the function try_again to allow the user to try another transaction if he or she wants
        # if the amount and pin you provided is not a number it will give you an error message and ask if you want to try again
    except:
        print("**** Invalid Cash/Pin. Both Must Be A Number Please Try Again ****")
    finally:
        return try_again()
#list(filter(lambda d: d['type'] in keyValList, exampleSet))
def withdrawal():
    # Your userID will be asked to verify your Identity
    print("**** Welcome To ZURI ATM.\n Please Enter Your userID, To Withdraw \n****")
    # here I am looping through the registered user list to get details of that user
    user_found = get_user(registredUser)
    if user_found:
        identified_user = user_found
        user_name = identified_user["name"]
        print(f"**** Welcome To ZURI ATM. {user_name} ****")
        # here I am using try and except to catch the amount you want to withdraw
        try:
            withdraw = int(input("Enter Amount To Withdraw: "))
            # if the amount is less than of equal to your available balance in the bank.
            if withdraw <= identified_user["cash"]:
                # Here I am asking for your transaction pin to validate your transaction.
                pin = int(input(
                    "Enter Your Pin To Validate Withdraw: "))
                # once you provide the right pin withdrawal is successful
                if pin == identified_user["pin"]:
                    # here I am updating the balance of the user
                    identified_user["cash"] -= withdraw
                    print(
                        "**** Withdraw Successful. Thank You For Using ZURI ATM ****")
                    # if the pin you provided is not valid it will give you an error message and ask if you want to try again
                else:
                    print("**** Invalid Pin ****")
                # if the pin you provided is not a number it will give you an error message and ask if you want to try again
            else:
                print("**** You Have Insufficient Funds. ****")
            # if the amount you provided is not a number it will give you an error message and ask if you want to try again
        except:
            print("**** Invalid Input For Amount. ****")
    # if the userID you provided is not valid it will give you an error message and ask if you want to try again
    else:
        print("**** Invalid UserID ****")
    return try_again()
def to_deposit():
    print("**** Welcome To ZURI ATM.\n Please Enter Your userID, To Deposit \n****")
    user_found = get_user(registredUser)
    if user_found:
        identified_user = user_found
        user_name = identified_user["name"]
        print(f"**** Welcome To ZURI ATM. {user_name} ****")
        # here I am using try and except to catch the amount you want to deposit
        try:
            deposit = int(input("Enter Amount To Deposit: "))
            # Here I am updating the amount in the bank with the amount you deposited
            identified_user["cash"] += deposit
            print("**** Deposit Successful. Thank You For Using ZURI ATM ****")
            # if the amount you provided is not a number it will give you an error message and ask if you want to try again
        except:
            print("**** Invalid Input For Amount. ****")
    # if the userID you provided is not valid it will give you an error message and ask if you want to try again
    else:
        print("**** Account Not Found. Please Try Again. ****")
    return try_again()

def check_balance():
    print(
        "**** Welcome To ZURI ATM.\n Please Enter Your userID, To Check Balance \n****")
    user_found = get_user(registredUser)
    if user_found:
        identified_user = user_found
        user_name = identified_user["name"]
        print(f"**** Welcome To ZURI ATM. {user_name} ****")
        # here I am printing the balance of the user
        print(f"**** Your Current Balance is: #{identified_user['cash']} ****")
    # if the userID you provided is not valid it will give you an error message and ask if you want to try again
    else:
        print("**** Account Not Found. Please Try Again. ****")
    return try_again()
def exit_app():
    print("**** Thank You For Using Our ATM ****")
    # I am setting keep_running to false to end the ATM CLI APP
    return False
def invalid_entry():
    print("**** Invalid Entery ****")
    return try_again()