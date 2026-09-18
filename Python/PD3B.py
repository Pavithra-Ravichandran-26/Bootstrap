bill_amount = float(input("Enter your total bill amount: ₹"))

if bill_amount >= 5000:
    discount_rate = 20
elif bill_amount >= 3000:
    discount_rate = 10
elif bill_amount >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount = bill_amount * discount_rate / 100
final_amount = bill_amount - discount

print("\n==============================")
print("       SHOPPING BILL")
print("==============================")
print(f"Total Bill Amount : ₹{bill_amount:.2f}")
print(f"Discount Applied  : ₹{discount:.2f}")
print(f"Final Bill Amount : ₹{final_amount:.2f}")
print("==============================")