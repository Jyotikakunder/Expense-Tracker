import sqlite3
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT,date TEXT,category TEXT,description TEXT,amount REAL)""")
conn.commit()
def add_expense():
    date= input("\nThe date when expense was done(DD/MM/YYYY): ")
    print("Suggested category:Food,Travel,Books,Makeup")
    category= input("Enter category:").strip().title()
    description= input("Add some more detail: ").strip()
    while True:
        try:
            amount= float(input("Enter the amount: "))
            if amount<=0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")
    cursor.execute("""INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)""", (date, category, description, amount))
    conn.commit()
    print("\nDone. Expense is added successfully")
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    if not rows:
        print("No Expenses Available.")
        return
    else:
        print("===== Your all expenses ======")
        for row in rows:
            print(f"""
            Expense #{row[0]}
            Date: {row[1]}
            Category: {row[2]}
            Description: {row[3]}
            Amount: ₹{row[4]:.2f}
            ---------------------------""") 
def total_expenses():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    if total:
        print(f"Total Expenses: ₹{total:.2f}")
    else:
        print("Total Expenses: ₹0.00")
def update_expenses():
    view_expenses()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    if not rows:
        print("No expenses available.")
        return
    try:
        id = int(input("Enter expense ID: "))
    except ValueError:
        print("Invalid input")
        return
    new_category = input("New category: ")
    new_description = input("New description: ")
    while True:
        try:
            new_amount = float(input("New amount: "))
            if new_amount <= 0:
                print("Amount must be greater than 0")
                continue
            break
        except ValueError:
            print("Invalid input")
    cursor.execute("""UPDATE expenses SET category=?, description=?, amount=? WHERE id=?""", (new_category, new_description, new_amount, id))
    conn.commit()
    if cursor.rowcount == 0:
        print("No such expense ID found.")
    else:
        print("Updated successfully")
def filter_by_category():
    category = input("Enter category to filter: ").strip().title()
    cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
    rows = cursor.fetchall()
    if not rows:
        print("No expenses found for this category.")
    else:
        print(f"\nExpenses for category: {category}")
        for row in rows:
            print(f"""Expense #{row[0]}
                      Date: {row[1]}
                      Category: {row[2]}
                      Description: {row[3]}
                      Amount: ₹{row[4]:.2f}""")
def delete_expense():
    view_expenses()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    if not rows:
        print("No expenses available.")
        return
    confirm=input("Are you sure you want to delete?(yes/no):").lower()
    if confirm!="yes":
       print("Deletion cancelled")
       return
    try:
        id = int(input("Enter expense ID: "))
    except ValueError:
        print("Invalid input")
        return
    cursor.execute("DELETE FROM expenses WHERE id=?", (id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("No such expense ID found.")
    else:
        print("Deleted successfully")
print(" Welcome to Expense Tracker : ")
while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Update/Edit Expenses")
    print("5. Search by category")
    print("6. Delete an Expense")
    print("7. Exit")
    try:
        choice= int(input("Please Enter Your Choice : "))
    except ValueError:
        print("Invalid input.Please enter a number.")
        continue
    if (choice==1):
        add_expense()
    elif (choice==2):
        view_expenses()
    elif (choice==3):
        total_expenses()
    elif (choice==4):
        update_expenses()
    elif (choice==5):
        filter_by_category()
    elif (choice==6):
        delete_expense()
    elif(choice ==7):
        print("Thank You for using our system")
        break
    else:
        print("INVALID CHOICE. TRY AGAIN")
conn.close()
