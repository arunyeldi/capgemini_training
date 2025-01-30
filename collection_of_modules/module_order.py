class Order:
    def __init__(self, order_id, customer_id, order_date):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date

    def get_details(self):
        return {"Order ID": self.order_id, "Customer ID": self.customer_id, "Order Date": self.order_date}