"""
ATMApp Class:

- authenticate_fingerprint(self)
- authenticate_pass(self)
- screen_deposit1(self)
- screen_deposit2(self)
- screen_withdraw1(self)
- screen_withdraw2(self)
- screen_show_account_details(self)
- screen_transfer1(self)
- screen_transfer2(self)
- screen_transfer3(self)
- screen_show_latest_transaction(self)
- clear_frame(self)

"""



import tkinter as tk
from tkinter import messagebox
import user
import serial

sent = False
userID = 0
condition = False
serial_port = serial.Serial('COM16', 9600, timeout=1)


class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Authentication System")
        self.root.geometry("1000x450")
        self.root.resizable(False, False)

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.trials = 3
        self.messasge = None
        self.amount = None
        self.user1 = None
        self.username_entry = None
        self.password_entry = None
        self.username = None
        self.password = None
        self.fingerprint = None

        self.inactivity_timer = None
        self.inactivity_period = 60000

        self.screen1()

    def screen1(self):
        self.clear_frame()

        label = tk.Label(self.frame, text="Welcome!", font=("Arial", 18))
        label.pack(pady=60)

        start_button = tk.Button(
            self.frame, text="Press to start", command=self.screen2, font=("Arial", 14)
        )
        start_button.pack(pady=20)

    def reset_inactivity_timer(self):
        if self.inactivity_timer is not None:
            self.root.after_cancel(self.inactivity_timer)
        self.inactivity_timer = self.root.after(
            self.inactivity_period, self.destroy_root
        )

    def destroy_root(self):
        self.screen6("Session Ended!")

    def screen2(self):
        self.clear_frame()

        label = tk.Label(self.frame, text="Please enter username", font=("Arial", 14))
        label.pack(pady=20)

        self.username_entry = tk.Entry(self.frame, font=("Arial", 14))
        self.username_entry.pack(pady=5)

        next_button = tk.Button(
            self.frame, text="Next", command=self.submit1, font=("Arial", 14)
        )
        next_button.pack(pady=20)

        self.reset_inactivity_timer()
        self.username_entry.bind("<Key>", lambda event: self.reset_inactivity_timer())

    def submit1(self):
        self.username = self.username_entry.get()
        print(self.username)
        self.choice_screen()

    def choice_screen(self):
        self.clear_frame()

        label = tk.Label(
            self.frame,
            text="Choose desired input (Fingerprint / PIN)",
            font=("Arial", 14),
        )
        label.pack(pady=20)

        fingerprint_button = tk.Button(
            self.frame, text="Fingerprint", command=self.screen3_alternative, font=("Arial", 14)
        )
        fingerprint_button.pack(pady=5)

        pin_button = tk.Button(
            self.frame, text="PIN", command=self.screen3, font=("Arial", 14)
        )
        pin_button.pack(pady=5)

    def screen3(self):
        self.clear_frame()

        label = tk.Label(
            self.frame,
            text="Please enter password",
            font=("Arial", 14),
        )
        label.pack(pady=20)

        self.password_entry = tk.Entry(self.frame, show="*", font=("Arial", 14))
        self.password_entry.pack(pady=5)

        next_button = tk.Button(
            self.frame, text="Next", command=self.submit2, font=("Arial", 14)
        )
        next_button.pack(pady=20)

        self.reset_inactivity_timer()
        self.password_entry.bind("<Key>", lambda event: self.reset_inactivity_timer())

        if self.trials == 0:
            self.screen6("You have exceeded the number of trials!")

    def submit2(self):
        self.password = self.password_entry.get()
        print(self.password)
        self.authenticate_pass()
    

    def screen3_alternative(self):
        global serial_port
        self.clear_frame()

        label = tk.Label(
            self.frame,
            text="Please scan your fingerprint",
            font=("Arial", 14),
        )
        label.pack(pady=20)
        root.after(1000, self.try_except, serial_port)
    
    def try_except(self, serial_port):
        global sent
        sent = False
        global userID
        global condition
        try:
            while (sent == False):
                global condition
                condition = False
                data = serial_port.readline().decode().strip()
                matchStatus = data.split(": ", 1)
                if matchStatus[0] == "Fingerprint match":
                    userID = matchStatus[1]
                    print(userID)
                    sent = True
                    if userID is not None:
                        condition = True
                        self.authenticate_fingerprint()
                
                else:
                    print("No Match found")

        except KeyboardInterrupt:
            serial_port.close()
            print("Serial connection closed.")

            self.reset_inactivity_timer()


    def authenticate_fingerprint(self):
        global userID
        global condition
        self.user1 = user.Authentication(self.username)
        # self.user1.uid = userID
        self.fingerprint = condition
        self.password = self.user1.getPIN()
        # check = self.user1.validate_user(self.password)

        try:
            check = self.user1.validate_user(self.password)
        except Exception as e:
            self.screen6("This user doesn't exist in the database")
            return
        
        print(self.user1.getUID())
        print(userID)
        if ((int(self.user1.getUID()) == int(userID)) and (check == True)):
            self.screen4()
        else:
            self.screen3()

    def authenticate_pass(self):
        try:
            self.user1 = user.Authentication(self.username)
            check = self.user1.validate_user(self.password)
        except Exception as e:
            self.screen6("This user doesn't exist in the database")
            return


        if check:
            self.screen4()

        elif self.trials != 0:
            self.trials -= 1
            messagebox.showerror(
                "Authentication Failed",
                f"Invalid password\nYou have {self.trials} trial(s) left",
            )
            self.screen3()

    def screen4(self):
        self.clear_frame()

        label = tk.Label(self.frame, text="Welcome", font=("Arial", 18))
        label.pack(pady=60)

        next_button = tk.Button(
            self.frame, text="Next", command=self.screen5, font=("Arial", 14)
        )
        next_button.pack(pady=20)

        self.reset_inactivity_timer()

    def screen5(self):
        self.clear_frame()

        label = tk.Label(
            self.frame,
            text="Which service would you like to use today?",
            font=("Arial", 14),
        )
        label.pack(pady=20)

        services = [
            "Balance",
            "Deposit",
            "Withdraw",
            "Show Account Details",
            "Transfer",
            "Show Latest Transaction",
        ]
        for service in services:
            button = tk.Button(
                self.frame,
                text=service,
                command=lambda s=service: self.service_action(s),
                font=("Arial", 12),
            )
            button.pack(pady=5)

        close_button = tk.Button(
            self.frame, text="Close", command=self.screen6, font=("Arial", 12)
        )
        close_button.pack(pady=20)

        self.reset_inactivity_timer()

    def service_action(self, service):
        if service == "Balance":
            self.screen_balance()
        elif service == "Deposit":
            self.screen_deposit1()
        elif service == "Withdraw":
            self.screen_withdraw1()
        elif service == "Show Account Details":
            self.screen_show_account_details()
        elif service == "Transfer":
            self.screen_transfer1()
        elif service == "Show Latest Transaction":
            self.screen_show_latest_transaction()

    def screen_balance(self):
        self.clear_frame()
        balance = self.user1.getAccountBalance()
        label = tk.Label(
            self.frame, text=f"Your account balance is: {balance}", font=("Arial", 14)
        )
        label.pack(pady=20)
        back_button = tk.Button(
            self.frame, text="Back", command=self.screen5, font=("Arial", 14)
        )
        back_button.pack(pady=20)

        self.reset_inactivity_timer()

    def countdown(self, seconds, message):
        self.clear_frame()
        label = tk.Label(self.frame, text=message, font=("Arial", 14))
        label.pack(pady=20)
        label = tk.Label(
            self.frame, text=f"Waiting for {seconds} seconds...", font=("Arial", 14)
        )

        if seconds > 0:
            label.pack(pady=20)
            root.after(1000, self.countdown, seconds - 1, self.messasge)
        else:
            self.screen1()

    def screen_deposit1(self):
        self.clear_frame()
        label = tk.Label(self.frame, text="Deposit Amount", font=("Arial", 18))
        label.pack(pady=20)
        self.amount = tk.Entry(self.frame, font=("Arial", 14))
        self.amount.pack()
        back_button = tk.Button(
            self.frame, text="Next", command=self.screen_deposit2, font=("Arial", 14)
        )
        back_button.pack(pady=20)

        self.reset_inactivity_timer()
        self.amount.bind("<Key>", lambda event: self.reset_inactivity_timer())

    def screen_deposit2(self):
        amount = int(self.amount.get())
        self.clear_frame()
        deposit_result = self.user1.deposit(amount)
        result_label = tk.Label(
            self.frame,
            text=f"{amount} is Deposited\nUpdated Balance: {self.user1.getAccountBalance()}",
            font=("Arial", 14),
        )
        result_label.pack(pady=20)

        back_button = tk.Button(
            self.frame, text="Back", command=self.screen5, font=("Arial", 14)
        )
        back_button.pack(pady=20)

        self.reset_inactivity_timer()

    def screen_withdraw1(self):
        self.clear_frame()
        label = tk.Label(self.frame, text="Withdrawal Amount", font=("Arial", 18))
        label.pack(pady=20)
        self.amount = tk.Entry(self.frame, font=("Arial", 14))
        self.amount.pack()
        back_button = tk.Button(
            self.frame, text="Next", command=self.screen_withdraw2, font=("Arial", 14)
        )
        back_button.pack(pady=20)

        self.reset_inactivity_timer()
        self.amount.bind("<Key>", lambda event: self.reset_inactivity_timer())

    def screen_withdraw2(self):
        amount = int(self.amount.get())
        self.clear_frame()
        withdraw_result = self.user1.withdraw(amount)
        if withdraw_result:
            result_label = tk.Label(
                self.frame,
                text=f"You withdrawed {amount} successfully\nUpdated Balance: {self.user1.getAccountBalance()}",
                font=("Arial", 14),
            )
            result_label.pack(pady=20)
        else:
            result_label = tk.Label(
                self.frame,
                text=f"Insuffecient Amount\nAvailable Balance: {self.user1.getAccountBalance()}",
                font=("Arial", 14),
            )
            result_label.pack(pady=20)

        back_button = tk.Button(
            self.frame, text="Back", command=self.screen5, font=("Arial", 14)
        )
        back_button.pack(pady=20)

        self.reset_inactivity_timer()

    def screen_show_account_details(self):
        self.clear_frame()
        label = tk.Label(self.frame, text="Account Details", font=("Arial", 18))
        label.pack(pady=20)
        result_label = tk.Label(
            self.frame,
            text=f"Your balance is: {self.user1.getAccountBalance()}\nYour account number is: {self.user1.getAccountNumber()}\nYour national ID is: {self.user1.getNationalID()}\nYour phone number is: {self.user1.getPhoneNumber()}",
            font=("Arial", 14),
        )
        result_label.pack(pady=20)

        back_button = tk.Button(
            self.frame, text="Back", command=self.screen5, font=("Arial", 14)
        )
        back_button.pack(pady=20)

        self.reset_inactivity_timer()

    def screen_transfer1(self):
        self.clear_frame()
        label = tk.Label(
            self.frame, text="Enter the recipient's name", font=("Arial", 18)
        )
        label.pack(pady=20)
        self.username_entry = tk.Entry(self.frame, font=("Arial", 14))
        self.username_entry.pack()
        back_button = tk.Button(
            self.frame, text="Next", command=self.screen_transfer2, font=("Arial", 14)
        )
        back_button.pack(pady=20)

        self.reset_inactivity_timer()
        self.username_entry.bind("<Key>", lambda event: self.reset_inactivity_timer())

    def screen_transfer2(self):
        self.username = self.username_entry.get()
        self.clear_frame()
        label = tk.Label(
            self.frame, text="Enter the transfer amount", font=("Arial", 18)
        )
        label.pack(pady=20)
        self.amount = tk.Entry(self.frame, font=("Arial", 14))
        self.amount.pack()
        back_button = tk.Button(
            self.frame, text="Next", command=self.screen_transfer3, font=("Arial", 14)
        )
        back_button.pack(pady=20)

        self.reset_inactivity_timer()
        self.amount.bind("<Key>", lambda event: self.reset_inactivity_timer())

    def screen_transfer3(self):
        amount = int(self.amount.get())
        self.clear_frame()
        try:
            transaction = self.user1.makeTransaction(self.username, amount)
        except Exception as e:
            messagebox.showerror(
                "Error", f"The entered recipient doesn't exist in the database"
            )
            self.screen5()
            return

        if transaction:
            transfer_result = f"Transfered {amount} to {self.username}\nUpdated Balance: {self.user1.getAccountBalance()}"
        else:
            transfer_result = f"Insuffecient Amount\nAvailable Balance: {self.user1.getAccountBalance()}"
        result_label = tk.Label(self.frame, text=transfer_result, font=("Arial", 14))
        result_label.pack(pady=20)

        back_button = tk.Button(
            self.frame, text="Back", command=self.screen5, font=("Arial", 14)
        )
        back_button.pack(pady=20)

        self.reset_inactivity_timer()

    def screen_show_latest_transaction(self):
        self.clear_frame()
        label = tk.Label(self.frame, text="Latest Transactions", font=("Arial", 18))
        label.pack(pady=20)
        latest_transaction = self.user1.showLatestTransactions()
        result_label = tk.Label(self.frame, text=latest_transaction, font=("Arial", 14))
        result_label.pack(pady=20)

        back_button = tk.Button(
            self.frame, text="Back", command=self.screen5, font=("Arial", 14)
        )
        back_button.pack(pady=20)

        self.reset_inactivity_timer()

    def screen6(self, message="See you soon!"):
        self.messasge = message
        self.countdown(5, self.messasge)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()