class Payment:
    def process_payment(self):
        print("Payment Processed")

class CreditCardPayment(Payment):
    def process_payment(self):
        print("Credit Card Payment Processed")

class PayPalPayment(Payment):
    def process_payment(self):
        print("Pay Pal Payment Processed")

class BitcoinPayment(Payment):
    def process_payment(self):
        print("Bitcoin Payment Processed")

credit_obj = CreditCardPayment()
credit_obj.process_payment()

paypal_obj = PayPalPayment()
paypal_obj.process_payment()

bitcoin_obj = BitcoinPayment()
bitcoin_obj.process_payment()