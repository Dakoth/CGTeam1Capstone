import sqlite3
conn = sqlite3.connect('orders.db')

print('Opened database successfully')

conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCT
        (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        PRODUCT_NUMBER VARCHAR(10) NOT NULL,
        DESCRIPTION VARCHAR(50) NOT NULL,
        UNIT_COST DECIMAL(8, 2) NOT NULL);''')
print('Product table ready')

conn.execute('''CREATE TABLE IF NOT EXISTS [ORDER]
        (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        ORDER_NUMBER VARCHAR(10) NOT NULL,
        PRODUCT_ID INTEGER NOT NULL,
        QUANTITY INTEGER NOT NULL,
        TOTAL DECIMAL(8, 2) NOT NULL,
        FOREIGN KEY (PRODUCT_ID)
            REFERENCES PRODUCT (PRODUCT_ID));''')
print('Order table ready')

conn.close()
