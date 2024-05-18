import user

def main():
    uname = input("Enter your name: ")
    upin = input("Enter your PIN: ")
    user1 = user.Authentication(uname)
    check = user1.validate_user(upin)
    if check:
        print("Access granted!")
    else:
        print("Access denied!")


main()