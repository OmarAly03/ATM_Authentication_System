from enum import Enum
from datetime import datetime
from typing import List, Dict, Optional

class TransactionType(Enum):
    DEPOSIT = 1
    WITHDRAWAL = 2

class Transaction:
    def __init__(self, amount: float, date: datetime, type: TransactionType):
        self.amount = amount
        self.date = date
        self.type = type

    def getAmount(self) -> float:
        return self.amount

    def getDate(self) -> datetime:
        return self.date

    def getType(self) -> TransactionType:
        return self.type

class User:
    def __init__(self, username: str, pin: int, uid: int, fingerprint: str):
        self.username = username
        self.pin = pin
        self.uid = uid
        self.fingerprint = fingerprint
        
    def setPin(self, newPin: int):
        self.pin = newPin

    def getUsername(self) -> str:
        return self.username

    def getPin(self) -> int:
        return self.pin

    def getUID(self) -> int:
        return self.uid
    
    def getFingerprint(self) -> str:
        return self.fingerprint

class UserDatabase:
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.transactions: Dict[int, List[Transaction]] = {}
        self.accountNumbers: Dict[int, int] = {}
        self.accountBalances: Dict[int, float] = {}
        self.nationalIDs: Dict[int, int] = {}
        self.phoneNumbers: Dict[int, int] = {}

    def getUserByUID(self, uid: int) -> Optional[User]:
        return self.users.get(uid)

    def validateCredentials(self, username: str, pin: int) -> Optional[User]:
        for user in self.users.values():
            if user.getUsername() == username and user.getPin() == pin:
                return user
        return None

    def getAccountNumber(self, uid: int) -> Optional[int]:
        return self.accountNumbers.get(uid)

    def setAccountNumber(self, uid: int, accountNumber: int):
        self.accountNumbers[uid] = accountNumber

    def getAccountBalance(self, uid: int) -> Optional[float]:
        return self.accountBalances.get(uid)

    def setAccountBalance(self, uid: int, balance: float):
        self.accountBalances[uid] = balance

    def getNationalID(self, uid: int) -> Optional[int]:
        return self.nationalIDs.get(uid)

    def setNationalID(self, uid: int, nationalID: int):
        self.nationalIDs[uid] = nationalID

    def getPhoneNumber(self, uid: int) -> Optional[int]:
        return self.phoneNumbers.get(uid)

    def setPhoneNumber(self, uid: int, phoneNumber: int):
        self.phoneNumbers[uid] = phoneNumber

    def addTransaction(self, uid: int, transaction: Transaction):
        if uid in self.transactions:
            self.transactions[uid].append(transaction)
        else:
            self.transactions[uid] = [transaction]

class Bank:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.atmList = []

    def getName(self) -> str:
        return self.name

    def getLocation(self) -> str:
        return self.location

    def addATM(self, atm):
        self.atmList.append(atm)

    def removeATM(self, atm):
        self.atmList.remove(atm)

class AuthenticationSystem:
    def __init__(self, userDB: UserDatabase):
        self.userDB = userDB

    def authenticateWithFingerprint(self, fingerprint: str) -> Optional[User]:
        for user in self.userDB.users.values():
            if user.getFingerprint() == fingerprint:
                return user
        return None
        
    def authenticateWithUsernameAndPassword(self, username: str, pin: int) -> Optional[User]:
        return self.userDB.validateCredentials(username, pin)

class ATM:
    def __init__(self, userDB: UserDatabase):
        self.authenticatedUser: Optional[User] = None
        self.userDB = userDB

    def showBalance(self) -> Optional[float]:
        if self.authenticatedUser:
            uid = self.authenticatedUser.getUID()
            return self.userDB.getAccountBalance(uid)
        else:
            return None

    def deposit(self, amount: float):
        if self.authenticatedUser:
            uid = self.authenticatedUser.getUID()
            balance = self.userDB.getAccountBalance(uid) or 0
            self.userDB.setAccountBalance(uid, balance + amount)
            self.userDB.addTransaction(uid, Transaction(amount, datetime.now(), TransactionType.DEPOSIT))

    def withdraw(self, amount: float):
        if self.authenticatedUser:
            uid = self.authenticatedUser.getUID()
            balance = self.userDB.getAccountBalance(uid) or 0
            if balance >= amount:
                self.userDB.setAccountBalance(uid, balance - amount)
                self.userDB.addTransaction(uid, Transaction(amount, datetime.now(), TransactionType.WITHDRAWAL))

    def changePin(self, oldPin: int, newPin: int):
        if self.authenticatedUser and self.authenticatedUser.getPin() == oldPin:
            self.authenticatedUser.setPin(newPin)

    def showLatestTransactions(self) -> List[Transaction]:
        if self.authenticatedUser:
            uid = self.authenticatedUser.getUID()
            return self.userDB.transactions.get(uid, [])
