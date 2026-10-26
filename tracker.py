
# Expense Tracker - Installment 5
# Author: Ken Longanilla Balingway
# Tracks expenses, tax, total spending, and remaining budget.

print("=" * 40)
print(f"{'EXPENSE TRACKER':^40}")
print(f"{'Track your spending wisely':^40}")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate (%)? "))
budget = float(input("Your budget? "))

print(f"\nWelcome, {name}!")

subtotal = 0
count = 0
choice = ""

while choice != "4":
    print("\nMAIN MENU")
    print(f"{'1. Add an expense':<25}(coming soon)")
    print(f"{'2. View all expenses':<25}(coming soon)")
    print(f"{'3. Show total spent':<25}(coming soon)")
    print(f"{'4. Exit':<25}(coming soon)")

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print("Huge expense - are you sure?")
        elif amount > 100:
            print("Big expense.")
        elif amount > 50:
            print("Moderate expense.")
        else:
            print("Small expense.")

    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left_budget = budget - total

        print("-" * 40)
        print("SUMMARY")
        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal:.2f}")
        print(f"Tax ({tax_percent}%):\t${tax:.2f}")
        print(f"Grand total:\t${total:.2f}")

        over_budget = total > budget

        if over_budget:
            print(f"Over budget by ${total - budget:.2f}!")
        elif total > budget * 0.90:
            print(f"Careful: only ${left_budget:.2f} left.")
        else:
            print(f"Within budget. ${left_budget:.2f} left.")

        print("-" * 40)

    elif choice == "4":
        print(f"Goodbye, {name}!")

    else:
        print("Please choose 1, 2, 3 or 4.")

print("Made by: Ken Longanilla Balingway | Installment 5")
