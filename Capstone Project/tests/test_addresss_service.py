import unittest
from unittest.mock import Mock
#from orders.models.product import Product
from accounts.models.address import Address
from accounts.repositories.address import OrderRepository
from accounts.services.address import OrderService


class TestOrderService(unittest.TestCase):
    def setUp(self):
        #self.product = Product(id=1, product_number="123",
                         # description="desc", unit_cost=1.00)
        self.address = Address(id=1, order_number="456",
                           product=self.product, quantity=1, total=1.00)
        self.product_repository = Mock()
        self.orderRepository = Mock()
        self.orderService = OrderService(self.orderRepository, self.product_repository)

    def test_add_new_order(self):
        self.product_repository.get_by_id = Mock(return_value=self.product)
        self.orderRepository.insert = Mock(return_value=self.address)
        new_order = self.orderService.add_new(self.address)
        self.assertEqual(new_order, self.address)


if __name__ == "__main__":
    unittest.main()
