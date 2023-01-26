from pydantic import BaseModel
from accounts.models.address import Address

class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Address
    email: str

def __eq__(self, other):
    return self.id == other.id and self.first_name == other.first_name and \
        self.last_name == other.last_name and self.address_id == other.address_id and self.email == other.email