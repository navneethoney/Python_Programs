
class Account:

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt
        print("Added {} to the balance".format(dep_amt))

    def withdrawl(self, wd_amt):

        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawl accepted")

        else:
            print("Sorry, not enough funds")

    def __str__(self):
        return ("Owner: {} \nBalance: {}".format(self.owner, self.balance))


acc = Account("Sam", 500)
print acc.owner
print acc.balance
print(acc)

acc.deposit(100)
print(acc)

acc.withdrawl(600)
print acc

acc.withdrawl(20)
print acc
