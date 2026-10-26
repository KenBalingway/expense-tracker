
# Expense Tracker - Installment 4
# Author: Ken Longanilla Balingway
# Calculates expenses, tax, total spending, and remaining budget.

print("=" * 40)
print(f"{'EXPENSE TRACKER':^40}")
print(f"{'Track your spending wisely':^40}")
print("=" * 40)

print("MAIN MENU")
print(f"{'1. Add an expense':<25}(coming soon)")
print(f"{'2. View all expenses':<25}(coming soon)")
print(f"{'3. Show total spent':<25}(coming soon)")
print(f"{'4. Exit':<25}(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome {name}, Let's log two expenses.\n")

subTotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

if amount1 > 200:
    print("Huge expense - are you sure?")
elif amount1 > 100:
    print("Big expense.")
elif amount1 > 50:
    print("Moderate expense.")
else:
    print("Small expense.")

subTotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

if amount2 > 200:
    print("Huge expense - are you sure?")
elif amount2 > 100:
    print("Big expense.")
elif amount2 > 50:
    print("Moderate expense.")
else:
    print("Small expense.")

subTotal += amount2

if amount1 > 100 and amount2 > 100:
    print("Two big expenses in a row - slow down!")

# Calculation
average = subTotal / 2

taxPercent = float(input("Tax rate (%)? "))
tax = subTotal * (taxPercent / 100)

total = subTotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget

leftBudget = budget - total

print("\n" + "-" * 40)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Subtotal:\t${subTotal}")
print(f"Average:\t${average}")
print(f"Tax ({taxPercent}%):\t${tax}")
print(f"Grand Total:\t${total}")

if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > budget * 0.90:
    print(f"Careful: only ${leftBudget} left.")
else:
    print(f"Within budget. ${leftBudget} left.")

print("-" * 40)
print("Made by: Ken Longanilla Balingway | Installment 4")
