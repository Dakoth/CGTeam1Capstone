from pydantic import BaseModel


class Product(BaseModel):
    id: int
    product_number: str
    description: str
    unit_cost: float

    def __eq__(self, other):
        return self.id == other.id and self.product_number == other.product_number and \
            self.description == other.description and self.unit_cost == other.unit_cost
