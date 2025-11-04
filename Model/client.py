class Client:
    def __init__(self, client_name: str, identification_number: str):
        if not client_name or not identification_number:
            raise ValueError("Name and ID required.")
        self.client_name = client_name
        self.identification_number = identification_number
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)
