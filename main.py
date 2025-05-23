import random

MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "A": 2,
    "B":4,
    "C":6,
    "D":8

}
def get_slot_machine_spin(rows,cols,symbols):

    ...
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

def get_bet():

    while True: 

        amount = input("Enter the amount you want to bet? R")
        
        #we have to check if the amount is a number/int 

        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
        
                print(f"Amount must be R{MIN_BET} - R{MAX_BET}.")

        else:
            print("Please enter a number.")
    return amount
    

def get_number_of_lines():
     

     while True: 

        lines = input("Enter the number of lines you want to be on(1-"+ str(MAX_LINES) + ")? ")


        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
               return lines
            else:
        
                print("Please enter valid number of lines")

        else:
            print("Please enter a number.")
        # return lines
def main():         
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that number, your current balance is: R{balance}")
        else:
            break
    print(f"You are betting R{bet} on {lines} lines. Total bet is equal to: R{total_bet}")

    
    

main() #call main function 


