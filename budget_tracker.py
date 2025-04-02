print("Welcome to the Budget Tracker!")
print("This is where you'll manage your income and expenses.\n")

balance = 0

while True:
    print("1. Add income")
    print("2. Add expense")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        balance += amount
        print(f"✅ Income added. New balance: ${balance:.2f}\n")

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        balance -= amount
        print(f"💸 Expense recorded. New balance: ${balance:.2f}\n")

    elif choice == "3":
        print(f"📊 Current balance: ${balance:.2f}\n")

    elif choice == "4":
        print("👋 Goodbye! Thanks for using the Budget Tracker.")
        break

    else:
        print("❌ Invalid choice. Please select 1, 2, 3, or 4.\n")
