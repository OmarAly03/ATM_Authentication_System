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

