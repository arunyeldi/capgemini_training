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