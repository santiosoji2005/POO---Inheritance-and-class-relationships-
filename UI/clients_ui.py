from CRUD.clients_crud import ClientsCRUD

clients_crud = ClientsCRUD()

def clients_menu():
    while True:
        print("\n--- Clientes ---")
        print("1. Crear Cliente")
        print("2. Listar Clientes")
        print("3. Eliminar Cliente")
        print("4. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":
            name = input("Nombre: ")
            cid = input("Identificación: ")
            c = clients_crud.create_client(name, cid)
            print("Cliente creado:", c.client_name)

        elif opcion == "2":
            for c in clients_crud.list_clients():
                print(f"- {c.client_name} ({c.identification_number})")

        elif opcion == "3":
            cid = input("Identificación a eliminar: ")
            ok = clients_crud.delete_client(cid)
            print("Eliminado" if ok else "Cliente no encontrado")

        elif opcion == "4":
            break

        else:
            print("Opción inválida.")
