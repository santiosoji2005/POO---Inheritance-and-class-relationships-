class LineItem:
    def __init__(self, product, quantity: int):
        if product is None:
            raise ValueError("No puede ser vacío")
        if quantity <= 0:
            raise ValueError("Debe ser mayor que cero")
        self.product = product
        self.quantity = quantity

    @property
    def line_total(self):
        return self.product.price * self.quantity
