from pydantic import BaseModel
from orders.models.product import Product


class Order(BaseModel):
    id: int
    order_number: str
    product: Product
    quantity: int
    total: float

    def __eq__(self, other):
        return self.id == other.id and self.order_number == other.order_number and \
            self.product == other.product and self.quantity == other.quantity and self.total == other.total
