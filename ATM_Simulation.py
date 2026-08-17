users = {
    "Vishnu": {
        "customer_id": "CUS1001",
        "name": "Palakonda Vishnu",
        "account": "1234567890",
        "account_type": "Savings",
        "pin": 1234,
        "balance": 56000,
        "phone": "7780441516",
        "email": "vishnu@example.com",
        "date_of_birth": "15-08-2006",
        "gender": "Male",
        "address": "Ongole",
        "city": "Ongole",
        "state": "Andhra Pradesh",
        "branch": "Ongole Main Branch",
        "ifsc": "BANK0001001",
        "account_status": "Active",
        "last_login": "17-08-2026 10:15 AM",
        "daily_withdrawal_limit": 25000,
        "total_withdrawn_today": 0,
        "transactions": []
    },
    "Kelvin": {
        "customer_id": "CUS1002",
        "name": "Kelvin Kumar",
        "account": "9876543210",
        "account_type": "Current",
        "pin": 5678,
        "balance": 98000,
        "phone": "9948037288",
        "email": "kelvin@example.com",
        "date_of_birth": "21-03-2005",
        "gender": "Male",
        "address": "Vijayawada",
        "city": "Vijayawada",
        "state": "Andhra Pradesh",
        "branch": "Vijayawada Main Branch",
        "ifsc": "BANK0001002",
        "account_status": "Active",
        "last_login": "17-08-2026 09:45 AM",
        "daily_withdrawal_limit": 50000,
        "total_withdrawn_today": 0,
        "transactions": []
    },
    "Alexa": {
        "customer_id": "CUS1003",
        "name": "Jhon Alexa",
        "account": "1478523690",
        "account_type": "Savings",
        "pin": 9012,
        "balance": 78000,
        "phone": "6304111169",
        "email": "alexa@example.com",
        "date_of_birth": "10-11-2006",
        "gender": "Female",
        "address": "Guntur",
        "city": "Guntur",
        "state": "Andhra Pradesh",
        "branch": "Guntur Main Branch",
        "ifsc": "BANK0001003",
        "account_status": "Active",
        "last_login": "17-08-2026 08:30 AM",
        "daily_withdrawal_limit": 30000,
        "total_withdrawn_today": 0,
        "transactions": []
    }
}
print("+======================================+")
print("|          WELCOME TO PYTHON ATM       |")
print("+======================================+")
user_name = input("Please enter your name (e.g., jhon): ").strip().capitalize()
if user_name not in users:
    print("+======================================+")
    print("|          USER NOT FOUND              |")
    print("+======================================+")
    print("Please check your username.")
else:
    user = users[user_name]
    if user["account_status"] != "Active":
        print("+======================================+")
        print("|        ACCOUNT NOT ACTIVE            |")
        print("+======================================+")
        print("Please contact your bank.")
    else:
        account_verified = False
        acc_attempt = 3
        while acc_attempt > 0:
            try:
                user_account = input("Please Enter Your Account Number: ").strip()
                if user["account"] == user_account:
                    account_verified = True
                    break
                else:
                    acc_attempt -= 1
                    print("Incorrect Account Number.")
                    print("Attempts Remaining:", acc_attempt)
            except ValueError:
                print("Please enter a valid account number.")
        if not account_verified:
            print("+======================================+")
            print("|             ACCESS DENIED            |")
            print("+======================================+")
            print("Maximum account attempts reached.")
        else:
            pin_verified = False
            pin_attempt = 3
            while pin_attempt > 0:
                try:
                    user_pin = int(input("Please Enter Your PIN: "))
                    if user["pin"] == user_pin:
                        pin_verified = True
                        break
                    else:
                        pin_attempt -= 1
                        print("Incorrect PIN.")
                        print("Attempts Remaining:", pin_attempt)
                except ValueError:
                    print("Please enter numbers only.")
            if not pin_verified:
                print("+======================================+")
                print("|             ACCESS DENIED            |")
                print("+======================================+")
                print("Maximum PIN attempts reached.")
            else:
                print("+======================================+")
                print("|            ACCESS GRANTED             |")
                print("+======================================+")
                while True:
                    print("\n")
                    print("+======================================+")
                    print("|              ATM MENU                |")
                    print("+======================================+")
                    print("| 1. Check Balance                     |")
                    print("| 2. Withdraw Money                    |")
                    print("| 3. Deposit Money                     |")
                    print("| 4. Change PIN                        |")
                    print("| 5. Fetch My Details                  |")
                    print("| 6. Transaction History               |")
                    print("| 7. Daily Withdrawal Information      |")
                    print("| 8. Exit                              |")
                    print("+======================================+")
                    try:
                        user_choice = int(input("Please Enter Your Choice (1-8): "))
                    except ValueError:
                        print("Please enter a number from 1 to 8.")
                        continue
                    if user_choice == 1:
                        print("\n+======================================+")
                        print("|           ACCOUNT BALANCE             |")
                        print("+======================================+")
                        print("Customer ID :", user["customer_id"])
                        print("Holder Name :", user["name"])
                        print("Account No  :", user["account"])
                        print("Account Type:", user["account_type"])
                        print("Balance     :", user["balance"])
                    elif user_choice == 2:
                        print("\n+======================================+")
                        print("|           WITHDRAW MONEY             |")
                        print("+======================================+")
                        try:
                            withdraw_amount = float(input("Please Enter Amount to Withdraw: "))
                            if withdraw_amount <= 0:
                                print("Please enter a valid amount.")
                            elif withdraw_amount > user["balance"]:
                                print("+======================================+")
                                print("|         INSUFFICIENT BALANCE         |")
                                print("+======================================+")
                                print("Available Balance:",user["balance"])
                            elif (user["total_withdrawn_today"]+withdraw_amount>user["daily_withdrawal_limit"]):
                                remaining_limit = (user["daily_withdrawal_limit"]-user["total_withdrawn_today"])
                                print("Daily withdrawal limit exceeded.")
                                print("Remaining Withdrawal Limit:",remaining_limit)
                            else:
                                user["balance"] -= withdraw_amount
                                user["total_withdrawn_today"] +=(withdraw_amount)
                                user["transactions"].append({"type": "Withdrawal","amount": withdraw_amount,"balance_after": user["balance"]})
                                print("+======================================+")
                                print("|       WITHDRAWAL SUCCESSFUL           |")
                                print("+======================================+")
                                print("Withdrawn Amount:",withdraw_amount)
                                print("Remaining Balance:",user["balance"])
                                print("Please collect your cash.")
                                print("Thank You!")
                        except ValueError:
                            print("Please enter a valid amount.")
                    elif user_choice == 3:
                        print("\n+======================================+")
                        print("|            DEPOSIT MONEY             |")
                        print("+======================================+")
                        try:
                            deposit_amount = float(input("Please Enter Amount to Deposit: "))
                            if deposit_amount <= 0:
                                print("Please enter a valid amount.")
                            else:
                                user["balance"] += deposit_amount
                                user["transactions"].append({"type": "Deposit","amount": deposit_amount,"balance_after": user["balance"]})
                                print("+======================================+")
                                print("|         DEPOSIT SUCCESSFUL            |")
                                print("+======================================+")
                                print("Deposited Amount:",deposit_amount)
                                print("New Balance:",user["balance"])
                        except ValueError:
                            print("Please enter a valid amount.")
                    elif user_choice == 4:
                        print("\n+======================================+")
                        print("|              CHANGE PIN              |")
                        print("+======================================+")
                        try:
                            changed_pin = int(input("Please Enter Your New PIN: "))
                            verified_pin = int(input("Please Re-Enter Your New PIN: "))
                            if changed_pin != verified_pin:
                                print("PINs do not match.")
                            elif not (1000 <= changed_pin <= 9999):
                                print("PIN must contain exactly 4 digits.")
                            elif changed_pin == user["pin"]:
                                print("New PIN cannot be the same as""your current PIN.")
                            else:
                                user["pin"] = changed_pin
                                print("PIN Changed Successfully.")
                        except ValueError:
                            print("Please enter numbers only.")
                    elif user_choice == 5:
                        print("\n+======================================+")
                        print("|           HOLDER DETAILS             |")
                        print("+======================================+")
                        print("Customer ID      :", user["customer_id"])
                        print("Name             :", user["name"])
                        print("Account Number   :", user["account"])
                        print("Account Type     :", user["account_type"])
                        print("Phone            :", user["phone"])
                        print("Email            :", user["email"])
                        print("Date of Birth    :", user["date_of_birth"])
                        print("Gender           :", user["gender"])
                        print("Address          :", user["address"])
                        print("City             :", user["city"])
                        print("State            :", user["state"])
                        print("Branch           :", user["branch"])
                        print("IFSC             :", user["ifsc"])
                        print("Account Status   :", user["account_status"])
                        print("Last Login       :", user["last_login"])
                    elif user_choice == 6:
                        print("\n+======================================+")
                        print("|        TRANSACTION HISTORY           |")
                        print("+======================================+")
                        if len(user["transactions"]) == 0:
                            print("No transactions available.")
                        else:
                            for transaction in user["transactions"]:
                                print("--------------------------------------")
                                print("Type:",transaction["type"])
                                print("Amount:",transaction["amount"])
                                print("Balance After:",transaction["balance_after"])
                            print("--------------------------------------")
                    elif user_choice == 7:
                        print("\n+======================================+")
                        print("|       DAILY WITHDRAWAL INFO           |")
                        print("+======================================+")
                        daily_limit = user["daily_withdrawal_limit"]
                        withdrawn_today = user["total_withdrawn_today"]
                        remaining_limit = (daily_limit - withdrawn_today)
                        print("Daily Limit       :",daily_limit)
                        print("Withdrawn Today   :",withdrawn_today)
                        print("Remaining Limit   :",remaining_limit)
                    elif user_choice == 8:
                        print("+======================================+")
                        print("|         EXITED SUCCESSFULLY           |")
                        print("+======================================+")
                        print("Thank You for using Python ATM.")
                        break
                    else:
                        print("Please choose a correct option (1-8).")