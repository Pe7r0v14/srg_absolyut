import sqlite3
from prompt import string as ps
from prompt import integer as pi
#connect
connection = sqlite3.connect('products.db')
cursor = connection.cursor()
#create
cursor.execute(
'''
CREATE TABLE IF NOT EXISTS Products(
categories TEXT NOT NULL,
name_products TEXT NOT NULL,
code_product INTEGER,
data_start TEXT NOT NULL,
finished INTEGER,
value INTEGER
)
'''
)
#add products
def add_product():
    print('Welcome, do you want add products?')
    categories = ps('Cat')
    name_products = ps('Name')
    code_product = pi('Integer')
    data_start = pi('Data start')
    finished = pi('Finished')
    value = pi('KOlichestvo')
    cursor.execute('INSERT INTO Products (categories, name_products, code_product, data_start,finished, value) VALUES (?,?,?,?,?,?)',(categories,name_products,code_product,data_start,finished, value))
    connection.commit()

def select_data():
    select_string = '''SELECT * from Products'''
    cursor.execute(select_string)
    records = cursor.fetchall()
    for row in records:
        print(row)
    connection.commit()

select_data()


connection.close()


