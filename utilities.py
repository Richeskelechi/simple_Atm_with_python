def try_again() -> bool:
    try_again = True
    # the try again gives you just two chances. So the count will keep track of how many times you have tried again
    count = 0
    while try_again:
        user_try = input(
            "**** Do You Want To Perform Another Transaction y for 'Yes'  and n for 'No'")
        user_try = user_try.lower()
        # so once you select y it will allow you to run the App again
        if user_try in ("y","n","yes","no"):
            return True if user_try in ("y","yes") else False
        else:
            # if you select a wrong option it will ask you to try again while updating the count so that you can only try again twice
            count += 1
            if count == 2:
                print("**** Thank You For Using Our ATM \n ****")
                return False
            print("*** Invalid Entery. You Have One More Trial ***")
        
def get_user_by_id(registredUser):
    userID = input("Enter Your UserID: ")
    # here I am looping through the registered user list to get details of that user
    user_found = list(filter(lambda d: d["userID"] == userID, registredUser))
    return user_found[0] if len(user_found) else None