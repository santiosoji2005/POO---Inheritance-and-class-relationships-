# UI/console_ui.py
import sys
from datetime import date
from CRUD import products_crud, clients_crud, invoices_crud
from CRUD.db import products_db, clients_db, invoices_db
from Model.products import Product
from Model.antibiotic import Antibiotic
from Model.fertilizer_control import Fertilizer
from Model.pest_control import PestControl

def menu():
    while True:
        print("\n=== Agro_Shop - Menú Principal ===")
        print("1. Gestionar clientes")
        print("2. Gestionar productos")
        print("3. Crear venta / Factura")
        print("4. Buscar por cédula (facturas y productos vendidos)")
        print("5. Listar DB simulada (clientes/productos/facturas)")
        print("0. Salir")
        opt = input("Elija una opción: ").strip()
        if opt == "1":
            gestionar_clientes()
        elif opt == "2":
            gestionar_productos()
        elif opt == "3":
            crear_venta()
        elif opt == "4":
            buscar_por_cedula_ui()
        elif opt == "5":
            mostrar_db()
        elif opt == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

def gestionar_clientes():
    print("\n--- Gestionar clientes ---")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("0. Volver")
    opt = input("Elija: ").strip()
    if opt == "1":
        nombre = input("Nombre del cliente: ").strip()
        cedula = input("Identificación: ").strip()
        try:
            c = clients_crud.create_client(nombre, cedula)
            print("Cliente creado:", c.client_name, c.identification_number)
        except Exception as e:
            print("Error:", e)
    elif opt == "2":
        for c in clients_crud.list_clients():
            print(f"- {c.client_name} ({c.identification_number}) - Facturas: {len(getattr(c, 'invoices', []))}")
    else:
        return

def gestionar_productos():
    print("\n--- Gestionar productos ---")
    print("1. Agregar producto simple")
    print("2. Agregar Antibiotic (ejemplo)")
    print("3. Listar productos")
    print("0. Volver")
    opt = input("Elija: ").strip()
    if opt == "1":
        name = input("Nombre: ").strip()
        price = float(input("Precio: ").strip())
        p = Product(name, price)
        products_crud.add_product(p)
        print("Producto agregado.")
    elif opt == "2":
        name = input("Nombre: ").strip()
        dose = input("Dose (ej: 500 o 500Kg): ").strip()
        animal = input("Animal (Bovino/Caprino/Porcino): ").strip()
        price = float(input("Precio: ").strip())
        ab = Antibiotic(name, dose, animal, price)
        products_crud.add_product(ab)
        print("Antibiotic agregado.")
    elif opt == "3":
        for p in products_crud.list_products():
            print(f"- {p.name} ({type(p).__name__}) - ${p.price}")
    else:
        return

def crear_venta():
    cedula = input("Cédula del cliente: ").strip()
    client = clients_crud.get_client_by_id(cedula)
    if not client:
        print("Cliente no encontrado. Cree el cliente primero.")
        return
    inv_date_str = input("Fecha factura (YYYY-MM-DD) o dejar vacío para hoy: ").strip()
    if inv_date_str == "":
        inv_date = date.today()
    else:
        y,m,d = map(int, inv_date_str.split("-"))
        inv_date = date(y,m,d)
    invoice = invoices_crud.create_invoice(client, inv_date)
    while True:
        print("Agregar producto a la factura: (escriba 'done' para terminar)")
        name = input("Nombre del producto: ").strip()
        if name.lower() == "done":
            break
        matches = [p for p in products_crud.list_products() if p.name.lower() == name.lower()]
        if not matches:
            print("Producto no encontrado.")
            continue
        product = matches[0]
        qty = int(input("Cantidad: ").strip() or "1")
        invoices_crud.add_item_to_invoice(invoice, product, qty)
        print("Producto agregado.")
    invoices_crud.calculate_invoice_total(invoice)
    print("Factura creada. Total:", invoice.total)

def buscar_por_cedula_ui():
    cedula = input("Ingrese cédula: ").strip()
    res = clients_crud.buscar_por_cedula(cedula)
    if not res:
        print("Cliente no encontrado o sin facturas.")
        return
    client = res["client"]
    print(f"Cliente: {client.client_name} - {client.identification_number}")
    print("Facturas encontradas:", len(res["invoices"]))
    for i, inv in enumerate(res["invoices"], 1):
        print(f"  Factura #{i} - Fecha: {inv.date} - Total: {inv.total}")
        for it in inv.items:
            print(f"    - {it.product.name} x{it.quantity} = {it.line_total}")
    print("Productos vendidos (lista):")
    for p in res["products_sold"]:
        print(f" - {p.name} ({type(p).__name__}) - ${p.price}")

def mostrar_db():
    print("\n-- Clientes --")
    for c in clients_db:
        print(f"  {c.client_name} ({c.identification_number}) - facturas: {len(getattr(c,'invoices',[]))}")
    print("\n-- Productos --")
    for p in products_db:
        print(f"  {p.name} ({type(p).__name__}) - ${p.price}")
    print("\n-- Facturas --")
    for inv in invoices_db:
        print(f"  Cliente: {inv.client.client_name}, Fecha: {inv.date}, Total: {inv.total}")

if __name__ == "__main__":
    menu()
