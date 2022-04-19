class Atm(object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin = pin_number

    def cash_withdrawl(self, amount):
        new_amount = 1000000 - amount
        print("You have withdrawn " + str(amount) + " dollars. Your balance is " + str(new_amount))

    def check_balance(self):
        print('Your bank balance is 1000000')

def main():
    Card_number = input("Please enter your card number: ")
    pin_number = input("Please enter your pin number: ")

    new_user = Atm(Card_number, pin_number)

    print("Choose your activity: ")
    print("1. Check your balance   2. Withdraw Cash")
    activity = int(input("Enter activity number: "))

    if(activity == 1):
        new_user.check_balance()
        
    elif(activity == 2):
        amount = int(input("Please enter the amount you want to withdraw: "))
        new_user.cash_withdrawl(amount)
        
    else:
        print("Please enter a valid activity number.")

if __name__ =="__main__":
    main()


