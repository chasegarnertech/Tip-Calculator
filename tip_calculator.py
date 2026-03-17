bill = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter tip percentage: "))

tip = bill * (tip_percentage / 100)
total = bill + tip

print("\n----- TIP CALCULATOR -----")
print("Bill: $" + str(bill))
print("Tip: $" + str(tip))
print("Total: $" + str(total))

