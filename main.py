
"""Baxromov Ruslan"""

# 1 masala --- Postgresql bazaga python yordamida ulaning . Product nomli jadval yarating (id,name,price, color,image)
"""pip install psycopg2"""

import psycopg2

db_name = 'exam'
password = '1436'
host = 'localhost'
port = 5432
user = 'postgres'

conn = psycopg2.connect(dbname=db_name,
                        user=user,
                        password=password,
                        host=host,
                        port=port)

c = conn.cursor()

create_table_query = """CREATE TABLE IF NOT EXISTS products(
             id bigserial PRIMARY KEY,
             product_name  varchar(100) not null,
             color  varchar(100) not null,
             image varchar(200) not null,
             is_liked boolean default false,
             created_at timestamp default current_timestamp,
             updated_at timestamp default current_timestamp);
           """
c.execute(create_table_query)
conn.commit()
print('Table Successfully Created')

def insert_products_query(product_name, color, image):
    try:
        query = "INSERT INTO products (product_name,color, image) VALUES (%s, %s, %s)"
        c.execute(query, (product_name, color, image))
        conn.commit()
        print("Data inserted successfully!")
    except psycopg2.Error as e:
        print(f"Xato inserting data: {e}")

insert_products_query("Samsung", "Black","https://cdn.mediapark.uz/imgs/4ac7c124-1001-4319-92b7-d686232dd879.webp")
insert_products_query("Iphone", "White", "https://assets.asaxiy.uz/product/items/desktop/54072f485cdb7897ebbcaf75251395612023103117384195268j9cIch3f4C.png.webp")


# 2 - masala


# def delete_data(id):
#     try:
#         query = "DELETE FROM products WHERE id = %s"
#         c.execute(query, (id,))
#         conn.commit()
#         print("Data deleted successfully!")
#     except psycopg2.Error as e:
#         print(f"Error deleting data: {e}")
#
# delete_data(1)


# def update_date(id, new_name):
#     try:
#
#         update_query = """Update products set product_name = %s where id = %s"""
#         c.execute(update_query, (new_name, id))
#         conn.commit()
#         results = c.rowcount
#         print(results, "Product Updated successfully ")
#     except (Exception, psycopg2.Error) as error:
#         print("Error in update operation", error)
#
#
# update_date(2, "Changyutgich Tefal TW7690EA")


# def select_data(id, product_name, color, image):
#     try:
#         query = "SELECT * FROM products WHERE id = 2;"
#         c.execute(query, (id, product_name, color, image,))
#         conn.commit()
#         results = c.fetchall()
#         print(results)
#     finally:
#         c.close()
#         conn.close()


# 3 - masala

#
# class Alphabet:
#     def __init__(self):
#         self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         self.index = 0
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#     def __next__(self):
#         if self.index < len(self.letters):
#             letter = self.letters[self.index]
#             self.index += 1
#             return letter
#         else:
#             raise StopIteration
#
#
# alphabet = Alphabet()
#
# for letter in alphabet:
#     print(letter)
#

# 4 - masala

# import threading
# import time
#
#
# def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         time.sleep(1)
#
#
# def print_letters():
#     letters = "ABCDE"
#     for letter in letters:
#         print(letter)
#         time.sleep(1)
#
#
# thread_numbers = threading.Thread(target=print_numbers)
# thread_letters = threading.Thread(target=print_letters)
#
#
# thread_numbers.start()
# thread_letters.start()
#
# thread_numbers.join()
# thread_letters.join()


# 5 - masala

#
# import sqlite3
#
# class Products:
#     def __init__(self, database_name):
#         self.connection = sqlite3.connect(database_name)
#         self.cursor = self.connection.cursor()
#         self.cursor.execute('''
#             CREATE TABLE IF NOT EXISTS products (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 price REAL NOT NULL
#             )
#         ''')
#         self.connection.commit()
#
#     def save(self, name, price):
#         self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
#         self.connection.commit()
#
#     def get_all(self):
#         self.cursor.execute('SELECT * FROM products')
#         return self.cursor.fetchall()
#
# db = Products('company.db')
# db.save('Kompyuter', 1500.00)
# products = db.get_all()
# for product in products:
#     print(product)


# 6 - masala
#
# import psycopg2
#
# class DbConnect:
#     def __init__(self, con):
#         self.con = con
#
#     def __enter__(self):
#         self.conn = psycopg2.connect(**self.con)
#         self.cur = self.conn.cursor()
#         return self.cur
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.conn.commit()
#         self.cur.close()
#         self.conn.close()
#
# con = {
#     'dbname': 'exam',
#     'user': 'postgres',
#     'password': '1436',
#     'host': 'localhost',
#     'port': 5432
# }
#
# with DbConnect(con) as cur:
#     cur.execute("SELECT version();")
#     print(cur.fetchone()[0])


# 7 - masala

import requests
import sqlite3


url = "https://dummyjson.com/products/"
response = requests.get(url)
data = response.json()
products = data['products']


conn = sqlite3.connect('products.db')
cur = conn.cursor()

cur.execute("""
    CREATE TABLE Product(
        id INTEGER PRIMARY KEY,
        title text,
        description text,
        price real,
        discountPercentage real,
        rating real,
        stock int,
        brand text,
        category text,
        thumbnail text)
        """)

for product in response.json()['products']:
    cur.execute('''
        INSERT INTO Product8(id, title, description, price, discountPercentage, rating, stock, brand, category, thumbnail)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (product['id'], product['title'], product['description'], product['price'], product['discountPercentage'],
          product['rating'], product['stock'], product['brand'], product['category'], product['thumbnail']))

conn.commit()
conn.close()


# 8 - masala

# git init
# git add .
# git commit -m "The exam was successfully completed"
# git branch -M master
# git remote add origin https://github.com/bahkromov01/exam-.git
# git push -u origin master

