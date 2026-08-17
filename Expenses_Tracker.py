expenses = []
def add_expense():
    print("\n+================================+")
    print("|          Add Expense           |")
    print("+================================+")
    expense_id = input("Enter Expense ID: ")
    name = input("Enter Expense Name: ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    date = input("Enter Date (DD-MM-YYYY): ")
    expense = {
        "id": expense_id,
        "name": name,
        "category": category,
        "amount": amount,
        "date": date
    }
    expenses.append(expense)
    print("Expense Added Successfully!")
def view_expenses():
    print("\n+================================+")
    print("|         View Expenses          |")
    print("+================================+")
    if len(expenses) == 0:
        print("No Expenses Found.")
    else:
        for expense in expenses:
            print(f"ID       : {expense['id']}")
            print(f"Name     : {expense['name']}")
            print(f"Category : {expense['category']}")
            print(f"Amount   : ₹{expense['amount']:.2f}")
            print(f"Date     : {expense['date']}")
            print("--------------------------------")
def categories():
    print("\n+================================+")
    print("|           Categories           |")
    print("+================================+")
    if len(expenses) == 0:
        print("No Expenses Found.")
        return
    category_list = []
    for expense in expenses:
        if expense["category"] not in category_list:
            category_list.append(expense["category"])
    for category in category_list:
        total = 0
        for expense in expenses:
            if expense["category"] == category:
                total += expense["amount"]
        print(f"{category}: ₹{total:.2f}")
def total_spendings():
    print("\n+================================+")
    print("|         Total Spendings        |")
    print("+================================+")
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total Spending: ₹{total:.2f}")
def export_report():
    print("\n+================================+")
    print("|          Export Report         |")
    print("+================================+")
    if len(expenses) == 0:
        print("No Expenses Available.")
        return
    with open("expense_report.txt", "w") as file:
        file.write("========== EXPENSE REPORT ==========\n\n")
        for expense in expenses:
            file.write(f"ID       : {expense['id']}\n")
            file.write(f"Name     : {expense['name']}\n")
            file.write(f"Category : {expense['category']}\n")
            file.write(f"Amount   : ₹{expense['amount']:.2f}\n")
            file.write(f"Date     : {expense['date']}\n")
            file.write("------------------------------------\n")
        total = 0
        for expense in expenses:
            total += expense["amount"]
        file.write(f"\nTotal Spending: ₹{total:.2f}\n")
    print("Report Exported Successfully!")
    print("File Name: expense_report.txt")
def delete_expense():
    print("\n+================================+")
    print("|          Delete Expense        |")
    print("+================================+")
    delete_id = input("Enter Expense ID: ")
    found = False
    for expense in expenses:
        if expense["id"] == delete_id:
            expenses.remove(expense)
            print("Expense Deleted Successfully!")
            found = True
            break
    if not found:
        print("Expense Not Found!")
def search_expense():
    print("\n+================================+")
    print("|          Search Expense        |")
    print("+================================+")
    search = input("Enter Expense Name or Category: ").lower()
    found = False
    for expense in expenses:
        if (search in expense["name"].lower() or
                search in expense["category"].lower()):
            print("\nExpense Found!")
            print(f"ID       : {expense['id']}")
            print(f"Name     : {expense['name']}")
            print(f"Category : {expense['category']}")
            print(f"Amount   : ₹{expense['amount']:.2f}")
            print(f"Date     : {expense['date']}")
            found = True
    if not found:
        print("Expense Not Found!")
def update_expense():
    print("\n+================================+")
    print("|          Update Expense        |")
    print("+================================+")
    update_id = input("Enter Expense ID: ")
    found = False
    for expense in expenses:
        if expense["id"] == update_id:
            print("Expense Found!")
            expense["name"] = input("Enter New Name: ")
            expense["category"] = input("Enter New Category: ")
            expense["amount"] = float(input("Enter New Amount: "))
            expense["date"] = input("Enter New Date: ")
            print("Expense Updated Successfully!")
            found = True
            break
    if not found:
        print("Expense Not Found!")
def monthly_summary():
    print("\n+================================+")
    print("|         Monthly Summary        |")
    print("+================================+")
    month = input("Enter Month (MM): ")
    total = 0
    found = False
    for expense in expenses:
        date = expense["date"]
        expense_month = date[3:5]
        if expense_month == month:
            total += expense["amount"]
            found = True
    if found:
        print(f"Total Spending for Month {month}: ₹{total:.2f}")
    else:
        print("No Expenses Found for this Month.")
def highest_expense():
    print("\n+================================+")
    print("|         Highest Expense        |")
    print("+================================+")
    if len(expenses) == 0:
        print("No Expenses Found.")
        return
    highest = expenses[0]
    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense
    print(f"Expense : {highest['name']}")
    print(f"Category: {highest['category']}")
    print(f"Amount  : ₹{highest['amount']:.2f}")
    print(f"Date    : {highest['date']}")
def lowest_expense():
    print("\n+================================+")
    print("|          Lowest Expense        |")
    print("+================================+")
    if len(expenses) == 0:
        print("No Expenses Found.")
        return
    lowest = expenses[0]
    for expense in expenses:
        if expense["amount"] < lowest["amount"]:
            lowest = expense
    print(f"Expense : {lowest['name']}")
    print(f"Category: {lowest['category']}")
    print(f"Amount  : ₹{lowest['amount']:.2f}")
    print(f"Date    : {lowest['date']}")
while True:
    print("\n+================================+")
    print("|         Expense Tracker        |")
    print("+================================+")
    print("|  1. Add Expense                |")
    print("|  2. View Expenses              |")
    print("|  3. Categories                 |")
    print("|  4. Total Spendings            |")
    print("|  5. Export Report              |")
    print("|  6. Delete Expense             |")
    print("|  7. Search Expense             |")
    print("|  8. Update Expense             |")
    print("|  9. Monthly Summary            |")
    print("| 10. Highest Expense            |")
    print("| 11. Lowest Expense             |")
    print("| 12. Exit                       |")
    print("+================================+")
    try:
        choice = int(input("Choose an Option From 1 To 12: "))
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            categories()
        elif choice == 4:
            total_spendings()
        elif choice == 5:
            export_report()
        elif choice == 6:
            delete_expense()
        elif choice == 7:
            search_expense()
        elif choice == 8:
            update_expense()
        elif choice == 9:
            monthly_summary()
        elif choice == 10:
            highest_expense()
        elif choice == 11:
            lowest_expense()
        elif choice == 12:
            print("\n+================================+")
            print("|       Exited Successfully      |")
            print("+================================+")
            break
        else:
            print("Invalid Choice!")
            print("Please Choose Correct Choice!")
    except ValueError:
        print("Please Enter Valid Data!")