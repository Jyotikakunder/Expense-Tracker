import json
try:
    with open("expenses.json","r") as file:
        expensesList=json.load(file)
except FileNotFoundError:
    expensesList=[]
def save_expenses():
    with open("expenses.json","w") as file:
            json.dump(expensesList,file,indent=4)
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
    expense= {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }
    expensesList.append(expense)
    save_expenses()
    print(" \n DONE. Expense is added succesfully")
def view_expenses():
    if( len(expensesList)==0 ):
        print("No Expenses Added. First add the expenses. ")
    else:
        print("===== Your all expenses ======")
        count= 1
        for eachExpense in expensesList:
            print(f"""\nExpense #{count} \nDate:{eachExpense['date']} \nCategory:{eachExpense['category']} \nDescription:{eachExpense['description']} \nAmount:₹{eachExpense['amount']:.2f}""")
            count+=1 
def total_expenses():
    total= 0
    for eachExpense in expensesList:
        total = total + eachExpense["amount"]
    print("\n TOTAL expenses =₹{total:.2f}")
def update_expenses():
    if len(expensesList)==0:
        print("No Expenses Available.")
        return
    view_expenses()
    try:
        update_index=int(input("Enter expense number to update/edit:"))
        if update_index>0 and update_index<=len(expensesList):
            new_category=input("Enter new category:").strip().title()
            new_description=input("Enter new description:").strip()
            while True:
                try:
                    new_amount=float(input("Enter new amount:"))
                    if new_amount<=0:
                        print("Amount must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid amount.")
            expensesList[update_index-1]["category"]=new_category
            expensesList[update_index-1]["description"]=new_description
            expensesList[update_index-1]["amount"]=new_amount
            save_expenses()
            print("Expense updated successfully")
        else:
            print("Invalid Expense number")
    except ValueError:
        print("Please enter valid number")
def delete_expense():
    if len(expensesList)==0:
        print("No Expense Available.")
        return
    view_expenses()
    try:
        delete_index=int(input("Enter expense number to delete:"))
        if delete_index>0 and delete_index<=len(expensesList):
            expensesList.pop(delete_index-1)
            save_expenses()
            print("Expense deleted successfully")
        else:
            print("Invalid Expense number")
    except ValueError:
        print("Please Enter valid ")
print(" Welcome to Expense Tracker : ")
while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Update/Edit Expenses")
    print("5. Delete an Expense")
    print("6. Exit")
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
        delete_expense()
    elif(choice == 6):
        print("Thank You for using our system")
        break
    else:
        print("INVALID CHOICE. TRY AGAIN")
