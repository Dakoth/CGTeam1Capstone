import unittest
from orders.models.product import Product
from orders.models.order import Order
from orders.repositories.product import ProductRepository
from orders.repositories.order import OrderRepository


class TestOrderRepository(unittest.TestCase):
    def setUp(self):
        self.orderRepository = OrderRepository()
        self.inserted_order = \
            self.orderRepository.insert(Order(
                id=0, order_number="12345678", product=Product(id=1, product_number='', description='', unit_cost=0.0), quantity=1, total=1.99))

    def tearDown(self):
        self.orderRepository.delete(self.inserted_order.id)

    def test_get_by_number(self):
        get_order = self.orderRepository.get_by_number(
            self.inserted_order.order_number)
        self.assertEqual(get_order, self.inserted_order)


if __name__ == "__main__":
    unittest.main()
