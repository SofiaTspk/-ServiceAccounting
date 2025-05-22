# client_management_system/main.py
from database import init_db
from ui import main_menu

if __name__ == "__main__":
    init_db()
    main_menu()