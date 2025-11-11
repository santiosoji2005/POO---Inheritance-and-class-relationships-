# CRUD/clients_crud.py
from typing import Optional, List
from Model.client import Client
from .db import clients_db, invoices_db

def create_client(client_name: str, identification_number: str) -> Client:
    # evitar duplicados por cédula
    existing = get_client_by_id(identification_number)
    if existing:
        raise ValueError("Ya existe un cliente con esa identificación.")
    client = Client(client_name, identification_number)
    clients_db.append(client)
    return client

def list_clients() -> List[Client]:
    return list(clients_db)

def get_client_by_id(identification_number: str) -> Optional[Client]:
    for c in clients_db:
        if c.identification_number == identification_number:
            return c
    return None

def buscar_por_cedula(identification_number: str):
    client = get_client_by_id(identification_number)
    if not client:
        return None
    
    client_invoices = [inv for inv in invoices_db if getattr(inv, 'client', None) is client or (hasattr(inv, 'client') and inv.client.identification_number == identification_number)]

    productos = []
    for inv in client_invoices:
        productos.extend(inv.products)  
    return {
        "client": client,
        "invoices": client_invoices,
        "products_sold": productos
    }
