# client_management_system/ui.py
from logic import add_client, view_clients, edit_client, delete_client, generate_bill

def main_menu():
    while True:
        print("\n1. Додати клієнта")
        print("2. Перегляд клієнтів")
        print("3. Редагувати клієнта")
        print("4. Видалити клієнта")
        print("5. Вивести рахунок")
        print("6. Вихід")
        
        choice = input("Виберіть опцію: ")

        if choice == '1':
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            address = input("Адреса: ")
            services = input("Послуги (через кому): ")
            add_client(name, phone, address, services)
            print("Клієнта додано.")
        elif choice == '2':
            for client in view_clients():
                print(client)
        elif choice == '3':
            client_id = int(input("ID клієнта: "))
            name = input("Нове ім'я: ")
            phone = input("Новий телефон: ")
            address = input("Нова адреса: ")
            services = input("Нові послуги: ")
            edit_client(client_id, name, phone, address, services)
            print("Дані оновлено.")
        elif choice == '4':
            client_id = int(input("ID клієнта: "))
            delete_client(client_id)
            print("Клієнта видалено.")
        elif choice == '5':
            client_id = int(input("ID клієнта: "))
            print(generate_bill(client_id))
        elif choice == '6':
            break
        else:
            print("Невірна опція, спробуйте ще раз.")