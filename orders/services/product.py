from orders.models.product import Product
from orders.repositories.product import ProductRepository


class ProductService():
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def add_new(self, product: Product):
        return self.product_repository.insert(product)

    def get_all(self):
        return self.product_repository.get_all()

    def get_one(self, product_number):
        return self.product_repository.get_by_number(product_number)

    def update(self, product: Product):
        return self.product_repository.update(product)