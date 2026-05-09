import json
try:
    with open("expenses.json","r") as file:
        expensesList=json.load(file)
except FileNotFoundError:
    expensesList=[]
print(" Welcome to Expense Tracker : ")
while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
    try:
        choice= int(input("Please Enter Your Choice : "))
    except ValueError:
        print("Invalid input.Please enter a number.")
        continue
    if(choice == 1):
        date= input("\nThe date when expense was done(DD/MM/YYYY): ")
        category= input("Type of Expense(Food, Travel, Makeup, Books): ")
        description= input("Add some more detail: ")
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
        with open("expenses.json","w") as file:
            json.dump(expensesList,file,indent=4)
        print(" \n DONE. Expense is added succesfully") 
    elif(choice == 2):
        if( len(expensesList)==0 ):
            print("No Expenses Added. First add the expenses. ")
        else:
           print("===== Your all expenses ======")
           count= 1
           for eachExpense in expensesList:
                print(f"""Expense #{count} Date:{eachExpense['date']} Category:{eachExpense['category']} Description:{eachExpense['description']} Amount:{eachExpense['amount']}""")
                count+=1 
    elif(choice == 3):
        total= 0
        for eachExpense in expensesList:
            total = total + eachExpense["amount"]
        print("\n TOTAL expenses = ", total) 
    elif(choice == 4):
        print("Thank You for using our system")
        break
    else:
        print("INVALID CHOICE. TRY AGAIN")
