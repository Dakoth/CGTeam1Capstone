import unittest
from unittest.mock import Mock
from orders.models.product import Product
from orders.models.order import Order
from orders.repositories.order import OrderRepository
from orders.services.order import OrderService


class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.product = Product(id=1, product_number="123",
                          description="desc", unit_cost=1.00)
        self.order = Order(id=1, order_number="456",
                           product=self.product, quantity=1, total=1.00)
        self.product_repository = Mock()
        self.orderRepository = Mock()
        self.orderService = OrderService(self.orderRepository, self.product_repository)

    def test_add_new_order(self):
        self.product_repository.get_by_id = Mock(return_value=self.product)
        self.orderRepository.insert = Mock(return_value=self.order)
        new_order = self.orderService.add_new(self.order)
        self.assertEqual(new_order, self.order)

    def test_get_one_order(self):
        self.orderRepository.get_by_number = Mock(return_value=self.order)
        get_order = self.orderService.get_one("000")
        self.assertEqual(get_order, self.order)


if __name__ == "__main__":
    unittest.main()
