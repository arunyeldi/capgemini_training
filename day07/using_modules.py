from collection_of_modules import module_customer, module_order_items

class Transaction:
    def __init__(self, customer, order):
        self.transaction_details = {
            "Customer Details": customer.get_details(),
            "Order Details": order.get_details()
        }

    def print_transaction(self):
        print("Transaction Details:")
        for key, value in self.transaction_details.items():
            print(key, "->", value)

customer = module_customer.Customer(1, "Arun", "arun@example.com")
order = module_order_items.OrderItem(100, 1, "30-01-2025", "Laptop", 1, 75000)

transaction = Transaction(customer, order)
transaction.print_transaction()
