from abc import ABC, abstractmethod


class Fraud(Exception):
    pass


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):
        if amount > 1000:
            raise Fraud("Transaction flagged as fraudulent.")
        print(f"Paid {amount} using Credit Card ending with {self.card_number[-4:]}")


class PayPalPayment(Payment):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid {amount} using PayPal account {self.email}")


def process_payment(payment_method: Payment, amount):
    payment_method.pay(amount)


# Example usage:
credit_card = CreditCardPayment("1234567890123456", "John Doe")
paypal = PayPalPayment("john.doe@example.com")
process_payment(credit_card, 500)
process_payment(paypal, 1500)
