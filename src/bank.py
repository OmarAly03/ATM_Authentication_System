import sqlite3
import database

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

user1 = Bank()
user1.input_user()
