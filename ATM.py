import getpass
import csv


class Atm:
    machine = "money Transfer machine"

    def add(self):
        bankbalance[self.b] = bankbalance[self.b] + self.plus
        print(f"Your Current Balance is {bankbalance[self.b]}")

    def diff(self):
        bankbalance[self.b] = bankbalance[self.b] - self.plus
        print(f"Your Current Balance is {bankbalance[self.b]}")

    def balance(self):
        print(f"Your Current Balance is {bankbalance[self.b]}")


atm = Atm()
with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        name = line[0]
        password = line[1]
        ballance = line[2]
        print(name, password, ballance)
        global name
        global password
        global ballance


atm.a = input("Enter your name: ")
atm.b = None
if name != atm.a:
    print("You dont have a account in this bank")
else:
    while atm.b != data[atm.a]:
        atm.b = getpass.getpass()
        if atm.b == data[atm.a]:
            print("Welcome to ATM")
            break
        else:
            print("Your Password is incorrect. Please renter your password")
atm.c = None
while atm.c == None:
    atm.c = input('''Press 1 For Credit
Press 2 For Withdrawl
Press 3 For Balance Enquiry\n''')
    if atm.c == "1":
        atm.plus = int(input("Enter the balance of input: "))
        atm.add()
    if atm.c == "2":
        atm.plus = int(input("Enter the balance you want to take: "))
        atm.diff()
    if atm.c == "3":

        atm.balance()
print("Thank you for visiting us")
