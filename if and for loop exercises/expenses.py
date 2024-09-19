expenses = [1200, 1300, 1500, 1700]
total_expense = 0

for i, expense in enumerate(expenses):
    print(f"month {i + 1} , expense: {expense}")
    total_expense += expense
print('total : ', total_expense)