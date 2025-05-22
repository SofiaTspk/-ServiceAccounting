# client_management_system/logic.py
from database import get_connection

def add_client(name, phone, address, services):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (name, phone, address, services) VALUES (?, ?, ?, ?)",
                   (name, phone, address, services))
    conn.commit()
    conn.close()

def view_clients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    conn.close()
    return clients

def edit_client(client_id, name, phone, address, services):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE clients SET name=?, phone=?, address=?, services=? WHERE id=?
    """, (name, phone, address, services, client_id))
    conn.commit()
    conn.close()

def delete_client(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE id=?", (client_id,))
    conn.commit()
    conn.close()

def generate_bill(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, services FROM clients WHERE id=?", (client_id,))
    client = cursor.fetchone()
    conn.close()
    if client:
        name, services = client
        # Спрощений розрахунок: кількість послуг * 100 грн
        service_list = services.split(',')
        total = len(service_list) * 100
        return f"Рахунок для {name}: {total} грн за послуги: {services}"
    else:
        return "Клієнт не знайдений."