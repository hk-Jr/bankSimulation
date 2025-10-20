balance_i = int(input("Enter initial balance: ₹"))
deposit = int(input("Enter deposit amount: ₹"))

new_b= balance_i + deposit
print(f"Initial Balance: Rs.{balance_i}\nDeposit: Rs.{deposit}\nNew Balance after deposit: Rs.{new_b}")

#added withdraw feauture.
withdraw = float(input("Enter withdrawal amount: ₹"))
if withdraw > new_b:
    print("Insufficient balance! Withdrawal not possible.")
else:
    final_b = new_b - withdraw
    print("Withdraw: ₹", withdraw)
    print("Final Balance: ₹", final_b)