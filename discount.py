import datetime

# Get the current date
current_date = datetime.datetime.now().date()

# Get the subtotal from the user
subtotal = float(input("Enter the subtotal: $"))

# Check if today is Tuesday or Wednesday and subtotal is $50 or greater
if (current_date.strftime('%A') == 'Tuesday' or current_date.strftime('%A') == 'Wednesday') and subtotal >= 50:
    discount = subtotal * 0.10
else:
    discount = 0

# Calculate the sales tax and total amount due
sales_tax_rate = 0.06
sales_tax = subtotal * sales_tax_rate
total_amount_due = subtotal - discount + sales_tax

# Print the results
print("Discount Amount: $", discount)
print("Sales Tax Amount: $", sales_tax)
print("Total Amount Due: $", total_amount_due)
