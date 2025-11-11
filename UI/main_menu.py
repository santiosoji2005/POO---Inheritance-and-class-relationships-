from UI.products_ui import products_menu
from UI.clients_ui import clients_menu
from UI.invoices_ui import invoices_menu

def main_menu():
    while True:
        print("\n=== AGRO SHOP ===")
        print("1. Gestionar Productos")
        print("2. Gestionar Clientes")
        print("3. Gestionar Facturas")
        print("4. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            products_menu()
        elif opcion == "2":
            clients_menu()
        elif opcion == "3":
            invoices_menu()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
