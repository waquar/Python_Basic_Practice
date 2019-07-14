from random import  randint

class SavingAccount():
    def __init__(self):
        self.savingAccounts = {}

    def createAccount(self, name, initialDeposit):

        self.accountNumber = randint(9000, 9999)
        self.savingAccounts[self.accountNumber] = [name, initialDeposit]
        print("your unique account number is : ", self.accountNumber)
        print(self.savingAccounts)


    def authentication(self, name, accountNumber):
        print(self.savingAccounts)
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("Thankyou ! Authenticated")
                self.accountNumber = accountNumber
                return  True
            else:
                print("Authentication Failed inner if")
        else:
            print("Authentication Failed outer if")
            return  False

    def withdraw(self, withdrawlAmount):
        if withdrawlAmount > self.savingAccounts[self.accountNumber][1]:
            print('insufficient amount')
        else:
            self.savingAccounts[self.accountNumber][1] -= withdrawlAmount
            print("withdrawl successful")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingAccounts[self.accountNumber][1 ]  += depositAmount
        print("deposit successful")
        self.displayBalance()

    def displayBalance(self):
        print("available balance is : ", self.savingAccounts[self.accountNumber][1])


objsavingaccount = SavingAccount()

while True:
    print("1: For creating Account")
    print("2 : For existing Account")
    print("3: to exit")
    userchoice = int(input('your choice please!!'))
    if userchoice == 1:
        print("Enter your name--")
        name = input()
        print("Enter your First Deposit Amount:  ")
        initialDeposit =int(input())
        objsavingaccount.createAccount(name, initialDeposit)
    elif userchoice == 2:
        print("Enter your name")
        name = input()
        accountNumber = int(input('your account number?'))
        status =  objsavingaccount.authentication(name, accountNumber)
        if status is True:
            while True:
                print("enter 1 to withdraw: ")
                print("enter 2 to deposit")
                print("enter 3 to see your balance")
                print('4 to go back previous menu')
                userchoice = int(input())
                if userchoice is 1:
                    print('withdrawl amount:')
                    withdrawlamount = int(input())
                    objsavingaccount.withdraw(withdrawlamount)
                elif userchoice is 2:
                    print("deposit amount:")
                    depositamount = int(input())
                    objsavingaccount.deposit(depositamount)
                elif userchoice is 3:
                    objsavingaccount.displayBalance()
                elif userchoice is 4:
                    break

    elif userchoice is 3:
        quit()