# Expense Tracker - Installment 2
# Author: Ken Longanilla Balingway
# A record of two expenses and calculates the total and average

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

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

#Calculation
total = amount1 + amount2
average = total / 2

print(f"\n{"-" * 40}")
print("SUMMARY")
print(f"{f'- {item1}:':<20}${amount1}")
print(f"{f'- {item2}:':<20}${amount2}")
print(f"{'Total spent:':<20}${total}")
print(f"{'Average:':<20}${average}")
print("-" * 40)

print("Made by: KEN LONGANILLA BALINGWAY | Installment 2")
