import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


class SimpleBank:

    def __init__(self):
        self.balance = None
        self.card_number = None
        self.pin = None
        self.iin = "400000"
        self.dictionary = {}
        self.acc_identifier = None
        self.command = "SELECT number,pin FROM card"

    def list_in_dict(self, data):
        dictionary = {}
        for i in data:
            dictionary[i[0]] = i[1]
        return dictionary

    def insert_into(self, card, pin):
        cur.execute(f"INSERT INTO card (number,pin) VALUES({card},{pin})")
        conn.commit()

    def read_query(self, query):
        cur.execute(query)
        temp = self.list_in_dict(cur.fetchall())
        return temp

    def create_pin(self):
        return '%04d' % random.randint(0, 9999)

    def create_acc_identifier(self):
        self.acc_identifier = '%09d' % random.randint(0, 999999999)
        return self.acc_identifier

    def check_balance(self, log):
        cur.execute(f"SELECT balance FROM card WHERE number = '{log}'")
        result = cur.fetchone()
        return result[0]

    def add_income(self, income, log):
        cur.execute(f"UPDATE card SET balance = balance + {income} WHERE number = '{log}' ")
        conn.commit()

    def close_account(self, log):
        cur.execute(f"DELETE FROM card WHERE number = '{log}'")
        conn.commit()

    def do_transfer(self, log):
        to_card = input("Enter card number:\n")
        if self.luhn_algorithm(to_card):
            if to_card not in self.dictionary:
                print("Such a card does not exist.")
            elif to_card == log:
                print("You can't transfer money to the same account!")
            else:
                how_much = int(input("Enter how much money you want transfer:\n"))
                if how_much > self.check_balance(log):
                    print("Not enough money!")
                else:
                    self.add_income(how_much, to_card)
                    cur.execute(f"UPDATE card SET balance = balance - {how_much} WHERE number = '{log}'")
                    conn.commit()
                    print("Success!")
        else:
            print("Probably you made a mistake in the card number. Please try again!")

    def create(self):
        print("You card has been created")
        temp = self.iin + self.create_acc_identifier()
        card_number = self.luhn_algorithm(temp)
        pin = self.create_pin()
        self.insert_into(card_number, pin)
        print(f"You card number:\n{card_number}")
        print(f"You card PIN:\n{pin}")

    def log(self):
        log = input("Enter your card number:\n")
        password = input("Enter you PIN:\n")
        self.dictionary = self.read_query(self.command)
        if log in self.dictionary and self.dictionary.get(log) == password:
            print("Ypu have successfully logged in!")
            while True:
                print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
                menu = input()
                if menu == "1":
                    print(self.check_balance(log))
                elif menu == "2":
                    income = int(input("Enter income:\n"))
                    self.add_income(income, log)
                    print(f"Successfully added {income}!")
                elif menu == "3":
                    self.do_transfer(log)
                elif menu == "4":
                    self.close_account(log)
                    print("The account has been closed!")
                elif menu == "5":
                    print("You successfully log out!")
                    self.start()
                elif menu == "0":
                    print("")
                    print("Bye")
                    exit(0)
        else:
            print("Wrong card number or PIN")

    def start(self):
        while True:
            print("1. Create an account\n2. Log into account\n0. Exit")
            choice = input()
            if choice == "1":
                self.create()
            elif choice == "2":
                self.log()
            elif choice == "0":
                print("")
                print("Bye")
                exit(0)

    def luhn_algorithm(self, card_number):
        temp = card_number
        summa = 0
        if len(temp) == 16:
            for i in range(0, 16):
                if i % 2 == 0:
                    num = int(temp[i]) * 2
                    if num > 9:
                        num -= 9
                    summa += num
                else:
                    summa += int(temp[i])
            if summa % 10 == 0:
                return True
            else:
                return False
        else:
            for i in range(0, 15):
                if i % 2 == 0:
                    num = int(temp[i]) * 2
                    if num > 9:
                        num -= 9
                    summa += num
                else:
                    summa += int(temp[i])
            if summa % 10 == 0:
                return card_number + "0"
            else:
                return card_number + f"{10 - summa % 10}"


bank = SimpleBank()
bank.start()
