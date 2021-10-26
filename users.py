class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self,ammount):
        self.account_balance += ammount
        return self

    def make_withdrawal(self, ammount):
        self.account_balance -= ammount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, ammount, User):
        self.account_balance -= ammount
        User.account_balance += ammount
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
keanu = User("Keanu Reeves", "keanu@thematrix.com")

guido.make_deposit(500).make_deposit(100) #test return
guido.make_deposit(400)
guido.make_deposit(80)
guido.make_withdrawal(350)
guido.display_user_balance()

monty.make_deposit(420)
monty.make_deposit(380)
monty.make_withdrawal(120)
monty.make_withdrawal(175)
monty.display_user_balance()

keanu.make_deposit(556)
keanu.make_withdrawal(223)
keanu.make_withdrawal(45)
keanu.make_withdrawal(9)
keanu.display_user_balance()

guido.transfer_money(226, keanu)

guido.display_user_balance()
keanu.display_user_balance()


