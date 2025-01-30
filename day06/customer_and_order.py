class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def get_details(self):
        return {"Customer ID": self.customer_id, "Name": self.name, "Email": self.email}

class Order:
    def __init__(self, order_id, customer_id, order_date):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date

    def get_details(self):
        return {"Order ID": self.order_id, "Customer ID": self.customer_id, "Order Date": self.order_date}

class OrderItem(Order):
    def __init__(self, order_id, customer_id, order_date, item_name, quantity, price):
        super().__init__(order_id, customer_id, order_date)
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    def get_details(self):
        order_details = super().get_details()
        order_details.update({"Item Name": self.item_name, "Quantity": self.quantity, "Price": self.price})
        return order_details

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

customer = Customer(1, "Arun", "arun@example.com")
order = OrderItem(100, 1, "30-01-2025", "Laptop", 1, 75000)

transaction = Transaction(customer, order)
transaction.print_transaction()
