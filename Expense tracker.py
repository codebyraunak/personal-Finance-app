expenseslist=[]
print("welcome to Expense tracker:Try to reduce your expenses")
while True:
    print("-----menu-----")
    print("1.Add Expenses")
    print("2.View all Expenses")
    print("3.view total Expenses")
    print("4.Exit")

    choice = int(input("Please Enter Your Choice :"))
    if(choice == 1):
        Date=input("When did you spend the money?:")
        Category= input("What kind of spending did you do?(Food,Travel,Book):")
        Discription=input("You Can Add More Detail:")
        Amount=float(input("Enter The Amount:"))

        expense= {
            "Date": Date,
            "Category": Category,
            "Discription":Discription,
            "Amount":Amount,
             }
        expenseslist.append(expense)
        
        print("\n Expense is added sucessfully")

    elif(choice == 2):
        if(len(expenseslist)==0):
            print("No expense is added")
        else:
            print("Here Are Your Expenses")
            count=1
            for eachexpense in expenseslist:
                print(f"Expense Number {count}->{eachexpense["Date"]},{eachexpense["Category"]},{eachexpense["Discription"]},{eachexpense["Amount"]}")
                count=count+1

    elif(choice == 3):
        total=0
        for eachexpense in expenseslist:
            total=total+eachexpense["amount"]
            print("\n Total expense=",total)

    elif(choice == 4):
        print("Exit")
        break
    else:
        print("Invalid choice")