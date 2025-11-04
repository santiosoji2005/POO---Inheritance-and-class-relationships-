from datetime import date

class Product:
    def __init__(self, product_name: str, product_price: float):
        if not product_name or product_name.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if product_price <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        
        self.name = product_name
        self.price = product_price
