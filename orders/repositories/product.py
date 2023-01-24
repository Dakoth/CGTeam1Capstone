import sqlite3
from orders.models.product import Product


class ProductRepository():
    db_name = 'orders.db'

    def get_by_id(self, id):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute(
                'SELECT ID, PRODUCT_NUMBER, DESCRIPTION, UNIT_COST FROM PRODUCT WHERE ID=?;', [id])
        row = cursor.fetchone()
        return Product(id=row[0], product_number=row[1], description=row[2], unit_cost=row[3])

    def get_by_number(self, product_number):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute(
                'SELECT ID, PRODUCT_NUMBER, DESCRIPTION, UNIT_COST FROM PRODUCT WHERE PRODUCT_NUMBER=?;', [product_number])
        row = cursor.fetchone()
        if row:
            return Product(id=row[0], product_number=row[1], description=row[2], unit_cost=row[3])
        else:
            return None

    def get_all(self):
        results = []
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute(
                'SELECT ID, PRODUCT_NUMBER, DESCRIPTION, UNIT_COST FROM PRODUCT;')
        rows = cursor.fetchall()
        for row in rows:
            results.append(
                Product(id=row[0], product_number=row[1], description=row[2], unit_cost=row[3]))
        return results

    def insert(self, product: Product):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute('INSERT INTO PRODUCT (PRODUCT_NUMBER, DESCRIPTION, UNIT_COST) VALUES \
                (?, ?, ?)', [product.product_number, product.description, product.unit_cost])
        product.id = cursor.lastrowid
        return product

    def update(self, product: Product):
        with sqlite3.connect(self.db_name) as db:
            db.execute('UPDATE PRODUCT SET PRODUCT_NUMBER=?, DESCRIPTION=?, UNIT_COST=? WHERE ID=?', 
                [product.product_number, product.description, product.unit_cost, product.id])
        return self.get_by_id(product.id)

    def delete(self, id):
        with sqlite3.connect(self.db_name) as db:
            db.execute('DELETE FROM PRODUCT WHERE ID=?;', [id])
