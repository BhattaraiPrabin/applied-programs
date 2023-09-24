# Function to calculate the electricity bill
def calculate_bill(units_consumed):
    if units_consumed < 80:
        unit_price = 4
        discount = 0
        service_charge = 0
    elif units_consumed < 150:
        unit_price = 10
        discount = 5
        service_charge = 5
    elif units_consumed < 250:
        unit_price = 12
        discount = 8
        service_charge = 5
    elif units_consumed < 350:
        unit_price = 15
        discount = 10
        service_charge = 8
    elif units_consumed < 500:
        unit_price = 18
        discount = 12
        service_charge = 10
    else:
        unit_price = 20
        discount = 15
        service_charge = 12

    bill_amount = units_consumed * unit_price
    total_discount = (bill_amount * discount) / 100
    total_amount = bill_amount + service_charge
    price_after_discount = total_amount - total_discount

    return unit_price, discount, service_charge, bill_amount, total_amount, total_discount, price_after_discount

# Input
print("****************Unicampus Electricity Company***************")
print("Putalisadak, Kathmandu")
print("------------------------------------------------------------------------")
customer_name = input("Please enter Name of the Customer: ")
customer_address = input("Please enter Address of the Customer: ")
customer_phone = input("Please enter Phone No of the Customer: ")
units_consumed = int(input("Please enter Number of Unit you consumed: "))

# Calculate the bill
unit_price, discount, service_charge, bill_amount, total_amount, total_discount, price_after_discount = calculate_bill(units_consumed)

# Output
print("\n****************Unicampus Electricity Company***************")
print("Putalisadak, Kathmandu")
print("------------------------------------------------------------------------")
print(f"CustomerName: {customer_name}\tAddress: {customer_address}")
print(f"Phone: {customer_phone}\tTotal Unit Consumed: {units_consumed}")
print(f"Bill Amount: {bill_amount}\tService Charge: {service_charge}")
print(f"Total Amount: {total_amount}\tTotal discount: {total_discount}")
print(f"Price After Discount Amount: {price_after_discount}")

print(f"\nYour total bill is: {bill_amount} + {service_charge} = {total_amount}.")
print(f"{customer_name}, you got a {discount}% discount, and the discount price is {total_discount}.")
print(f"After discount Amount is {price_after_discount}.")
