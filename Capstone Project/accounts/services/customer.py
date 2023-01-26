from ast import Add
from audioop import add
from accounts.repositories.customer import CustomerRepository #f key
from accounts.repositories.address import AddressRepository # f key

class CustomerService():
    def __init__(self, customer_repository: CustomerRepository,
            address_repository: AddressRepository) -> None:
        self.customer_repository = customer_repository
        self.address_repository = address_repository


    #def get_all(self):
    #    return self.customer_repository.get_by_id()
