from pydantic import BaseModel
from accounts.models.customer import Customer

class Account(BaseModel):
    id: int
    account_number: str
    customer: Customer
    current_balance: float

def __eq__(self, other):
    return self.id == other.id and self.account_number == other.account_number and \
        self.customer_id == other.customer_id and self.current_balance == other.current_balance