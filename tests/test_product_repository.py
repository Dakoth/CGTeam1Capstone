import unittest
from orders.models.product import Product
from orders.repositories.product import ProductRepository


class TestProductRepository(unittest.TestCase):
    def setUp(self):
        self.productRepository = ProductRepository()
        self.inserted_product = self.productRepository.insert(Product(id=0, product_number="XXX111",
                                                                      description="Sample Description", unit_cost=1.99))

    def tearDown(self):
        self.productRepository.delete(self.inserted_product.id)

    def test_get_by_id(self):
        get_product = self.productRepository.get_by_id(
            self.inserted_product.id)
        self.assertEqual(get_product, self.inserted_product)

    def test_get_by_number(self):
        get_product = self.productRepository.get_by_number(
            self.inserted_product.product_number)
        self.assertEqual(get_product, self.inserted_product)

    def test_get_all(self):
        inserted_product2 = self.productRepository.insert(Product(id=0, product_number="YYY222",
                                                                  description="Sample Description", unit_cost=2.99))
        products = self.productRepository.get_all()
        self.assertGreaterEqual(len(products), 2)
        self.assertTrue(self.inserted_product in products)
        self.assertTrue(inserted_product2 in products)
        self.productRepository.delete(inserted_product2.id)

    def test_edit_existing(self):
        current = self.productRepository.get_by_id(self.inserted_product.id)
        current.description = 'modified description'
        update = self.productRepository.update(current)
        self.assertEqual(update.id, self.inserted_product.id)
        self.assertEqual(update.product_number, self.inserted_product.product_number)
        self.assertEqual(update.description, 'modified description')
        self.assertEqual(update.unit_cost, self.inserted_product.unit_cost)

        

if __name__ == "__main__":
    unittest.main()
