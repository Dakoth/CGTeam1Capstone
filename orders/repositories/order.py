import sqlite3
from orders.models.order import Order
from orders.models.product import Product


class OrderRepository():
    db_name = 'orders.db'

    def insert(self, order: Order):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute('INSERT INTO [ORDER] (ORDER_NUMBER, PRODUCT_ID, QUANTITY, TOTAL) VALUES \
                (?, ?, ?, ?)', [order.order_number, order.product.id, order.quantity, round(order.total, 2)])
        order.id = cursor.lastrowid
        return order

    def get_by_number(self, order_number):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute(
                'SELECT ID, ORDER_NUMBER, PRODUCT_ID, QUANTITY, TOTAL FROM [ORDER] WHERE ORDER_NUMBER=?;', [order_number])
        row = cursor.fetchone()
        if row:
            product = Product(id=row[2], product_number='', description='', unit_cost=0.0)
            return Order(id=row[0], order_number=row[1], product=product, quantity=row[3], total=row[4])
        else:
            return None

    def delete(self, id):
        with sqlite3.connect(self.db_name) as db:
            db.execute(
                'DELETE FROM [ORDER] WHERE ID=?;', [id])
