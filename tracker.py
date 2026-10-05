# Expense Tracker - Installment 3
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
subTotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subTotal += amount2

#Calculation
average = subTotal / 2

taxPercent = float(input("Tax rate (%)? "))
tax = subTotal * (taxPercent / 100)

total = subTotal + tax

budget = float(input("Your budget? "))
overBudget = total > budget

leftBudget = budget - total

print(f"\n{"-" * 40}")
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Subtotal:\t${subTotal}")
print(f"Average:\t${average}")
print(f"Tax ({taxPercent}%):\t${tax}")
print(f"Grand Total:\t${total}")
print(f"Over budget?\t{overBudget}")
print(f"Left in budget:\t${leftBudget}")
print("-" * 40)

print("Made by: KEN LONGANILLA BALINGWAY | Installment 3")
