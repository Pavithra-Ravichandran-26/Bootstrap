balance = 10000

while True:

    print("\n===== SIMPLE BANKING SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("Type 'quit' to exit")

    choice = input("Enter your choice: ")

    if choice.lower() == "quit":
        print("Thank you for using the banking system.")
        break

    if choice == "1":

        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Invalid amount.")
            continue

        balance += amount
        print("Amount deposited successfully.")
        print("Current Balance:", balance)

    elif choice == "2":

        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")
            continue

        if amount > balance:
            print("Insufficient balance.")
            continue

        balance -= amount
        print("Amount withdrawn successfully.")
        print("Current Balance:", balance)

    elif choice == "3":

        print("Current Balance:", balance)

        pass

    else:
        print("Invalid choice. Please try again.")

else:
    print("Banking session completed.")