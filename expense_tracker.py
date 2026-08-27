print("=" * 40)
print("   WELCOME TO EXPENSE TRACKER")
print("=" * 40)

name = input("What is your name?")
print(f"\nHello {name}! Let's start tracking your expenses.\n")
print("(Type 'done' instead of the expense name to finish)\n")

expenses = []
total = 0.0

while True:
    expense_name = input("Enter expense name (or 'done'): ")

    if expense_name.lower() == 'done':
      break

    while True: 
        try:
            amount = float(input("Enter amount in USD: $"))
            break
        except ValueError:
            print("❌ Invalid input! please enter a number.")

    expenses.append((expense_name, amount))
    total += amount
    print(f"✅ Added: {expense_name} (${amount:.2f})")
    print(f"  Total so far: ${total:.2f}\n")

if not expenses:
        print("\n⚠ you didn't add any expenses. Exiting program." )
else:
    while True:
         try:
               budget = float(input("\nEnter your monthly budget: $"))
               break 
         except ValueError:
              print("❌ Invalid input! please enter a valid number.")

    print("\n" + "=" * 40)
    print("       FINAL EXPENSE REPORT")
    print("=" * 40)
    print(f"User: {name}")
    print(f"Number of expenses : {len(expenses)}")
    print("-" * 40)

    for i in range(len(expenses)):
        expense_name = expenses[i][0]
        amount = expenses[i][1]
        print(f"{i+1}. {expense_name:<20} ${amount:.2f}")

    print("-" * 40)
    print(f"💰 Total spent: ${total:.2f}")
    print(f"📊 your budget: ${budget:.2f}")

    if total > budget:
        overspent = total - budget
        print(f"\n❌ WARNING: You are exceeded your budget by ${overspent:.2f}!")
        print(f"  Try to reduce unnecessary expenses next month.")
    else:
        remaining = budget - total
        print(f"\n✅ Congratulations! You are within your budget.")
        print(f"  Remaining balance: ${remaining:.2f}")

    print("=" * 40)
    print(f"Thank you for using Expense Track , {name}!")