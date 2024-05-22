import sqlite3
import database
import os
from tabulate import tabulate

"""
Class Bank Methods:

- add_user(self, name, uid, accountNumber, accountBalance, nationalID, phoneNumber, PIN)
- input_user(self)
- delete_user(self, uid)
- show_table(self, table_name)
- update_name(self, name, uid)
- update_accountNumber(self, accountNumber, uid)
- update_accountBalance(self, accountBalance, uid)
- update_nationalID(self, nationalID, uid)
- update_phoneNumber(self, phoneNumber, uid)
- update_PIN(self, PIN, uid)
- retrieve_account(self, uid)
- retrieve_uid_with_username(self, name)
- retrieve_name(self, uid)
- retrieve_accountNumber(self, uid)
- retrieve_accountBalance(self, uid)
- retrieve_nationalID(self, uid)
- retrieve_phoneNumber(self, uid)
- retrieve_PIN(self, uid)
"""

class Bank():
    def __init__(self):
        pass

    def add_user(self, name, uid, accountNumber, accountBalance, nationalID, phoneNumber, PIN):
        db = sqlite3.connect("src/app.db")
        cr = db.cursor()
        cr.execute(
            f"INSERT INTO users (name, uid, accountNumber, accountBalance, nationalID, phoneNumber, PIN) VALUES ('{name}', {uid}, '{accountNumber}', '{accountBalance}', '{nationalID}', '{phoneNumber}', '{PIN}')"
        )
        db.commit()
        db.close()
        print(f"{name} added successfully !")

    def input_user(self):
        name = input("Enter name: ")
        uid = int(input("Enter uid: "))
        accountNumber = input("Enter account number: ")
        accountBalance = input("Enter account balance: ")
        nationalID = input("Enter national ID: ")
        phoneNumber = input("Enter phone number: ")
        PIN = input("Enter PIN: ")
        self.add_user(
            name.strip(),
            uid,
            accountNumber.strip(),
            accountBalance.strip(),
            nationalID.strip(),
            phoneNumber.strip(),
            PIN.strip(),
        )

    def delete_user(self, uid):
        db = sqlite3.connect("src/app.db")
        cr = db.cursor()
        cr.execute(f"DELETE FROM users WHERE uid = {uid}")
        db.commit()
        db.close()
        print(f"User with uid {uid} deleted successfully !")
    
    def show_table(self, table_name):
        db = sqlite3.connect("src/app.db")
        cr = db.cursor()
        cr.execute(f"SELECT rowid, * FROM {table_name}")
        entries = cr.fetchall()
        headers = [description[0] for description in cr.description]
        print(tabulate(entries, headers=headers, tablefmt='pretty'))
        db.commit()
        db.close()


################################################## users Table Update Functions ####################################################################
    def update_name(self, name, uid):
        db = sqlite3.connect("src/app.db")
        cr = db.cursor()
        cr.execute(f"UPDATE users SET name = '{name}' WHERE uid = {uid}")
        db.commit()
        db.close()
        print(f"Name updated successfully !")

    def update_accountNumber(self, accountNumber, uid):
        db = sqlite3.connect("src/app.db")
        cr = db.cursor()
        cr.execute(f"UPDATE users SET accountNumber = '{accountNumber}' WHERE uid = {uid}")
        db.commit()
        db.close()
        print(f"Account number updated successfully !")

    def update_accountBalance(self, accountBalance, uid):
        db = sqlite3.connect("src/app.db")
        cr = db.cursor()
        cr.execute(
            f"UPDATE users SET accountBalance = '{accountBalance}' WHERE uid = {uid}"
        )
        db.commit()
        db.close()
        print(f"Account balance updated successfully !")

    def update_nationalID(self, nationalID, uid):
        db = sqlite3.connect("src/app.db")
        cr = db.cursor()
        cr.execute(f"UPDATE users SET nationalID = '{nationalID}' WHERE uid = {uid}")
        db.commit()
        db.close()
        print(f"National ID updated successfully !")

    def update_phoneNumber(self, phoneNumber, uid):
        db = sqlite3.connect("src/app.db")
        cr = db.cursor()
        cr.execute(f"UPDATE users SET phoneNumber = '{phoneNumber}' WHERE uid = {uid}")
        db.commit()
        db.close()
        print(f"Phone number updated successfully !")

    def update_PIN(self, PIN, uid):
        db = sqlite3.connect("src/app.db")
        cr = db.cursor()
        cr.execute(f"UPDATE users SET PIN = '{PIN}' WHERE uid = {uid}")
        db.commit()
        db.close()
        print(f"PIN updated successfully !")

########################################################################################################################################

############################################### users Table Retrieval Functions ####################################################################
    def retrieve_account(self, uid):
        db = sqlite3.connect("src/app.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM users WHERE uid = {uid}")
        data = cr.fetchall()
        print(data)
        db.close()

    def retrieve_uid_with_username(self, name):
        db = sqlite3.connect("src/app.db")
        db.row_factory = sqlite3.Row
        cr = db.cursor()
        cr.execute(f"SELECT uid FROM users WHERE name = '{name}'")
        row = cr.fetchone()
        db.close()
        if row is not None:
            return row["uid"]
        else:
            return "Not found"

    def retrieve_name(self, uid):
        db = sqlite3.connect("src/app.db")
        db.row_factory = sqlite3.Row
        cr = db.cursor()
        cr.execute(f"SELECT name FROM users WHERE uid = {uid}")
        row = cr.fetchone()
        db.close()
        if row is not None:
            return row["name"]
        else:
            return "Not found"

    def retrieve_accountNumber(self, uid):
        db = sqlite3.connect("src/app.db")
        db.row_factory = sqlite3.Row
        cr = db.cursor()
        cr.execute(f"SELECT accountNumber FROM users WHERE uid = {uid}")
        row = cr.fetchone()
        db.close()
        if row is not None:
            return row["accountNumber"]
        else:
            return "Not found"

    def retrieve_accountBalance(self, uid) -> int:
        db = sqlite3.connect("src/app.db")
        db.row_factory = sqlite3.Row
        cr = db.cursor()
        cr.execute(f"SELECT accountBalance FROM users WHERE uid = {uid}")
        row = cr.fetchone()
        db.close()
        if row is not None:
            return row["accountBalance"]
        else:
            return "Not found"

    def retrieve_nationalID(self, uid):
        db = sqlite3.connect("src/app.db")
        db.row_factory = sqlite3.Row
        cr = db.cursor()
        cr.execute(f"SELECT nationalID FROM users WHERE uid = {uid}")
        row = cr.fetchone()
        db.close()
        if row is not None:
            return row["nationalID"]
        else:
            return "Not found"
        
    def retrieve_phoneNumber(self, uid):
        db = sqlite3.connect("src/app.db")
        db.row_factory = sqlite3.Row
        cr = db.cursor()
        cr.execute(f"SELECT phoneNumber FROM users WHERE uid = {uid}")
        row = cr.fetchone()
        db.close()
        if row is not None:
            return row["phoneNumber"]
        else:
            return "Not found"

    def retrieve_PIN(self, uid):
        db = sqlite3.connect("src/app.db")
        db.row_factory = sqlite3.Row
        cr = db.cursor()
        cr.execute(f"SELECT PIN FROM users WHERE uid = {uid}")
        row = cr.fetchone()
        db.close()
        if row is not None:
            return row["PIN"]
        else:
            return "Not found"
        
########################################################################################################################################

def main():
    user1 = Bank()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("########################################")
        print("Welcome to the Bank System!\nWhat would you like to do?\n")
        print("1. Add User\n2. Delete User\n3. Update User\n4. Retrieve User Data\n5. Show Users Table\n6. Exit\n")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                user1.input_user()
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"User Added Successfully !")
            case "2":
                uid = int(input("Enter uid of user to delete: "))
                os.system('cls' if os.name == 'nt' else 'clear')
                user1.delete_user(uid)

            case "3":
                uid = int(input("Enter uid of user to update data: "))
                while True:
                    print("########################################")
                    print("What would you like to update:\n")
                    print("1. Name\n2. Account Number\n3. National ID\n4. Phone Number\n5. PIN\n6. Return to previous menu\n")
                    choice = input("Enter your choice: ")
                    match choice:
                        case "1":
                            name = input("Enter new name: ")
                            user1.update_name(name, uid)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Name Updated Successfully !")
                        case "2":
                            accountNumber = input("Enter new account number: ")
                            user1.update_accountNumber(accountNumber, uid)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Account Number Updated Successfully !")
                        case "3":
                            nationalID = input("Enter new national ID: ")
                            user1.update_nationalID(nationalID, uid)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("National ID Updated Successfully !")
                        case "4":
                            phoneNumber = input("Enter new phone number: ")
                            user1.update_phoneNumber(phoneNumber, uid)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Phone Number Updated Successfully !")
                        case "5":
                            PIN = input("Enter new PIN: ")
                            user1.update_PIN(PIN, uid)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("PIN Updated Successfully !")
                        case "6":
                            print("Returning to previous menu...")
                            break
                        case _:
                            print("Invalid choice!")

            case "4":
                uid = int(input("Enter uid of user to retrieve data: "))
                while True:
                    print("########################################")
                    print("What would you like to retrieve:\n")
                    print("1. Name\n2. Account Number\n3. Account Balance\n4. National ID\n5. Phone Number\n6. Retrieve All\n7. Return to previous menu\n")
                    choice = input("Enter your choice: ")
                    match choice:
                        case "1":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Name: " + user1.retrieve_name(uid))
                        case "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Account Number: " + user1.retrieve_accountNumber(uid))
                        case "3":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Account Balance: " + user1.retrieve_accountBalance(uid))
                        case "4":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("National ID: " + user1.retrieve_nationalID(uid))
                        case "5":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Phone Number: " + user1.retrieve_phoneNumber(uid))
                        case "6":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(user1.retrieve_account(uid))
                        case "7":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Returning to previous menu...")
                            break
                        case _:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Invalid choice!")
            case "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Users Table: ")
                user1.show_table("users")
                input("Press enter to continue...")
            
            case "6":
                # os.system('cls' if os.name == 'nt' else 'clear')
                print("Exiting...")
                return
            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid choice! ")            

main()


