class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def get_details(self):
        return {"Customer ID": self.customer_id, "Name": self.name, "Email": self.email}