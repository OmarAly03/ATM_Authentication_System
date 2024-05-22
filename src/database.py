import sqlite3

################################################### Table Management #####################################################################
def create_users_table(table_name):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            name TEXT,
            uid INTEGER,
            accountNumber TEXT,
            accountBalance TEXT,
            nationalID TEXT,
            phoneNumber TEXT,
            PIN TEXT
        )
    """
    )
    db.commit()
    db.close()
    print(f"Table {table_name} created successfully !")


def create_transactions_table(table_name):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            transactionID INTEGER,
            transactionType TEXT,
            uid INTEGER,
            date TEXT,
            amount REAL,
            newBalance REAL,
            sender TEXT,
            Receiver TEXT
        )
    """
    )
    db.commit()
    db.close()
    print(f"Table {table_name} created successfully !")

def create_variables_table(table_name):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} (transactionID INTEGER)"
    )
    db.commit()
    db.close()
    print(f"Table {table_name} created successfully !")


def delete_table(table_name):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"DROP TABLE IF EXISTS {table_name}")
    db.commit()
    db.close()
    print(f"Table {table_name} deleted successfully !")


def show_table(table_name):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"SELECT rowid, * FROM {table_name}")
    entries = cr.fetchall()
    for entry in entries:
        print(entry)
    db.commit()
    db.close()

########################################################################################################################################

#################################################### User & Transactions Management #####################################################
def add_user(name, uid, accountNumber, accountBalance, nationalID, phoneNumber, PIN):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(
        f"INSERT INTO users (name, uid, accountNumber, accountBalance, nationalID, phoneNumber, PIN) VALUES ('{name}', {uid}, '{accountNumber}', '{accountBalance}', '{nationalID}', '{phoneNumber}', '{PIN}')"
    )
    db.commit()
    db.close()
    print(f"{name} added successfully !")


def add_transaction(
    transactionID, transactionType, uid, date, amount, newBalance, sender, receiver
):
    
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(
        f"INSERT INTO transactions (transactionID, transactionType, uid, date, amount, newBalance, sender, receiver) VALUES ('{transactionID}', '{transactionType}',  {uid}, '{date}', '{amount}', '{newBalance}', '{sender}', '{receiver}')"
    )
    db.commit()
    db.close()
    print("New transaction added successfully !")


def delete_user(uid):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"DELETE FROM users WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"User with uid {uid} deleted successfully !")


def delete_transaction(transactionID):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"DELETE FROM transactions WHERE transactionID = {transactionID}")
    db.commit()
    db.close()
    print(f"Transaction with ID {transactionID} deleted successfully !")


def input_user():
    name = input("Enter name: ")
    uid = int(input("Enter uid: "))
    accountNumber = input("Enter account number: ")
    accountBalance = input("Enter account balance: ")
    nationalID = input("Enter national ID: ")
    phoneNumber = input("Enter phone number: ")
    PIN = input("Enter PIN: ")
    add_user(
        name.strip(),
        uid,
        accountNumber.strip(),
        accountBalance.strip(),
        nationalID.strip(),
        phoneNumber.strip(),
        PIN.strip(),
    )
########################################################################################################################################

################################################## users Table Update Functions ####################################################################
def update_name(name, uid):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"UPDATE users SET name = '{name}' WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"Name updated successfully !")


def update_accountNumber(accountNumber, uid):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"UPDATE users SET accountNumber = '{accountNumber}' WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"Account number updated successfully !")


def update_accountBalance(accountBalance, uid):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(
        f"UPDATE users SET accountBalance = '{accountBalance}' WHERE uid = {uid}"
    )
    db.commit()
    db.close()
    print(f"Account balance updated successfully !")


def update_nationalID(nationalID, uid):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"UPDATE users SET nationalID = '{nationalID}' WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"National ID updated successfully !")


def update_phoneNumber(phoneNumber, uid):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"UPDATE users SET phoneNumber = '{phoneNumber}' WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"Phone number updated successfully !")


def update_PIN(PIN, uid):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"UPDATE users SET PIN = '{PIN}' WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"PIN updated successfully !")

########################################################################################################################################
############################################### users Table Retrieval Functions ####################################################################
def retrieve_account(uid):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"SELECT * FROM users WHERE uid = {uid}")
    data = cr.fetchall()
    print(data)
    db.close()

def retrieve_uid_with_username(name):
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

def retrieve_name(uid):
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

def retrieve_accountNumber(uid):
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

def retrieve_accountBalance(uid) -> int:
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

def retrieve_nationalID(uid):
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
    
def retrieve_phoneNumber(uid):
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

def retrieve_PIN(uid):
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

######################################### transactions Table Retrieval Functions #######################################################
 
def retrieve_accountTransactions(uid):
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"SELECT * FROM transactions WHERE uid = {uid}")
    entries = cr.fetchall()
    string = ""
    for entry in entries[:7]:
        print(entry)
        string += str(entry) + "\n"
    db.commit()
    db.close()
    return string

def retrieve_transactionType(transactionID):
    db = sqlite3.connect("src/app.db")
    db.row_factory = sqlite3.Row
    cr = db.cursor()
    cr.execute(
        f"SELECT transactionType FROM transactions WHERE transactionID = {transactionID}"
    )
    row = cr.fetchone()
    db.close()
    if row is not None:
        print(row["transactionType"])
    else:
        print("Not found")

def retrieve_transactionDate(transactionID):
    db = sqlite3.connect("src/app.db")
    db.row_factory = sqlite3.Row
    cr = db.cursor()
    cr.execute(f"SELECT date FROM transactions WHERE transactionID = {transactionID}")
    row = cr.fetchone()
    db.close()
    if row is not None:
        print(row["date"])
    else:
        print("Not found")

def retrieve_transactionAmount(transactionID):
    db = sqlite3.connect("src/app.db")
    db.row_factory = sqlite3.Row
    cr = db.cursor()
    cr.execute(f"SELECT amount FROM transactions WHERE transactionID = {transactionID}")
    row = cr.fetchone()
    db.close()
    if row is not None:
        print(row["amount"])
    else:
        print("Not found")

def retrieve_transactionSender(transactionID):
    db = sqlite3.connect("app.db")
    db.row_factory = sqlite3.Row
    cr = db.cursor()
    cr.execute(f"SELECT sender FROM transactions WHERE transactionID = {transactionID}")
    row = cr.fetchone()
    db.close()
    if row is not None:
        print(row["sender"])
    else:
        print("Not found")

def retrieve_transactionReceiver(transactionID):
    db = sqlite3.connect("app.db")
    db.row_factory = sqlite3.Row
    cr = db.cursor()
    cr.execute(
        f"SELECT receiver FROM transactions WHERE transactionID = {transactionID}"
    )
    row = cr.fetchone()
    db.close()
    if row is not None:
        print(row["receiver"])
    else:
        print("Not found")

def retrieve_transactionID():
    db = sqlite3.connect("src/app.db")
    db.row_factory = sqlite3.Row
    cr = db.cursor()
    cr.execute("SELECT transactionID FROM variables")
    row = cr.fetchone()
    db.close()
    if row is not None:
        return row["transactionID"]
    else:
        return "Not found"
    
def reset_transactionID():
    db = sqlite3.connect("src/app.db")
    cr = db.cursor()
    cr.execute(f"UPDATE variables SET transactionID = (0)")
    db.commit()
    db.close()

def update_transactionID():
    db = sqlite3.connect("src/app.db")
    db.row_factory = sqlite3.Row  # Add this line
    cr = db.cursor()
    cr.execute("SELECT transactionID FROM variables")
    row = cr.fetchone()
    if row is not None:
        transactionID = row["transactionID"]
        cr.execute("UPDATE variables SET transactionID = ?", ((transactionID + 1),))
        db.commit()
    db.close()
    return transactionID + 1
################################################################################################################################


