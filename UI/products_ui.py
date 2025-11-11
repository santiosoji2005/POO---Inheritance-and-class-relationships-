from CRUD.products_crud import ProductsCRUD
from datetime import date

products_crud = ProductsCRUD()

def products_menu():
    while True:
        print("\n--- Productos ---")
        print("1. Crear Antibiotico")
        print("2. Crear Fertilizante")
        print("3. Crear Producto Control de Plagas")
        print("4. Listar Productos")
        print("5. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":
            name = input("Nombre: ")
            dose = input("Dosis (Ej: 500): ")
            animal = input("Tipo animal (Bovino/Caprino/Porcino): ")
            price = float(input("Precio: "))
            prod = products_crud.create_antibiotic(name, dose, animal, price)
            print("Creado:", prod.name)

        elif opcion == "2":
            cert = input("Certificado ICA: ")
            name = input("Nombre: ")
            freq = int(input("Frecuencia días: "))
            price = float(input("Precio: "))
            yyyy, mm, dd = map(int, input("Fecha última aplicación (YYYY-MM-DD): ").split("-"))
            last_date = date(yyyy, mm, dd)
            prod = products_crud.create_fertilizer(cert, name, freq, price, last_date)
            print("Creado:", prod.name)

        elif opcion == "3":
            cert = input("Certificado ICA: ")
            name = input("Nombre: ")
            freq = int(input("Frecuencia días: "))
            withdrawal = int(input("Período de retiro: "))
            price = float(input("Precio: "))
            prod = products_crud.create_pest_control(cert, name, freq, withdrawal, price)
            print("Creado:", prod.name)

        elif opcion == "4":
            print("\nLista de productos:")
            for p in products_crud.list_products():
                print(f"- {p.name} (${p.price})")

        elif opcion == "5":
            break

        else:
            print("Opción inválida.")
