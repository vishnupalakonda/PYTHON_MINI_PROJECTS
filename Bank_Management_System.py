accounts = []
def create_account():
    print("\n+================================+")
    print("|        Account Creation       |")
    print("+================================+")
    account_number = input("Enter Account Number: ")
    for account in accounts:
        if account["account_number"] == account_number:
            print("Account Number Already Exists!")
            return
    name = input("Enter Account Holder Name: ")
    phone = input("Enter Phone Number: ")
    account_type = input("Enter Account Type (Savings/Current): ")
    try:
        initial_deposit = float(input("Enter Initial Deposit: "))
        if initial_deposit < 0:
            print("Deposit Cannot Be Negative!")
            return
    except ValueError:
        print("Please Enter a Valid Amount!")
        return
    account = {
        "account_number": account_number,
        "name": name,
        "phone": phone,
        "account_type": account_type,
        "balance": initial_deposit,
        "transactions": []
    }
    if initial_deposit > 0:
        account["transactions"].append(
            f"Initial Deposit: ₹{initial_deposit:.2f}"
        )
    accounts.append(account)
    print("Account Created Successfully!")
def find_account(account_number):
    for account in accounts:
        if account["account_number"] == account_number:
            return account
    return None
def view_account():
    print("\n+================================+")
    print("|          View Account          |")
    print("+================================+")
    account_number = input("Enter Account Number: ")
    account = find_account(account_number)
    if account is None:
        print("Account Not Found!")
        return
    print("\nAccount Details")
    print("--------------------------------")
    print(f"Account Number : {account['account_number']}")
    print(f"Name           : {account['name']}")
    print(f"Phone          : {account['phone']}")
    print(f"Account Type   : {account['account_type']}")
    print(f"Balance        : ₹{account['balance']:.2f}")
    print("--------------------------------")
def deposit_money():
    print("\n+================================+")
    print("|          Deposit Money         |")
    print("+================================+")
    account_number = input("Enter Account Number: ")
    account = find_account(account_number)
    if account is None:
        print("Account Not Found!")
        return
    try:
        amount = float(input("Enter Deposit Amount: "))
        if amount <= 0:
            print("Amount Must Be Greater Than Zero!")
            return
    except ValueError:
        print("Please Enter a Valid Amount!")
        return
    account["balance"] += amount
    account["transactions"].append(
        f"Deposited: ₹{amount:.2f}"
    )
    print("Money Deposited Successfully!")
    print(f"Current Balance: ₹{account['balance']:.2f}")
def withdraw_money():
    print("\n+================================+")
    print("|         Withdraw Money         |")
    print("+================================+")
    account_number = input("Enter Account Number: ")
    account = find_account(account_number)
    if account is None:
        print("Account Not Found!")
        return
    try:
        amount = float(input("Enter Withdrawal Amount: "))
        if amount <= 0:
            print("Amount Must Be Greater Than Zero!")
            return
    except ValueError:
        print("Please Enter a Valid Amount!")
        return
    if amount > account["balance"]:
        print("Insufficient Balance!")
        return
    account["balance"] -= amount
    account["transactions"].append(
        f"Withdrawn: ₹{amount:.2f}"
    )
    print("Money Withdrawn Successfully!")
    print(f"Current Balance: ₹{account['balance']:.2f}")
def transfer_money():
    print("\n+================================+")
    print("|          Transfer Money        |")
    print("+================================+")
    sender_number = input("Enter Your Account Number: ")
    sender = find_account(sender_number)
    if sender is None:
        print("Sender Account Not Found!")
        return
    receiver_number = input("Enter Receiver Account Number: ")
    receiver = find_account(receiver_number)
    if receiver is None:
        print("Receiver Account Not Found!")
        return
    if sender_number == receiver_number:
        print("Cannot Transfer Money to the Same Account!")
        return
    try:
        amount = float(input("Enter Transfer Amount: "))
        if amount <= 0:
            print("Amount Must Be Greater Than Zero!")
            return
    except ValueError:
        print("Please Enter a Valid Amount!")
        return
    if amount > sender["balance"]:
        print("Insufficient Balance!")
        return
    sender["balance"] -= amount
    receiver["balance"] += amount
    sender["transactions"].append(
        f"Transferred ₹{amount:.2f} to {receiver_number}"
    )
    receiver["transactions"].append(
        f"Received ₹{amount:.2f} from {sender_number}"
    )
    print("Money Transferred Successfully!")
    print(f"Your Current Balance: ₹{sender['balance']:.2f}")
def view_transactions():
    print("\n+================================+")
    print("|        View Transactions       |")
    print("+================================+")
    account_number = input("Enter Account Number: ")
    account = find_account(account_number)
    if account is None:
        print("Account Not Found!")
        return
    print("\nTransaction History")
    print("--------------------------------")
    if len(account["transactions"]) == 0:
        print("No Transactions Found.")
    else:
        for i in range(len(account["transactions"])):
            print(
                f"{i + 1}. "
                f"{account['transactions'][i]}"
            )
    print("--------------------------------")
    print(f"Current Balance: ₹{account['balance']:.2f}")
while True:
    print("\n+================================+")
    print("|      Bank Management System    |")
    print("+================================+")
    print("|  1. Account Creation           |")
    print("|  2. View Account               |")
    print("|  3. Deposit Money              |")
    print("|  4. Withdraw Money             |")
    print("|  5. Transfer Money             |")
    print("|  6. View Transactions          |")
    print("|  7. Exit System                |")
    print("+================================+")
    try:
        choice = int(
            input("Choose an Option From 1 To 7: ")
        )
        if choice == 1:
            create_account()
        elif choice == 2:
            view_account()
        elif choice == 3:
            deposit_money()
        elif choice == 4:
            withdraw_money()
        elif choice == 5:
            transfer_money()
        elif choice == 6:
            view_transactions()
        elif choice == 7:
            print("\n+================================+")
            print("|      System Exited Successfully |")
            print("+================================+")
            break
        else:
            print("Invalid Choice!")
            print("Please Choose Correct Choice!")
    except ValueError:
        print("Please Enter a Valid Number!")