def bank_statement(Current_balance, Amount):
    
    if (Current_balance >= Amount):
        Current_balance = Current_balance - Amount
        return Current_balance

balance = bank_statement(1000, 200)

if balance >= 500:
    print("Withdrawal successful")
else:
    print("Make a deposit")