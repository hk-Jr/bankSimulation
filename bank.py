
initial_balance = int(input("Enter initial balance: ₹"))
deposit = int(input("Enter deposit amount: ₹"))

new_balance = initial_balance + deposit
print(f"Initial Balance: Rs.{initial_balance}\nDeposit: Rs.{deposit}\nNew Balance after deposit: Rs.{new_balance}")

#added withdraw feauture.
withdraw = float(input("Enter withdrawal amount: ₹"))
if withdraw > new_balance:
    print("Insufficient balance! Withdrawal not possible.")
else:
    final_balance = new_balance - withdraw
    print("Withdraw: ₹", withdraw)
    print("Final Balance: ₹", final_balance)