def deposit():
    #This function is responsible for collecting user input that gets the deposit from the user 

    while True: 

        amount = input("What would you like to deposit? R")

        #we have to check if the amount is a number/int 

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
        
                print("amount must be greater than 0")

        else:
            print("Please enter a number.")
    return amount

            
deposit()
        