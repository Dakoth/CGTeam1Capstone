import unittest
from unittest.mock import Mock
from orders.models.product import Product
from orders.repositories.product import ProductRepository
from orders.services.product import ProductService

class TestProductService(unittest.TestCase):
    def setUp(self):
        self.products = [
            Product(id=1, product_number="123", description="desc", unit_cost=1),
            Product(id=2, product_number="456", description="desc", unit_cost=2)
        ]
        self.productRepository = Mock()
        self.productService = ProductService(self.productRepository)

    def test_get_one_product(self):
        self.productRepository.get_by_number = Mock(return_value=self.products[0])
        get_one_product = self.productService.get_one("000")
        self.assertEqual(get_one_product, self.products[0])

    def test_get_all_products(self):
        self.productRepository.get_all = Mock(return_value=self.products)
        get_all_products = self.productService.get_all()
        self.assertEqual(get_all_products, self.products)

    def test_add_new_(self):
        self.productRepository.insert = Mock(return_value=self.products[0])
        new_product = self.productService.add_new(self.products[0])
        self.assertEqual(new_product, self.products[0])


if __name__ == "__main__":
    unittest.main()
