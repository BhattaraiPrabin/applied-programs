import datetime

class BillGenerator:
    def __init__(self, heading):
        self.heading = heading
        self.customers = []

    def add_customer(self, name, address, email):
        customer = {
            'name': name,
            'address': address,
            'email': email,
            'items': []
        }
        self.customers.append(customer)

    def add_item(self, name, price, quantity):
        if not self.customers:
            print("No customers added yet. Please add a customer first.")
            return

        try:
            item = {
                'name': name,
                'price': float(price),
                'quantity': int(quantity)
            }
        except ValueError:
            print("Invalid input for price or quantity. Please enter valid numbers.")
            return

        self.customers[-1]['items'].append(item)

    def calculate_total(self, customer):
        total = 0
        for item in customer['items']:
            total += item['price'] * item['quantity']
        return total

    def calculate_discount(self, total):
        discount = 0
        if total <= 5000:
            discount = total * 0.05
        elif total <= 7000:
            discount = (5000 * 0.05) + (total - 5000) * 0.08
        elif total <= 10000:
            discount = (5000 * 0.05) + (2000 * 0.08) + (total - 7000) * 0.10
        else:
            discount = (5000 * 0.05) + (2000 * 0.08) + (3000 * 0.10) + (total - 10000) * 0.15
        return discount

    def generate_bill(self, customer):
        total = self.calculate_total(customer)
        discount = self.calculate_discount(total)
        net_total = total - discount
        return total, discount, net_total

    def save_bill_to_file(self, customer):
        filename = f"bill_{customer['name']}_{datetime.datetime.now().date()}.txt"
        with open(filename, 'w') as bill_file:
            bill_file.write(self.heading)
            bill_file.write(f"Customer Name: {customer['name']}\n")
            bill_file.write(f"Customer Address: {customer['address']}\n")
            bill_file.write(f"Customer Email: {customer['email']}\n\n")
            bill_file.write("{:<20} {:>10} {:>15} {:>15}\n".format("Item Name", "Item Price", "Item Quantity", "Total Price"))
            for item in customer['items']:
                bill_file.write("{:<20} {:>10} {:>15} {:>15}\n".format(item['name'], item['price'], item['quantity'], item['price'] * item['quantity']))
            bill_file.write("\nDiscount: {}\n".format(self.calculate_discount(self.calculate_total(customer))))
            bill_file.write("Net Total: {}\n".format(self.generate_bill(customer)[2]))

def main():
    heading = '''
            Sunway College Bhatbhateni System
                  Maitidevi, Kathmandu    
    '''

    bill_generator = BillGenerator(heading)

    try:
        n = int(input("Enter the number of customers: "))
    except ValueError:
        print("Invalid input for the number of customers. Please enter a valid number.")
        return

    for i in range(n):
        name = input(f"Enter the name of customer [{i+1}]: ")
        address = input(f"Enter the address of customer [{i+1}]: ")
        email = input(f"Enter the email of customer [{i+1}]: ")
        bill_generator.add_customer(name, address, email)

        itemno = int(input(f"Enter the number of items for {name}: "))
        for j in range(itemno):
            itemname = input(f"Enter the name of item [{j+1}]: ")
            itemprice = input(f"Enter the price of item [{j+1}]: ")
            itemqty = input(f"Enter the quantity of item [{j+1}]: ")
            bill_generator.add_item(itemname, itemprice, itemqty)

    for customer in bill_generator.customers:
        total, discount, net_total = bill_generator.generate_bill(customer)
        print(heading)
        print("Customer Name: ", customer['name'])
        print("Customer Address: ", customer['address'])
        print("Customer Email: ", customer['email'])
        print("\n")
        print("{:<20} {:>10} {:>15} {:>15}".format("Item Name", "Item Price", "Item Quantity", "Total Price"))
        for item in customer['items']:
            print("{:<20} {:>10} {:>15} {:>15}".format(item['name'], item['price'], item['quantity'], item['price'] * item['quantity']))
        print("\nDiscount: ", discount)
        print("Net Total: ", net_total)
        print("\n")

        bill_generator.save_bill_to_file(customer)

if __name__ == "__main__":
    main()
