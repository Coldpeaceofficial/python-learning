def bank_statement(Current_balance, Amount):
    
    if (Current_balance >= Amount):
        Current_balance = Current_balance - Amount
        print("The balance is", Current_balance)
    else:
        print("Insufficient Funds")

bank_statement(1000, 200)

