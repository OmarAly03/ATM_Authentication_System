import sqlite3


##############################################################################################################
def delete_table(table_name):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"DROP TABLE IF EXISTS {table_name}")
    db.commit()
    db.close()
    print(f"Table {table_name} deleted successfully !")


##############################################################################################################
def create_table(table_name):
    db = sqlite3.connect("app.db")
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


##############################################################################################################
def show_table(table_name):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"SELECT * FROM {table_name}")
    print(cr.fetchall())
    db.close()


##############################################################################################################
##############################################################################################################


def add_user(name, uid, accountNumber, accountBalance, nationalID, phoneNumber, PIN):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(
        f"INSERT INTO users (name, uid, accountNumber, accountBalance, nationalID, phoneNumber, PIN) VALUES ('{name}', {uid}, '{accountNumber}', '{accountBalance}', '{nationalID}', '{phoneNumber}', '{PIN}')"
    )
    db.commit()
    db.close()
    print(f"{name} added successfully !")


def delete_user(uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"DELETE FROM users WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"User with uid {uid} deleted successfully !")


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
        uid.strip(),
        accountNumber.strip(),
        accountBalance.strip(),
        nationalID.strip(),
        phoneNumber.strip(),
        PIN.strip(),
    )


###################################################################### Update functions ######################################################################
def update_name(name, uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"UPDATE users SET name = '{name}' WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"Name updated successfully !")


def update_accountNumber(accountNumber, uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"UPDATE users SET accountNumber = '{accountNumber}' WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"Account number updated successfully !")


def update_accountBalance(accountBalance, uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(
        f"UPDATE users SET accountBalance = '{accountBalance}' WHERE uid = {uid}"
    )
    db.commit()
    db.close()
    print(f"Account balance updated successfully !")


def update_nationalID(nationalID, uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"UPDATE users SET nationalID = '{nationalID}' WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"National ID updated successfully !")


def update_phoneNumber(phoneNumber, uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"UPDATE users SET phoneNumber = '{phoneNumber}' WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"Phone number updated successfully !")


def update_PIN(PIN, uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"UPDATE users SET PIN = '{PIN}' WHERE uid = {uid}")
    db.commit()
    db.close()
    print(f"PIN updated successfully !")


#################################################################################################################################################################

########################################################### Retrieve functions ##################################################################################
def retrieve_name(uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"SELECT name FROM users WHERE uid = {uid}")
    row = cr.fetchone()
    db.close()
    if row is not None:
        return row[0]
    else:
        return None


def retrieve_accountNumber(uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"SELECT accountNumber FROM users WHERE uid = {uid}")
    row = cr.fetchone()
    db.close()
    if row is not None:
        return row[0]
    else:
        return None


def retrieve_accountBalance(uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"SELECT accountBalance FROM users WHERE uid = {uid}")
    row = cr.fetchone()
    db.close()
    if row is not None:
        return row[0]
    else:
        return None


def retrieve_nationalID(uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"SELECT nationalID FROM users WHERE uid = {uid}")
    row = cr.fetchone()
    db.close()
    if row is not None:
        return row[0]
    else:
        return None


def retrieve_phoneNumber(uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"SELECT phoneNumber FROM users WHERE uid = {uid}")
    row = cr.fetchone()
    db.close()
    if row is not None:
        return row[0]
    else:
        return None


def retrieve_PIN(uid):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"SELECT PIN FROM users WHERE uid = {uid}")
    row = cr.fetchone()
    db.close()
    if row is not None:
        return row[0]
    else:
        return None


#################################################################################################################################################################

