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
    cursor.close()
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL
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


async def add_user(username: str, email: str, age: int):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'{username}', f'{email}', f'{age}', 1000))
    connection.commit()
    connection.close()


async def is_included(username):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM Users WHERE username = ?)", (username,))
    result = cursor.fetchone()[0]
    connection.close()
    return result

initiate_db()
