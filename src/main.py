import user

def main():
    uname = input("Enter your name: ")
    upin = input("Enter your PIN: ")

    try:
        user1 = user.Authentication(uname)
        check = user1.validate_user(upin)
    except Exception as e:
        print("\nWrong Credentials. Please try again later.")
        return

    if check:
        print("Access granted!")
    else:
        print("Access denied!") 

    while True:
        print("""########################################
How can we help you today ?\n
1. Check Balance
2. Show Account Details
3. Deposit
4. Withdraw
5. Make a Transaction
6. Show Latest Transactions 
7. Exit\n
""")

        choice = input("Enter your choice: ")
        if choice == "1":
            print("Your account balance is: ", user1.getAccountBalance())

        elif choice == "2":
            print("Your account number is: ", user1.getAccountNumber())
            print("Your national ID is: ", user1.getNationalID())
            print("Your phone number is: ", user1.getPhoneNumber())

        elif choice == "3":
            amount = int(input("Enter the amount you want to deposit: "))
            user1.deposit(amount)

        elif choice == "4":
            amount = int(input("Enter the amount you want to withdraw: "))
            user1.withdraw(amount)

        elif choice == "5":
            recipient = input("Enter the recipient's name: ")
            amount = int(input("Enter the amount you want to send: "))
            user1.makeTransaction(recipient, amount)

        elif choice == "6":
            print("Your latest transactions are: ")
            user1.showLatestTransactions()

        elif choice == "7":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice!")
            exit()

main()