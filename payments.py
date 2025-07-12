class PaymentGateway:
    def __init__(self):
        self.payments = {}  # username: [amounts]

    def process_payment(self, username, amount):
        if username not in self.payments:
            self.payments[username] = []
        self.payments[username].append(amount)
        return True