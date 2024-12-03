import sqlite3


def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')


def add_in_table():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (id, title, description, price) VALUES ( ?, ?, ?)",
                       (f"Продукт {i}", f"Описание {i}", i * 100))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, description, price FROM Products")
    total = cursor.fetchall()
    connection.close()
    return total


initiate_db()
