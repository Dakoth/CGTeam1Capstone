from orders.models.order import Order
from orders.repositories.order import OrderRepository
from orders.repositories.product import ProductRepository


class OrderService():
    def __init__(self, order_repository: OrderRepository, product_repository: ProductRepository):
        self.order_repository = order_repository
        self.product_respository = product_repository

    def add_new(self, order: Order):
        product = self.product_respository.get_by_id(order.product.id)
        order.product = product
        order.total = order.product.unit_cost * order.quantity
        return self.order_repository.insert(order)

    def get_one(self, order_number):
        order = self.order_repository.get_by_number(order_number)
        product = self.product_respository.get_by_id(order.product.id)
        order.product = product
        return order
