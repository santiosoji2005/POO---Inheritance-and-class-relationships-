from typing import List
from Model.invoice import Invoice
from Model.line_item import LineItem
from .db import invoices_db

def create_invoice(client, invoice_date):
    invoice = Invoice(client, invoice_date)
    invoices_db.append(invoice)
    try:
        client.add_invoice(invoice)
    except Exception:
        if hasattr(client, 'invoices'):
            client.invoices.append(invoice)
    return invoice

def add_item_to_invoice(invoice: Invoice, product, quantity: int = 1) -> LineItem:
    item = LineItem(product, quantity)
    invoice.add_item(item)
    return item

def add_product_to_invoice(invoice: Invoice, product):
    invoice.add_product(product)
    return invoice.items[-1]  

def calculate_invoice_total(invoice: Invoice):
    invoice.calculate_total()  
    return invoice.total_value

def list_invoices() -> List[Invoice]:
    return list(invoices_db)
