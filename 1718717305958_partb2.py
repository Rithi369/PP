class bankaccount:
    def __init__(self):
        self.balance=int(input("Enter the initial amount : "))
        print("your account created")

    def deposite(self):
        amount=int(input("enter the deposite amount : "))
        self.balance+=amount
        print("your new balance : ",self.balance)

    def withdraw(self):
        amount=int(input("Enter the amount to withdraw " ))
        if(amount>=self.balance):
            print("insufficent balance")
        else :
            self.balance-=amount
            print("your remainning balance : ",self.balance)

    def GetBalance(self):
        print("your balance : ",self.balance)

class savingsaccount(bankaccount):
    def __init__(self):
        bankaccount.__init__(self)

    def interest(self):
        self.rate=float(input("Enter rate of intrest : "))
        self.balance=self.balance+(self.balance*self.rate/100)
        print("your new balance : ",self.balance)
account=savingsaccount()
while(1):
    print("1.Deposit\n 2.withdraw \n 3.GetBalance\n 4.interest\n 5.exit")
    c=int(input("enter your choice "))
    if c==1:
        account.deposite()
    elif c==2:
        account.withdraw()
    elif c==3:
        account.GetBalance()
    elif c==4:
        account.interest()
    elif c==5:
        break
    else :
        print("invalid choice")
