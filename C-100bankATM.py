class Atm:

    def __init__(user, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pin = pin
        
    def balance(self)
        print("Your balance is 500000")
        
    def debit(self, amount):
    newAmount = 500000 - amount
        print(" You have withdrawn amount "+(amount)" Your remaininf balance is "+(newAmount)) 
       
    user1 = atm( cardNumber, pinNumber)
    
    cardNo = input(" enter your card number: ")
    pinNo = input(" enter your pin number: ")
    
    print( "Choose your  task" )
    print (" 1. Balance 2. Debit")
    task = input("Enter task number:- ")
    
    if(task == 1):
        user1.balance()
        
    elif (task ==2)
        amount = int(input("Enter the amount: "))
        user1.debit(amount)
        
    else:
        print("Entger walid task number")
        
    
    
    
    