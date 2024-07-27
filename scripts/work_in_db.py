#import library
import sqlite3 

#connect data base
connection = sqlite3.connect('products.db')
cursor = connection.cursor()

#create data base
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Products(
    categories TEXT NOT NULL,
    name_product TEXT NOT NULL,
    code_product INTEGER,
    data_start TEXT NOT NULL,
    finished INTEGER,
    value INTEGER
    )
    '''
)

#function add product in data base
def add_data(categories,name_product,code_product,data_start,finished, value):
    cursor.execute('INSERT INTO Products (categories, name_product, code_product, data_start,finished, value) VALUES (?,?,?,?,?,?)',(categories,name_product,code_product,data_start,finished, value))
    connection.commit()
    #connection.close()

#function vision product in data base
def vision_data():
    select_string = '''SELECT * from Products'''
    cursor.execute(select_string)
    records = cursor.fetchall()
    for row in records:
        print(row)
    connection.commit()
    connection.close()

#function delete product in data base
def delete_data():
    pass

#function update product in data base
def update_data():
    pass


