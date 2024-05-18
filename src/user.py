import database
from datetime import datetime

class User:
    def __init__(self, username : str):
        self.username = username
        self.uid = database.retrieve_uid_with_username(username)

    def getUsername(self) -> str:
        return self.username
    
    def getPIN(self) -> int:         
        return database.retrieve_PIN(self.uid)
    
    def getUID(self) -> int:
        return self.uid
    
    def getAccountNumber(self) -> str:
        return database.retrieve_accountNumber(self.uid)
    
    def getAccountBalance(self) -> int:
        return database.retrieve_accountBalance(self.uid)
          
    def getNationalID(self) -> str:
        return database.retrieve_nationalID(self.uid)
        
    def getPhoneNumber(self) -> str:    
        return database.retrieve_phoneNumber(self.uid)
    
    def deposit(self, amount : int):
        currentBalance = database.retrieve_accountBalance(self.uid)
        currentBalance += amount
        database.update_accountBalance(currentBalance, self.uid)
        
        database.update_transactionID()
        temp = int(database.retrieve_transactionID())
        
        now = datetime.now()
        date_string = now.strftime("%Y-%m-%d %H:%M:%S")
        
        database.add_transaction(temp, "deposit", self.uid, date_string, amount, currentBalance, database.retrieve_name(self.uid), "self")
        
        print("Deposit Successful!")

    def withdraw(self, amount : int):
        currentBalance = database.retrieve_accountBalance(self.uid)
        if currentBalance >= amount:
            currentBalance -= amount
            database.update_accountBalance(currentBalance, self.uid)
            
            database.update_transactionID()
            temp = int(database.retrieve_transactionID())
            
            now = datetime.now()
            date_string = now.strftime("%Y-%m-%d %H:%M:%S")
            
            database.add_transaction(temp, "withdraw", self.uid, date_string, amount, currentBalance, database.retrieve_name(self.uid), "self")
            
            print("Withdrawal Successful!")
        else:
            print("Insufficient Amount!")
    
    def makeTransaction(self, recipient : str, amount : int):
        senderBalance = database.retrieve_accountBalance(self.uid)
        recipientUID = database.retrieve_uid_with_username(recipient)
        recipientBalance = database.retrieve_accountBalance(recipientUID)
        if senderBalance >= amount:
            senderBalance -= amount
            recipientBalance += amount
            # Update balances in the database immediately after changing them
            database.update_accountBalance(senderBalance, self.uid)
            database.update_accountBalance(recipientBalance, recipientUID)
            
            database.update_transactionID()
            temp = int(database.retrieve_transactionID())
            
            now = datetime.now()
            date_string = now.strftime("%Y-%m-%d %H:%M:%S")

            database.add_transaction(temp, "transaction", self.uid, date_string, amount, senderBalance, database.retrieve_name(self.uid), recipient)
            
            print("Transaction Successful!")
        else:
            print("Insufficient Amount!")
        
    def showLatestTransactions(self):
        transactions = database.retrieve_accountTransactions(self.uid)
        print(transactions)
         
class Authentication(User):
    def __init__(self, name):
        super().__init__(name)

    def validate_user(self, pin) -> bool:
        return self.getPIN() == pin
    




    
