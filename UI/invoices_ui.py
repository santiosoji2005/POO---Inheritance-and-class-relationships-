from CRUD.invoices_crud import InvoicesCRUD
from CRUD.clients_crud import ClientsCRUD
from CRUD.products_crud import ProductsCRUD
from datetime import date

invoices_crud = InvoicesCRUD()
clients_crud = ClientsCRUD()
products_crud = ProductsCRUD()

def invoices_menu():
    while True:
        print("\n--- Facturas ---")
        print("1. Crear Factura")
        print("2. Agregar Producto a Factura")
        print("3. Listar Facturas")
        print("4. Volver")

        op = input("Seleccione: ")

        if op == "1":
            cid = input("ID Cliente: ")
            client = clients_crud.find_client(cid)
            if not client:
                print("Cliente no existe.")
                continue
            yyyy, mm, dd = map(int, input("Fecha factura YYYY-MM-DD: ").split("-"))
            inv = invoices_crud.create_invoice(client, date(yyyy, mm, dd))
            print("Factura creada.")

        elif op == "2":
            cid = input("ID Cliente de la factura: ")
            invs = invoices_crud.find_invoice_by_client(cid)
            if not invs:
                print("No hay facturas.")
                continue
            invoice = invs[-1]  # Usa la última factura

            pname = input("Nombre del producto: ")
            product = products_crud.find_by_name(pname)
            if not product:
                print("Producto no existe.")
                continue
            qty = int(input("Cantidad: "))
            invoices_crud.add_product_to_invoice(invoice, product, qty)
            print("Producto agregado.")

        elif op == "3":
            for inv in invoices_crud.list_invoices():
                print(f"Cliente: {inv.client.client_name} | Total: {inv.total}")

        elif op == "4":
            break

        else:
            print("Opción inválida.")
